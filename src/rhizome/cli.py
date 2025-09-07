import socket
from typing import Annotated

import typer

from rhizome import __version__
from rhizome.config import Home
from rhizome.server import run

app = typer.Typer(help="Database access helper for test tools")


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


@app.command()
def sync(
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
    """Synchronize database schemas and models (placeholder for future functionality)."""
    typer.echo("sync")


def main() -> None:
    app()
