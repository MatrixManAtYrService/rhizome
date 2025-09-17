"""Schema synchronization functionality."""

from pathlib import Path
from typing import Any, cast

import typer

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.git_diff import ChangeTracker, SchemaChangeClassifier


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


def sync_schema(env: RhizomeEnvironment | None = None, *, verbose: bool = False) -> None:
    """Syncs the schema for all environments and reports on changes."""
    typer.echo("Syncing schema...")
    client = RhizomeClient(data_in_logs=True)

    # Initialize change tracker with schema classifier
    change_tracker = ChangeTracker(SchemaChangeClassifier())

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)
        typer.echo(f"Syncing environment: {env_instance.name}")

        # Get environment folder name from the enum value
        env_folder = str(env_enum).split("_")[0]  # e.g., "dev_billing_bookkeeper" -> "dev"

        # Get database short name from the environment name
        db_short_name = get_database_short_name(env_instance.name)

        # Get all tables from the environment
        for table_name in env_instance.tables():
            typer.echo(f"  Syncing table: {table_name}")
            query_str = f"SHOW CREATE TABLE {table_name}"

            # Construct file path using naming conventions
            file_path = f"src/rhizome/environments/{env_folder}/expected_data/{db_short_name}_{table_name}.sql"

            try:
                result = env_instance.client.execute_raw_query(env_instance.get_connection_string(), query_str)
                if result and isinstance(result, tuple | list):
                    # Type narrow to sequence with explicit cast
                    result_seq = cast(tuple[Any, ...] | list[Any], result)
                    if len(result_seq) > 1:
                        # The result of SHOW CREATE TABLE is a tuple, the second element is the statement
                        create_table_statement = str(result_seq[1])

                        # Ensure directory exists
                        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

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
