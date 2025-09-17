"""Schema synchronization functionality."""

from typing import Any, cast

import typer

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, SchemaChangeClassifier


def sync_schema(env: RhizomeEnvironment | None = None, *, verbose: bool = False) -> None:
    """Syncs the schema for all environments and reports on changes."""
    typer.echo("Syncing schema...")
    client = RhizomeClient(data_in_logs=True)

    # Initialize change tracker with schema classifier
    change_tracker = ChangeTracker(SchemaChangeClassifier())

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for _env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)
        typer.echo(f"Syncing environment: {env_instance.name}")
        for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
            if model_class:
                typer.echo(f"  Syncing table: {table_name}")
                query_str = f"SHOW CREATE TABLE {table_name}"
                try:
                    result = env_instance.client.execute_raw_query(env_instance.get_connection_string(), query_str)
                    if result and isinstance(result, tuple | list):
                        # Type narrow to sequence with explicit cast
                        result_seq = cast(tuple[Any, ...] | list[Any], result)
                        if len(result_seq) > 1:
                            # The result of SHOW CREATE TABLE is a tuple, the second element is the statement
                            create_table_statement = str(result_seq[1])
                            module_path = emplacement_class.__module__
                            parts = module_path.split(".")
                            env_name = parts[2]
                            db_and_table_name = parts[4]
                            file_path = f"src/rhizome/environments/{env_name}/expected_data/{db_and_table_name}.sql"

                            # Write the file
                            with open(file_path, "w") as f:
                                f.write(create_table_statement)

                            # Track changes to this file
                            change_tracker.track_file(file_path)

                except Exception as e:
                    if verbose:
                        raise
                    typer.secho(f"    Error syncing table {table_name}: {e}", fg=typer.colors.RED)

    # Debug: Show how many files were tracked
    typer.echo(f"\nTracked {len(change_tracker.tracked_files)} files for change detection")

    # Analyze tracked files and print summary
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary()
