import socket
from typing import Annotated

import typer

from rhizome import __version__
from rhizome.config import Home
from rhizome.server import run

app = typer.Typer(help="Auth handler for clover db connections")



def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        typer.echo(f"rhizome {__version__}")
        raise typer.Exit()


@app.command()
def start(
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

    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]

    home = Home()
    home.set_port(port)
    run(home)


def main() -> None:
    app()
