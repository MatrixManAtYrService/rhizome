"""Schema synchronization functionality."""

from enum import StrEnum
from pathlib import Path
from typing import Any, cast

import typer

from rhizome.client import RhizomeClient
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


def _create_lightweight_environment(env_class: type, client: RhizomeClient) -> Any:
    """Create environment instance without initializing table_situation."""
    # We need the environment instance for connection and name info,
    # but we can't use the normal constructor because it tries to build table_situation
    # Instead, we'll manually create the instance and set minimal required attributes

    # Create the instance without calling __init__
    env_instance = env_class.__new__(env_class)

    # Set minimal required attributes
    env_instance.client = client

    # Call the parent __init__ but skip table_situation creation
    # We'll do this by temporarily overriding the abstract methods
    original_tables = env_class.tables
    original_situate_table = env_class.situate_table

    try:
        # Provide dummy implementations that won't be called
        env_class.tables = lambda self: []
        env_class.situate_table = lambda self, table: (None, None)

        # Now we can call __init__ safely
        env_instance.__init__(client)

    finally:
        # Restore original methods
        env_class.tables = original_tables
        env_class.situate_table = original_situate_table

    return env_instance


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
    verbose: bool,
) -> None:
    """Sync schema for all tables in an environment."""
    # Create lightweight environment instance that doesn't require table_situation
    env_instance = _create_lightweight_environment(env_class, client)
    typer.echo(f"Syncing environment: {env_instance.name}")

    # Get environment folder name from the enum value
    env_str = str(env_enum)
    if env_str.startswith("na_prod_"):
        env_folder = "na_prod"
    else:
        env_folder = env_str.split("_")[0]  # e.g., "dev_billing_bookkeeper" -> "dev"

    # Get database short name from the environment name
    db_short_name = get_database_short_name(env_instance.name)

    # Get all tables from the table enum (not from environment.tables())
    table_list = _get_table_enum_for_environment(env_enum)
    if not table_list:
        typer.echo(f"  Warning: No table enum found for {env_enum}")
        return

    # Try to sync schema for all tables in the enum
    for table_name in table_list:
        # Construct file path using naming conventions
        file_path = f"src/rhizome/environments/{env_folder}/expected_data/{db_short_name}_{table_name}.sql"

        _sync_table_schema(env_instance, str(table_name), file_path, change_tracker, errors, verbose)


def sync_schema(env: RhizomeEnvironment | None = None, *, verbose: bool = False) -> None:
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
        _sync_environment_schema(env_enum, env_class, client, change_tracker, errors, verbose)

    # Debug: Show how many files were tracked
    typer.echo(f"\nTracked {len(change_tracker.tracked_files)} files for change detection")

    # Analyze tracked files and print summary
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary(errors)
