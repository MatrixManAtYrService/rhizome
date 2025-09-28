"""Schema synchronization functionality."""

from enum import StrEnum
from pathlib import Path
from typing import Any, cast

import typer

from rhizome.client import RhizomeClient
from rhizome.environments.base import Environment
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, SchemaChangeClassifier
from rhizome.models.table_list import BillingBookkeeperTable, BillingEventTable, BillingTable


def get_database_short_name(environment_name: str) -> str:
    """Extract database short name from environment name.

    Examples:
        DevBillingBookkeeper -> billing_bookkeeper
        NorthAmericaBillingEvent -> billing_event
        NorthAmericaBilling -> billing
    """
    # Remove common prefixes
    name = environment_name.replace("NorthAmerica", "").replace("Dev", "").replace("Demo", "")

    # Convert from PascalCase to snake_case
    # Insert underscore before capital letters (except first)
    result: list[str] = []
    for i, char in enumerate(name):
        if i > 0 and char.isupper():
            result.append("_")
        result.append(char.lower())
    return "".join(result)


def _get_table_enum_for_environment(env_enum: RhizomeEnvironment) -> list[StrEnum] | None:
    """Get the table enum list for a given environment."""
    env_str = str(env_enum)

    if "billing_bookkeeper" in env_str:
        return list(BillingBookkeeperTable)
    elif "billing_event" in env_str:
        return list(BillingEventTable)
    elif "billing" in env_str and "bookkeeper" not in env_str and "event" not in env_str:
        return list(BillingTable)
    else:
        return None


class LightweightEnvironment:
    """Lightweight environment for schema sync that doesn't require table_situation."""

    def __init__(self, env_class: type, client: RhizomeClient) -> None:
        """Initialize with just the essentials needed for schema sync."""
        self.client = client
        self._env_class = env_class

        # Create a temporary instance, but monkey-patch to skip table_situation
        # We need to preserve port forwarding setup for connection strings
        original_init = env_class.__init__

        def patched_init(instance: Environment, client_arg: RhizomeClient) -> None:
            # Set the client attribute directly
            instance.client = client_arg

            # Set up port forwarding if needed (copied from base Environment.__init__)
            port_forward_config = instance.get_port_forward_config()  # type: ignore
            if port_forward_config is not None:
                instance._setup_port_forwarding(port_forward_config)  # type: ignore

            # Skip the table_situation initialization - this is what we want to avoid

        try:
            env_class.__init__ = patched_init  # type: ignore
            self._temp_instance = env_class(client)
        finally:
            env_class.__init__ = original_init  # type: ignore

    @property
    def name(self) -> str:
        """Get environment name."""
        return self._temp_instance.name

    def get_connection_string(self) -> str:
        """Get connection string for database access."""
        return self._temp_instance.get_connection_string()


def _convert_query_result_to_sequence(result: object) -> tuple[Any, ...] | list[Any] | None:
    """Convert SQLAlchemy Row or other result objects to a sequence."""
    if not result or not hasattr(result, "__len__"):
        return None

    if len(cast(Any, result)) == 0:
        return None

    try:
        if hasattr(result, "_tuple"):
            # SQLAlchemy Row to tuple
            return cast(Any, result)._tuple()
        elif isinstance(result, tuple | list):
            return cast(tuple[Any, ...] | list[Any], result)
        else:
            # Try to convert to list
            return list(cast(Any, result))
    except Exception:
        return None


def _sync_table_schema(
    env_instance: object,
    table_name: str,
    file_path: str,
    change_tracker: ChangeTracker,
    errors: list[str],
    verbose: bool,
) -> None:
    """Sync schema for a single table."""
    typer.echo(f"  Syncing table: {table_name}")
    query_str = f"SHOW CREATE TABLE {table_name}"

    try:
        result = cast(Any, env_instance).client.execute_raw_query(
            cast(Any, env_instance).get_connection_string(), query_str
        )
        result_length = len(result) if result and hasattr(result, "__len__") else "N/A"
        typer.echo(f"    Query result type: {type(result)}, length: {result_length}")

        # Convert result to sequence
        result_seq = _convert_query_result_to_sequence(result)

        if result_seq and len(result_seq) > 1:
            # The result of SHOW CREATE TABLE is a tuple, the second element is the statement
            create_table_statement = str(result_seq[1])

            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)

            # Write the file
            with open(file_path, "w") as f:
                f.write(create_table_statement)

            # Track changes to this file
            change_tracker.track_file(file_path)
            typer.echo(f"    ✓ Tracked file: {file_path}")
        else:
            seq_len = len(result_seq) if result_seq else 0
            error_msg = f"Result sequence too short or conversion failed for {table_name}: {seq_len} items"
            errors.append(error_msg)
            typer.echo(f"    ⚠ {error_msg}")

    except Exception as e:
        error_msg = f"Error syncing table {table_name}: {e}"
        errors.append(error_msg)
        if verbose:
            raise
        typer.secho(f"    {error_msg}", fg=typer.colors.RED)


def _sync_environment_schema(
    env_enum: RhizomeEnvironment,
    env_class: type,
    client: RhizomeClient,
    change_tracker: ChangeTracker,
    errors: list[str],
    table_names: list[str] | None,
    verbose: bool,
) -> None:
    """Sync schema for all tables in an environment."""
    # Create lightweight environment instance that doesn't require table_situation
    env_instance = LightweightEnvironment(env_class, client)
    typer.echo(f"Syncing environment: {env_instance.name}")

    # Get environment folder name from the enum value
    env_str = str(env_enum)
    env_folder = "na_prod" if env_str.startswith("na_prod_") else env_str.split("_")[0]

    # Get database short name from the environment name
    db_short_name = get_database_short_name(env_instance.name)

    # Get all tables from the table enum (not from environment.tables())
    table_list = _get_table_enum_for_environment(env_enum)
    if not table_list:
        typer.echo(f"  Warning: No table enum found for {env_enum}")
        return

    # Filter tables if specific table names were provided
    tables_to_sync = table_list
    if table_names:
        # Convert table_names to lowercase for case-insensitive matching
        target_table_names = [name.lower() for name in table_names]
        tables_to_sync = [
            table_name for table_name in table_list
            if str(table_name).lower() in target_table_names
        ]

        # Warn if some specified tables weren't found in this environment
        found_table_names = [str(table_name).lower() for table_name in tables_to_sync]
        missing_tables = [name for name in target_table_names if name not in found_table_names]
        if missing_tables:
            typer.echo(f"  Warning: Tables not found in {env_instance.name}: {', '.join(missing_tables)}")

    # Try to sync schema for filtered tables
    for table_name in tables_to_sync:
        # Construct file path using naming conventions
        file_path = f"src/rhizome/environments/{env_folder}/expected_data/{db_short_name}_{table_name}.sql"

        _sync_table_schema(env_instance, str(table_name), file_path, change_tracker, errors, verbose)


def sync_schema(env: RhizomeEnvironment | None = None, *, table_names: list[str] | None = None, verbose: bool = False) -> None:
    """Syncs the schema for all environments and reports on changes."""
    typer.echo("Syncing schema...")
    client = RhizomeClient(data_in_logs=True)

    # Initialize change tracker with schema classifier
    change_tracker = ChangeTracker(SchemaChangeClassifier())

    # Track errors
    errors: list[str] = []

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for env_enum, env_class in environments_to_sync:
        _sync_environment_schema(env_enum, env_class, client, change_tracker, errors, table_names, verbose)

    # Debug: Show how many files were tracked
    typer.echo(f"\nTracked {len(change_tracker.tracked_files)} files for change detection")

    # Analyze tracked files and print summary
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary(errors)
