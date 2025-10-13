"""Internal token extraction logic for Stolon."""

import webbrowser

import httpx
import typer

from stolon.auth_interceptor import AuthServer, start_auth_server
from trifolium.config import Home, InternalTokenPreference


def _try_get_token_from_server(home: Home, domain: str) -> str | None:
    """Try to get token from running stolon server.

    Args:
        home: Home configuration
        domain: Clover domain to authenticate with

    Returns:
        Token if successful, None if server not available
    """
    stolon_port = home.get_stolon_port()
    if stolon_port is None:
        return None

    try:
        base_url = f"http://0.0.0.0:{stolon_port}"
        with httpx.Client() as client:
            # First try to get cached token
            try:
                response = client.get(f"{base_url}/internal_token/{domain}", timeout=5.0)
                response.raise_for_status()
                token = response.json()["token"]
                typer.echo(f"✅ Retrieved cached token from stolon server (port {stolon_port})")
                return token
            except httpx.HTTPStatusError as e:
                if e.response.status_code != 404:
                    raise
                # Token not cached, need to authenticate via the server
                typer.echo(f"ℹ️  No cached token for {domain}, authenticating via stolon server...")

            # Token not cached, use POST /internal_token to authenticate
            response = client.post(
                f"{base_url}/internal_token",
                json={"domain": domain},
                timeout=120.0,  # Authentication might take a while
            )
            response.raise_for_status()
            token = response.json()["token"]
            typer.echo("✅ Authentication successful via stolon server")
            return token
    except (httpx.HTTPError, KeyError) as e:
        typer.echo(f"⚠️  Could not use stolon server on port {stolon_port}: {e}")
        typer.echo("   Falling back to standalone authentication...")
        return None


def _handle_first_time_setup(home: Home) -> None:
    """Handle first-time setup for token capture preference.

    Args:
        home: Home configuration
    """
    typer.echo("🤖 First-time setup: How would you like to handle internal token capture in the future?")
    typer.echo("")
    typer.echo("Options:")
    typer.echo("  1. auto    - Automatically capture tokens without asking")
    typer.echo("  2. prompt  - Always ask for confirmation before capturing tokens")
    typer.echo("")

    choice = typer.prompt("Enter your preference (auto/prompt)", default="auto")

    config = home.load_config()
    if choice.lower() in ["auto", "a", "1"]:
        config.internal_token_preference = InternalTokenPreference.AUTO
        typer.echo("✅ Set to automatically capture tokens in the future")
    else:
        config.internal_token_preference = InternalTokenPreference.PROMPT
        typer.echo("✅ Will prompt for confirmation each time")

    home.save_config(config)
    typer.echo("")


def _prompt_for_confirmation() -> None:
    """Prompt user for confirmation to capture token.

    Raises:
        typer.Exit: If user declines
    """
    typer.echo("🔐 Ready to capture internal token for authentication")
    proceed = typer.confirm("Continue with automatic token capture?", default=True)
    if not proceed:
        typer.echo("❌ Token capture cancelled by user")
        raise typer.Exit(1)
    typer.echo("")


def _wait_for_token_capture(server: AuthServer, port: int) -> str:
    """Wait for token to be captured by the auth server.

    Args:
        server: Auth server instance
        port: Server port number

    Returns:
        The captured token

    Raises:
        typer.Exit: If authentication fails or is cancelled
    """
    import time

    typer.echo("⏳ Waiting for authentication...")
    typer.echo("")
    typer.echo("📦 Browser Extension Required:")
    typer.echo("   For automatic token capture, install the Clover Session Extension:")
    typer.echo("   • Repository: github.corp.clover.com:clover/clover-session-extension")
    typer.echo("   • Branch: trifolium-integration")
    typer.echo("   • Works identically to main branch, plus adds CLI token capture support")
    typer.echo("")
    typer.echo("📋 Steps:")
    typer.echo("   1. Log in to Clover admin in the opened browser tab")
    typer.echo("   2. Extension will automatically detect and send token")
    typer.echo("   3. Tab closes automatically after successful transfer")
    typer.echo("")
    typer.echo(f"🔧 Manual fallback: Visit http://localhost:{port} if extension not installed")

    try:
        while server.captured_token is None:
            time.sleep(0.5)
    except KeyboardInterrupt:
        typer.echo("\n❌ Authentication cancelled by user")
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"❌ Error during authentication: {e}")
        raise typer.Exit(1) from e

    token = server.captured_token
    typer.echo("✅ Authentication successful!")
    typer.echo(f"🎫 Token: {token}")
    return token


def get_internal_token(domain: str, *, _skip_server_check: bool = False) -> str:
    """
    Get an internal session token via browser authentication.

    This function handles the complete flow:
    1. Load user preferences for token capture
    2. Prompt for first-time setup or confirmation if needed
    3. Start authentication server and open browser
    4. Wait for token capture via browser extension or manual entry
    5. Return the captured token

    Args:
        domain: Clover domain to authenticate with (e.g., dev1.dev.clover.com)
        _skip_server_check: Internal flag to prevent recursion when called from server

    Returns:
        The captured internal session token

    Raises:
        typer.Exit: If user cancels or authentication fails
    """
    home = Home()

    # First, check if there's a stolon server already running (unless disabled)
    if not _skip_server_check:
        token = _try_get_token_from_server(home, domain)
        if token is not None:
            return token

    config_file = home.config / "trifolium.json"

    # If this is the first time the user has run the command, ask for their preference.
    if not config_file.exists():
        _handle_first_time_setup(home)

    # Load user preferences
    config = home.load_config()

    # If user has selected prompt preference, ask for confirmation each time
    if config.internal_token_preference == InternalTokenPreference.PROMPT:
        _prompt_for_confirmation()

    # Start local HTTP server with improved UI
    server, port = start_auth_server(domain)

    typer.echo(f"🌐 Starting authentication server on http://localhost:{port}")
    typer.echo(f"🔐 Opening browser for authentication with {domain}")

    # Open browser directly to Clover admin page for extension integration
    clover_admin_url = f"https://{domain}/admin"
    webbrowser.open(clover_admin_url)

    # Wait for token capture
    return _wait_for_token_capture(server, port)
