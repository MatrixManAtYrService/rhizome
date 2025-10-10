"Schema synchronization functionality."

from pathlib import Path
from typing import Any, cast

import typer

from rhizome.client import RhizomeClient
from rhizome.environments.base import Environment
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, SchemaChangeClassifier
from rhizome.table_discovery import get_table_list_for_environment


def get_database_short_name(environment_name: str) -> str:
    """Extract database short name from environment name."""
    name = environment_name.replace("NorthAmerica", "").replace("Dev", "").replace("Demo", "")
    result: list[str] = []
    for i, char in enumerate(name):
        if i > 0 and char.isupper():
            result.append("_")
        result.append(char.lower())
    return "".join(result)


def create_lightweight_environment(env_class: type[Environment], client: RhizomeClient) -> Environment:
    """Create a lightweight environment instance that skips expensive table_situation setup."""

    # Try to create a normal instance first
    try:
        return env_class(client)
    except NotImplementedError:
        # If table_situation setup fails due to unimplemented models, create a lightweight version
        # This is needed for schema syncing where we don't need the model/emplacement mappings

        # Create instance without calling __init__
        env_instance = env_class.__new__(env_class)

        # Manually set up the essential attributes for schema syncing
        env_instance.client = client

        # Set up port forwarding if needed
        port_forward_config = env_instance.get_port_forward_config()
        if port_forward_config is not None:
            env_instance.setup_port_forwarding(port_forward_config)

        # Skip table_situation initialization for schema syncing
        env_instance.table_situation = {}

        return env_instance
    except Exception:
        # For other errors, let them propagate
        raise


def _convert_query_result_to_sequence(result: object) -> tuple[Any, ...] | list[Any] | None:
    if not result or not hasattr(result, "__len__"):
        return None
    if len(cast(Any, result)) == 0:
        return None
    try:
        if hasattr(result, "_tuple"):
            return cast(Any, result)._tuple()
        elif isinstance(result, tuple | list):
            return cast(tuple[Any, ...] | list[Any], result)
        else:
            return list(cast(Any, result))
    except Exception:
        return None


def _sync_table_schema(
    env_instance: object,
    table_name: str,
    file_path: str,
    change_tracker: ChangeTracker,
    verbose: bool,
) -> None:
    """Sync schema for a single table."""
    typer.echo(f"  Syncing table: {table_name}")
    query_str = f"SHOW CREATE TABLE {table_name}"

    try:
        result = cast(Any, env_instance).client.execute_raw_query(
            cast(Any, env_instance).get_connection_string(), query_str
        )
        result_seq = _convert_query_result_to_sequence(result)

        if result_seq and len(result_seq) > 1:
            create_table_statement = str(result_seq[1])
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w") as f:
                f.write(create_table_statement)
            change_tracker.track_file(file_path)
            typer.echo(f"    ✓ Tracked file: {file_path}")
        else:
            seq_len = len(result_seq) if result_seq else 0
            error_msg = f"Result sequence too short or conversion failed for {table_name}: {seq_len} items"
            change_tracker.add_error(error_msg)
            typer.echo(f"    ⚠ {error_msg}")

    except Exception as e:
        error_msg = f"Error syncing table {table_name}: {e}"
        change_tracker.add_error(error_msg)
        if verbose:
            raise
        typer.secho(f"    {error_msg}", fg=typer.colors.RED)


def _sync_environment_schema(
    env_enum: RhizomeEnvironment,
    env_class: type,
    client: RhizomeClient,
    change_tracker: ChangeTracker,
    verbose: bool,
    tables_to_sync_map: set[tuple[str, str]] | None,
    table_names: list[str] | None,
) -> None:
    """Sync schema for all tables in an environment."""
    env_instance = create_lightweight_environment(env_class, client)
    typer.echo(f"Syncing environment: {env_instance.name}")

    env_str = str(env_enum)
    env_folder = "na_prod" if env_str.startswith("na_prod_") else env_str.split("_")[0]
    db_short_name = get_database_short_name(env_instance.name)

    table_list = get_table_list_for_environment(env_enum)
    if not table_list:
        typer.echo(f"  Warning: No table enum found for {env_enum}")
        return

    for table_name in table_list:
        # Filter by missing_only if enabled
        if tables_to_sync_map is not None and (str(env_enum), str(table_name)) not in tables_to_sync_map:
            continue

        # Filter by table_names if provided
        if table_names and str(table_name).lower() not in [name.lower() for name in table_names]:
            continue

        file_path = f"src/rhizome/environments/{env_folder}/expected_data/{db_short_name}_{table_name}.sql"
        _sync_table_schema(env_instance, str(table_name), file_path, change_tracker, verbose)


def sync_schema(
    env: RhizomeEnvironment | None = None,
    *,
    table_names: list[str] | None = None,
    verbose: bool = False,
    missing_only: bool = False,
) -> None:
    """Syncs the schema for all environments and reports on changes."""
    typer.echo("Syncing schema...")

    tables_to_sync_map: set[tuple[str, str]] | None = None
    if missing_only:
        from rhizome.sync_report import SyncStatus, collect_sync_statuses

        typer.echo("Checking for missing schemas...")
        all_statuses = collect_sync_statuses(env)
        tables_to_sync_map = {
            (status.environment, status.table) for status in all_statuses if status.status == SyncStatus.MISSING
        }
        if not tables_to_sync_map:
            typer.echo("No missing schemas to sync.")
            return
        typer.echo(f"Found {len(tables_to_sync_map)} tables with missing schemas.")

    client = RhizomeClient(data_in_logs=True)
    change_tracker = ChangeTracker(SchemaChangeClassifier())

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for env_enum, env_class in environments_to_sync:
        _sync_environment_schema(env_enum, env_class, client, change_tracker, verbose, tables_to_sync_map, table_names)

    typer.echo(f"\nTracked {len(change_tracker.tracked_files)} files for change detection")
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary()
