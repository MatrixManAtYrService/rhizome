import typer
from sqlmodel import text

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import RhizomeEnvironment, environment_type


def sync_data(env: RhizomeEnvironment | None = None, *, verbose: bool = False) -> None:
    """Syncs the expected data for all environments."""
    typer.echo("Syncing data...")
    client = RhizomeClient(data_in_logs=True)

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for _env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)
        typer.echo(f"Syncing environment: {env_instance.name}")
        for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
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
                        with open(file_path, "w") as f:
                            f.write(json_data)
                        typer.echo(f"    Wrote data to {file_path}")
                except Exception as e:
                    if verbose:
                        raise
                    typer.secho(
                        f"    Error syncing table {table_name}: {e}", fg=typer.colors.RED
                    )


def sync_schema(env: RhizomeEnvironment | None = None, *, verbose: bool = False) -> None:
    """Syncs the schema for all environments."""
    typer.echo("Syncing schema...")
    client = RhizomeClient(data_in_logs=True)

    environments_to_sync = environment_type.items()
    if env:
        environments_to_sync = [(env, environment_type[env])]

    for _env_enum, env_class in environments_to_sync:
        env_instance = env_class(client)
        typer.echo(f"Syncing environment: {env_instance.name}")
        for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
            if model_class:
                typer.echo(f"  Syncing table: {table_name}")
                query = text(f"SHOW CREATE TABLE {table_name}")
                try:
                    result = env_instance.client.execute_raw_query(
                        env_instance._get_connection_string(), query
                    )
                    if result:
                        # The result of SHOW CREATE TABLE is a tuple, the second element is the statement
                        create_table_statement = result[1]
                        module_path = emplacement_class.__module__
                        parts = module_path.split(".")
                        env_name = parts[2]
                        db_and_table_name = parts[4]
                        file_path = f"src/rhizome/environments/{env_name}/expected_data/{db_and_table_name}.sql"
                        with open(file_path, "w") as f:
                            f.write(create_table_statement)
                        typer.echo(f"    Wrote schema to {file_path}")
                except Exception as e:
                    if verbose:
                        raise
                    typer.secho(
                        f"    Error syncing table {table_name}: {e}", fg=typer.colors.RED
                    )
