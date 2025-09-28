import typer

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, DataChangeClassifier


def sync_data(env: RhizomeEnvironment | None = None, *, table_names: list[str] | None = None, verbose: bool = False) -> None:
    """Syncs the expected data for all environments and reports on changes."""
    typer.echo("Syncing data...")
    client = RhizomeClient(data_in_logs=True)

    # Initialize change tracker with data classifier
    change_tracker = ChangeTracker(DataChangeClassifier())

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for _env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)
        typer.echo(f"Syncing environment: {env_instance.name}")

        # Filter tables if specific table names were provided
        tables_to_sync = env_instance.table_situation.items()
        if table_names:
            # Convert table_names to lowercase for case-insensitive matching
            target_table_names = [name.lower() for name in table_names]
            tables_to_sync = [
                (table_name, (model_class, emplacement_class))
                for table_name, (model_class, emplacement_class) in env_instance.table_situation.items()
                if str(table_name).lower() in target_table_names
            ]

            # Warn if some specified tables weren't found in this environment
            found_table_names = [str(table_name).lower() for table_name, _ in tables_to_sync]
            missing_tables = [name for name in target_table_names if name not in found_table_names]
            if missing_tables:
                typer.echo(f"  Warning: Tables not found in {env_instance.name}: {', '.join(missing_tables)}")

        for table_name, (model_class, emplacement_class) in tables_to_sync:
            if model_class:
                typer.echo(f"  Syncing table: {table_name}")
                query = emplacement_class.expectation_query(model_class)
                try:
                    result = env_instance.select_first(query)
                    if result:
                        json_data = result.model_dump_json(indent=2)
                        # Infer path from module path of the emplacement class
                        module_path = emplacement_class.__module__
                        # e.g. rhizome.environments.dev.expected_data.billing_bookkeeper_fee_summary
                        parts = module_path.split(".")
                        env_name = parts[2]
                        db_and_table_name = parts[4]
                        file_path = f"src/rhizome/environments/{env_name}/expected_data/{db_and_table_name}.json"

                        # Write the file
                        with open(file_path, "w") as f:
                            f.write(json_data)
                        typer.echo(f"    Wrote data to {file_path}")

                        # Track changes to this file
                        change_tracker.track_file(file_path)

                except Exception as e:
                    if verbose:
                        raise
                    typer.secho(f"    Error syncing table {table_name}: {e}", fg=typer.colors.RED)

    # Analyze tracked files and print summary
    change_tracker.analyze_tracked_files()
    change_tracker.print_summary()
