from pathlib import Path
from typing import Any

import typer

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, DataChangeClassifier


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
            return
        typer.echo(f"Found {len(tables_to_sync_map)} tables with missing data.")

    client = RhizomeClient(data_in_logs=True)
    change_tracker = ChangeTracker(DataChangeClassifier())

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for _env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)

        tables_for_this_env: list[tuple[Any, Any, Any]] = []
        for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
            if not model_class:
                continue

            # Filter by missing_only if enabled
            if tables_to_sync_map is not None and (str(_env_enum), str(table_name)) not in tables_to_sync_map:
                continue

            # Filter by table_names if provided
            if table_names and str(table_name).lower() not in [name.lower() for name in table_names]:
                continue

            tables_for_this_env.append((table_name, model_class, emplacement_class))

        if not tables_for_this_env:
            continue

        typer.echo(f"Syncing environment: {env_instance.name}")

        for table_name, model_class, emplacement_class in tables_for_this_env:
            table_name: Any
            model_class: Any
            emplacement_class: Any
            typer.echo(f"  Syncing table: {table_name}")
            query: Any = emplacement_class.expectation_query(model_class)
            try:
                result: Any = env_instance.select_first(query)

                # Infer path from module path of the emplacement class
                module_path: str = emplacement_class.__module__
                parts: list[str] = module_path.split(".")
                env_name: str = parts[2]
                db_and_table_name: str = parts[4]
                json_file_path_str = f"src/rhizome/environments/{env_name}/expected_data/{db_and_table_name}.json"
                json_file_path = Path(json_file_path_str)
                sql_file_path = json_file_path.with_suffix(".sql")

                if result:
                    # Data found in source, write/overwrite the file
                    json_data: str = result.model_dump_json(indent=2)
                    with open(json_file_path, "w") as f:
                        f.write(json_data)
                    typer.echo(f"    Wrote data to {json_file_path_str}")
                    change_tracker.track_file(json_file_path_str)
                else:
                    # No data found in source database
                    if not json_file_path.exists():
                        # And no local dummy/cached data file exists
                        error_msg = (
                            f"Source data for {env_instance.name}/{table_name} is empty and no local data file exists.\n"
                            f"  Suggestion: Generate dummy data in {json_file_path_str} based on the schema in {sql_file_path}.\n"
                            f"  Note: This dummy data will be overwritten by authentic data when it becomes available."
                        )
                        change_tracker.add_error(error_msg)
                        typer.secho(error_msg, fg=typer.colors.YELLOW)

            except Exception as e:
                if verbose:
                    raise
                error_msg = f"Error syncing table {table_name}: {e}"
                change_tracker.add_error(error_msg)
                typer.secho(f"    {error_msg}", fg=typer.colors.RED)

    # Analyze tracked files and print summary
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary()
