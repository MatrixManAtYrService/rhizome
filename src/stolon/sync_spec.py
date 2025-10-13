"""Sync OpenAPI specifications and generate Python clients."""

import subprocess
from pathlib import Path

import httpx
import structlog
import typer

from stolon.get_internal_token import get_internal_token

logger = structlog.get_logger()


def sync_spec(env: str, service: str, *, overwrite: bool = False) -> None:
    """
    Fetch OpenAPI spec and generate a Python client.

    Args:
        env: Environment name (e.g., 'dev', 'demo', 'prod')
        service: Service name (e.g., 'billing-bookkeeper')
        overwrite: Whether to overwrite existing generated client
    """
    # Map environment to domain
    domain_map = {
        "dev": "dev1.dev.clover.com",
        "demo": "demo.clover.com",
        "prod": "www.clover.com",
    }

    if env not in domain_map:
        typer.echo(f"❌ Unknown environment: {env}. Valid options: {', '.join(domain_map.keys())}")
        raise typer.Exit(1)

    # Some services use different subdomains
    # Map: (env, service) -> custom domain
    custom_domain_map = {
        ("dev", "agreement-k8s"): "apidev1.dev.clover.com",
    }

    domain = custom_domain_map.get((env, service), domain_map[env])
    spec_url = f"https://{domain}/{service}/v3/api-docs"

    typer.echo(f"📡 Fetching OpenAPI spec from {spec_url}")

    # Try to fetch the OpenAPI spec without authentication first (most specs are public)
    try:
        response = httpx.get(spec_url, follow_redirects=True, timeout=30.0)
        response.raise_for_status()
        spec_data = response.json()
        typer.echo("✅ Fetched spec without authentication")
    except httpx.HTTPError as e:
        # If that fails, try with authentication
        typer.echo(f"⚠️  Failed without auth ({e.response.status_code if hasattr(e, 'response') else 'error'}), trying with authentication...")

        # Get authentication token
        typer.echo("🔐 Getting authentication token...")
        token = get_internal_token(domain)

        # Fetch the OpenAPI spec with authentication
        try:
            headers = {
                "Cookie": f"internalSession={token}",
                "Content-Type": "application/json",
                "X-Clover-Appenv": f"{env}:{domain.split('.')[0]}",
            }
            response = httpx.get(spec_url, headers=headers, follow_redirects=True, timeout=30.0)
            response.raise_for_status()
            spec_data = response.json()
            typer.echo("✅ Fetched spec with authentication")
        except httpx.HTTPError as e2:
            typer.echo(f"❌ Failed to fetch spec even with authentication: {e2}")
            raise typer.Exit(1) from e2

    # Determine output path
    # Store generated clients in src/stolon/generated/{service}_{env}
    output_path = Path("src/stolon/generated") / f"{service.replace('-', '_')}_{env}"

    if output_path.exists() and not overwrite:
        typer.echo(f"⚠️  Client already exists at {output_path}")
        typer.echo("   Use --overwrite to regenerate")
        raise typer.Exit(1)

    # Save spec to temporary file for openapi-python-client
    spec_file = output_path.parent / f"{service}_{env}_spec.json"
    spec_file.parent.mkdir(parents=True, exist_ok=True)

    import json

    spec_file.write_text(json.dumps(spec_data, indent=2))

    typer.echo(f"💾 Saved spec to {spec_file}")
    typer.echo(f"🔨 Generating Python client at {output_path}")

    # Generate client using openapi-python-client with custom templates
    # Custom templates fix nullable date/datetime fields bug:
    # https://github.com/openapi-generators/openapi-python-client/issues/997
    custom_template_path = Path(__file__).parent / "custom_templates"

    try:
        cmd = [
            "openapi-python-client",
            "generate",
            "--path",
            str(spec_file),
            "--output-path",
            str(output_path),
            "--custom-template-path",
            str(custom_template_path),
        ]

        if overwrite:
            cmd.append("--overwrite")

        result = subprocess.run(cmd, check=True, capture_output=True, text=True)

        typer.echo(f"✅ Client generated successfully at {output_path}")

        if result.stdout:
            typer.echo(result.stdout)

    except subprocess.CalledProcessError as e:
        typer.echo(f"❌ Failed to generate client: {e}")
        if e.stderr:
            typer.echo(e.stderr)
        raise typer.Exit(1) from e
    except FileNotFoundError as e:
        typer.echo("❌ openapi-python-client not found. Please install it:")
        typer.echo("   pipx install openapi-python-client --include-deps")
        raise typer.Exit(1) from e

    # Clean up spec file
    spec_file.unlink()

    typer.echo("")
    typer.echo(f"🎉 Done! You can now import the client from stolon.generated.{service.replace('-', '_')}_{env}")
