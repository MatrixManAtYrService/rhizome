import socket
from typing import Annotated

import typer

from rhizome import __version__
from rhizome.environments.environment_list import RhizomeEnvironment
from rhizome.server import run
from rhizome.sync_data import sync_data
from rhizome.sync_report import sync_report
from rhizome.sync_schema import sync_schema
from trifolium.config import Home

app = typer.Typer(help="Database access helper for test tools")
sync_app = typer.Typer(help="Synchronize database schemas, models, and data.")
app.add_typer(sync_app, name="sync")


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        typer.echo(f"rhizome {__version__}")
        raise typer.Exit()


@app.command()
def serve(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit",
        ),
    ] = False,
) -> None:
    """Start the rhizome server for handling database connections."""
    sock = socket.socket()
    sock.bind(("", 0))
    port = sock.getsockname()[1]

    home = Home()
    home.set_port(port)
    run(home)


@sync_app.command()
def data(
    env: Annotated[
        RhizomeEnvironment | None,
        typer.Option(help="The environment to sync. If not provided, all are synced."),
    ] = None,
    table: Annotated[
        list[str] | None,
        typer.Option(help="Specific table(s) to sync. Can be specified multiple times. If not provided, all tables are synced."),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(help="Show full stack trace on error."),
    ] = False,
) -> None:
    """Syncs the expected data for all environments."""
    sync_data(env, table_names=table, verbose=verbose)


@sync_app.command()
def schema(
    env: Annotated[
        RhizomeEnvironment | None,
        typer.Option(help="The environment to sync. If not provided, all are synced."),
    ] = None,
    table: Annotated[
        list[str] | None,
        typer.Option(help="Specific table(s) to sync. Can be specified multiple times. If not provided, all tables are synced."),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(help="Show full stack trace on error."),
    ] = False,
) -> None:
    """Syncs the schema for all environments."""
    sync_schema(env, table_names=table, verbose=verbose)


@sync_app.command()
def report(
    env: Annotated[
        RhizomeEnvironment | None,
        typer.Option(help="The environment to check. If not provided, all are checked."),
    ] = None,
) -> None:
    """Generate a report of sync status for all environment/table pairs."""
    sync_report(env)


def main() -> None:
    app()
