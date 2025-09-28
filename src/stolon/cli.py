from typing import Annotated

import typer

from stolon import __version__
from stolon.get_internal_token import get_internal_token

app = typer.Typer(help="HTTP API access helper for Clover services")


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        typer.echo(f"stolon {__version__}")
        raise typer.Exit()


@app.command()
def internal_token(
    domain: Annotated[str, typer.Argument(help="Clover domain to authenticate with (e.g., dev1.dev.clover.com)")],
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
    """Get an internal session token via browser authentication."""
    get_internal_token(domain)


@app.command()
def hello() -> None:
    """A dummy command to satisfy typer's multi-command requirement."""
    typer.echo("Hello from stolon! 👋")


def main() -> None:
    app()
