from typing import Annotated

import typer

from stolon import __version__
from stolon.get_internal_token import get_internal_token
from trifolium.config import Home

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
def serve(
    port: Annotated[int, typer.Option(help="Port to run the server on")] = 8001,
) -> None:
    """Start the stolon server for managing HTTP API access."""
    import socket

    from stolon import server

    # Check if port is available
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex(("127.0.0.1", port)) == 0:
            typer.echo(f"❌ Port {port} is already in use")
            raise typer.Exit(1)

    # Store the port in the home directory
    home = Home()
    home.set_stolon_port(port)

    typer.echo(f"🚀 Starting stolon server on port {port}")
    typer.echo(server.message())

    try:
        server.run(home)
    except KeyboardInterrupt:
        typer.echo("\n👋 Shutting down stolon server")


@app.command()
def hello() -> None:
    """A dummy command to satisfy typer's multi-command requirement."""
    typer.echo("Hello from stolon! 👋")


def main() -> None:
    app()
