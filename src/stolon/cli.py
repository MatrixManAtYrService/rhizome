import webbrowser
from typing import Annotated

import typer

from stolon import __version__
from stolon.auth_interceptor import start_auth_server

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

    # Start local HTTP server with improved UI
    server, port = start_auth_server(domain)

    typer.echo(f"🌐 Starting authentication server on http://localhost:{port}")
    typer.echo(f"🔐 Opening browser for authentication with {domain}")

    # Open browser directly to Clover admin page for extension integration
    clover_admin_url = f"https://{domain}/admin"
    webbrowser.open(clover_admin_url)

    typer.echo("⏳ Waiting for authentication...")
    typer.echo("   1. Log in to Clover admin in the opened browser tab")
    typer.echo("   2. Browser extension will offer to send token automatically")
    typer.echo("   3. Click 'Send Token' when prompted by the extension")
    typer.echo(f"   4. Or visit http://localhost:{port} for manual entry")

    # Handle requests until we get a token
    while server.captured_token is None:
        try:
            server.handle_request()
        except KeyboardInterrupt:
            typer.echo("\n❌ Authentication cancelled by user")
            server.server_close()
            raise typer.Exit(1)
        except Exception as e:
            typer.echo(f"❌ Error during authentication: {e}")
            server.server_close()
            raise typer.Exit(1)

    # Got the token!
    token = server.captured_token
    server.server_close()

    typer.echo("✅ Authentication successful!")
    typer.echo(f"🎫 Token: {token}")


@app.command()
def hello() -> None:
    """A dummy command to satisfy typer's multi-command requirement."""
    typer.echo("Hello from stolon! 👋")


def main() -> None:
    app()