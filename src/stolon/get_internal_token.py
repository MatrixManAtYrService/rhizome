"""Internal token extraction logic for Stolon."""

import webbrowser

import typer

from stolon.auth_interceptor import start_auth_server
from trifolium.config import Home, InternalTokenPreference


def get_internal_token(domain: str) -> str:
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

    Returns:
        The captured internal session token

    Raises:
        typer.Exit: If user cancels or authentication fails
    """
    home = Home()
    config_file = home.config / "trifolium.json"

    # If this is the first time the user has run the command, ask for their preference.
    if not config_file.exists():
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

    # Load user preferences
    config = home.load_config()

    # If user has selected prompt preference, ask for confirmation each time
    if config.internal_token_preference == InternalTokenPreference.PROMPT:
        typer.echo("🔐 Ready to capture internal token for authentication")
        proceed = typer.confirm("Continue with automatic token capture?", default=True)
        if not proceed:
            typer.echo("❌ Token capture cancelled by user")
            raise typer.Exit(1)
        typer.echo("")

    # Start local HTTP server with improved UI
    server, port = start_auth_server(domain)

    typer.echo(f"🌐 Starting authentication server on http://localhost:{port}")
    typer.echo(f"🔐 Opening browser for authentication with {domain}")

    # Open browser directly to Clover admin page for extension integration
    clover_admin_url = f"https://{domain}/admin"
    webbrowser.open(clover_admin_url)

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

    # Wait until we get a token (server runs in background thread)
    import time

    try:
        while server.captured_token is None:
            time.sleep(0.5)
    except KeyboardInterrupt:
        typer.echo("\n❌ Authentication cancelled by user")
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"❌ Error during authentication: {e}")
        raise typer.Exit(1) from e

    # Got the token!
    token = server.captured_token

    typer.echo("✅ Authentication successful!")
    typer.echo(f"🎫 Token: {token}")

    return token
