from enum import StrEnum
from pathlib import Path
from typing import TYPE_CHECKING

import typer

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, DataChangeClassifier

if TYPE_CHECKING:
    from rhizome.environments.base import Environment
    from rhizome.models.base import Emplacement, RhizomeModel


def _get_data_file_paths(emplacement_class: type["Emplacement[RhizomeModel]"]) -> tuple[Path, Path, str]:
    """Extract file paths from emplacement class module path."""
    module_path: str = emplacement_class.__module__
    parts: list[str] = module_path.split(".")
    env_name: str = parts[2]
    db_and_table_name: str = parts[4]
    json_file_path_str = f"src/rhizome/environments/{env_name}/expected_data/{db_and_table_name}.json"
    json_file_path = Path(json_file_path_str)
    sql_file_path = json_file_path.with_suffix(".sql")
    return json_file_path, sql_file_path, json_file_path_str


def _write_data_file(
    result: "RhizomeModel", json_file_path: Path, json_file_path_str: str, change_tracker: ChangeTracker
) -> None:
    """Write query result data to JSON file."""
    json_data: str = result.model_dump_json(indent=2)
    with open(json_file_path, "w") as f:
        f.write(json_data)
    typer.echo(f"    Wrote data to {json_file_path_str}")
    change_tracker.track_file(json_file_path_str)


def _handle_missing_data(
    env_name: str,
    table_name: StrEnum,
    json_file_path: Path,
    sql_file_path: Path,
    json_file_path_str: str,
    change_tracker: ChangeTracker,
) -> None:
    """Handle case where no data is found in source database."""
    if not json_file_path.exists():
        error_msg = (
            f"Source data for {env_name}/{table_name} is empty "
            f"and no local data file exists.\n"
            f"  Suggestion: Generate dummy data in {json_file_path_str} "
            f"based on the schema in {sql_file_path}.\n"
            f"  Note: This dummy data will be overwritten by authentic data "
            f"when it becomes available."
        )
        change_tracker.add_error(error_msg)
        typer.secho(error_msg, fg=typer.colors.YELLOW)


def _sync_single_table(
    table_name: StrEnum,
    model_class: type["RhizomeModel"],
    emplacement_class: type["Emplacement[RhizomeModel]"],
    env_instance: "Environment",
    change_tracker: ChangeTracker,
    verbose: bool,
) -> None:
    """Sync data for a single table."""
    typer.echo(f"  Syncing table: {table_name}")
    query = emplacement_class.expectation_query(model_class)

    try:
        result = env_instance.select_first(query)
        json_file_path, sql_file_path, json_file_path_str = _get_data_file_paths(emplacement_class)

        if result:
            _write_data_file(result, json_file_path, json_file_path_str, change_tracker)
        else:
            _handle_missing_data(
                env_instance.name, table_name, json_file_path, sql_file_path, json_file_path_str, change_tracker
            )

    except Exception as e:
        if verbose:
            raise
        error_msg = f"Error syncing table {table_name}: {e}"
        change_tracker.add_error(error_msg)
        typer.secho(f"    {error_msg}", fg=typer.colors.RED)


def _get_missing_tables_filter(env: RhizomeEnvironment | None) -> set[tuple[str, str]] | None:
    """Get set of tables that need syncing based on missing data analysis."""
    from rhizome.sync_report import SyncStatus, collect_sync_statuses

    typer.echo("Checking for missing data...")
    all_statuses = collect_sync_statuses(env)
    tables_to_sync_map = {
        (status.environment, status.table)
        for status in all_statuses
        if status.status == SyncStatus.SCHEMA_MODEL_EMPLACEMENT
    }
    if not tables_to_sync_map:
        typer.echo("No missing data to sync.")
        return None
    typer.echo(f"Found {len(tables_to_sync_map)} tables with missing data.")
    return tables_to_sync_map


def _filter_tables_for_environment(
    env_instance: "Environment",
    env_enum: RhizomeEnvironment,
    tables_to_sync_map: set[tuple[str, str]] | None,
    table_names: list[str] | None,
) -> list[tuple[StrEnum, type["RhizomeModel"], type["Emplacement[RhizomeModel]"]]]:
    """Filter tables for a specific environment based on sync criteria."""
    tables_for_this_env: list[tuple[StrEnum, type[RhizomeModel], type[Emplacement[RhizomeModel]]]] = []

    for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
        if not model_class or not emplacement_class:
            continue

        # Filter by missing_only if enabled
        if tables_to_sync_map is not None and (str(env_enum), str(table_name)) not in tables_to_sync_map:
            continue

        # Filter by table_names if provided
        if table_names and str(table_name).lower() not in [name.lower() for name in table_names]:
            continue

        tables_for_this_env.append((table_name, model_class, emplacement_class))

    return tables_for_this_env


def _sync_environment_tables(
    env_instance: "Environment",
    tables_for_env: list[tuple[StrEnum, type["RhizomeModel"], type["Emplacement[RhizomeModel]"]]],
    change_tracker: ChangeTracker,
    verbose: bool,
) -> None:
    """Sync all tables for a specific environment."""
    typer.echo(f"Syncing environment: {env_instance.name}")

    for table_name, model_class, emplacement_class in tables_for_env:
        _sync_single_table(table_name, model_class, emplacement_class, env_instance, change_tracker, verbose)


def sync_data(
    env: RhizomeEnvironment | None = None,
    *,
    table_names: list[str] | None = None,
    verbose: bool = False,
    missing_only: bool = False,
) -> None:
    """Syncs the expected data for all environments and reports on changes."""
    typer.echo("Syncing data...")

    tables_to_sync_map: set[tuple[str, str]] | None = None
    if missing_only:
        tables_to_sync_map = _get_missing_tables_filter(env)
        if tables_to_sync_map is None:
            return

    client = RhizomeClient(data_in_logs=True)
    change_tracker = ChangeTracker(DataChangeClassifier())

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)

        tables_for_this_env = _filter_tables_for_environment(
            env_instance, env_enum, tables_to_sync_map, table_names
        )

        if tables_for_this_env:
            _sync_environment_tables(env_instance, tables_for_this_env, change_tracker, verbose)

    # Analyze tracked files and print summary
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary()
