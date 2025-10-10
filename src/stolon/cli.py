from typing import Annotated

import typer

from stolon import __version__
from stolon.get_internal_token import get_internal_token
from trifolium.config import Home

app = typer.Typer(help="HTTP API access helper for Clover services")
sync_app = typer.Typer(help="Synchronize API specifications and generate clients.")
app.add_typer(sync_app, name="sync")


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


@app.command()
def clear_cache(
    domain: Annotated[
        str | None,
        typer.Argument(
            help=(
                "Clover domain to clear cache for (e.g., dev1.dev.clover.com). "
                "If not provided, clears all cached tokens."
            )
        ),
    ] = None,
) -> None:
    """Clear cached authentication tokens."""
    import httpx

    home = Home()
    port = home.get_stolon_port()

    if port is None:
        typer.echo("❌ Stolon server is not running. Start it with 'stolon serve'")
        raise typer.Exit(1)

    base_url = f"http://0.0.0.0:{port}"

    if domain:
        # Clear specific domain
        try:
            with httpx.Client() as client:
                response = client.delete(f"{base_url}/internal_token/{domain}")
                response.raise_for_status()
                typer.echo(f"✅ Cleared cached token for {domain}")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                typer.echo(f"ℹ️  No cached token found for {domain}")
            else:
                typer.echo(f"❌ Error clearing cache: {e}")
                raise typer.Exit(1) from e
    else:
        # For now, we don't have an endpoint to clear all tokens
        # This would require adding a DELETE /internal_token endpoint
        typer.echo("❌ Clearing all cached tokens is not yet implemented.")
        typer.echo("   Please specify a domain to clear: stolon clear-cache <domain>")
        raise typer.Exit(1)


@sync_app.command()
def spec(
    env: Annotated[str, typer.Option(help="Environment to sync (e.g., 'dev', 'demo', 'prod')")],
    service: Annotated[str, typer.Option(help="Service to sync (e.g., 'billing-bookkeeper')")],
    overwrite: Annotated[bool, typer.Option(help="Overwrite existing generated client")] = False,
) -> None:
    """Generate a Python client from an OpenAPI specification."""
    from stolon.sync_spec import sync_spec

    sync_spec(env=env, service=service, overwrite=overwrite)


def main() -> None:
    app()
