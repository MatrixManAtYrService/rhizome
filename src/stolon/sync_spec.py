"""Sync OpenAPI specifications and generate Python clients."""

import subprocess
from pathlib import Path

import httpx
import structlog
import typer

from stolon.get_internal_token import get_internal_token

logger = structlog.get_logger()


def _fetch_openapi_spec(env: str, service: str, domain: str, spec_url: str) -> dict:
    """Fetch OpenAPI spec from the service, with or without authentication.

    Args:
        env: Environment name
        service: Service name
        domain: Domain to fetch from
        spec_url: Full URL to the OpenAPI spec

    Returns:
        Dictionary containing the OpenAPI spec

    Raises:
        typer.Exit: If fetching fails
    """
    # Try to fetch the OpenAPI spec without authentication first (most specs are public)
    try:
        response = httpx.get(spec_url, follow_redirects=True, timeout=30.0)
        response.raise_for_status()
        spec_data = response.json()
        typer.echo("✅ Fetched spec without authentication")
        return spec_data
    except httpx.HTTPError as e:
        # If that fails, try with authentication
        status: int | str
        status = e.response.status_code if isinstance(e, httpx.HTTPStatusError) else "error"
        typer.echo(f"⚠️  Failed without auth ({status}), trying with authentication...")

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
            return spec_data
        except httpx.HTTPError as e2:
            typer.echo(f"❌ Failed to fetch spec even with authentication: {e2}")
            raise typer.Exit(1) from e2


def _generate_client_from_spec(spec_data: dict, service: str, env: str, output_path: Path, overwrite: bool) -> None:
    """Generate Python client from OpenAPI spec using openapi-python-client.

    Args:
        spec_data: OpenAPI spec dictionary
        service: Service name
        env: Environment name
        output_path: Where to generate the client
        overwrite: Whether to overwrite existing client

    Raises:
        typer.Exit: If generation fails
    """
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
            # Filter out excessive blank lines from openapi-python-client output
            lines = [line for line in result.stdout.split("\n") if line.strip()]
            if lines:
                typer.echo("\n".join(lines))

    except subprocess.CalledProcessError as e:
        typer.echo(f"❌ Failed to generate client: {e}")
        if e.stderr:
            typer.echo(e.stderr)
        raise typer.Exit(1) from e
    except FileNotFoundError as e:
        typer.echo("❌ openapi-python-client not found. Please install it:")
        typer.echo("   pipx install openapi-python-client --include-deps")
        raise typer.Exit(1) from e
    finally:
        # Clean up spec file
        if spec_file.exists():
            spec_file.unlink()


def _generate_proxied_wrappers(service: str, env: str, openapi_path: Path) -> None:
    """Generate proxied wrapper functions for the generated client.

    Args:
        service: Service name
        env: Environment name
        openapi_path: Path to the OpenAPI-generated client
    """
    typer.echo("")
    typer.echo("🔧 Generating proxied wrapper functions...")

    try:
        from stolon.generate_wrappers import generate_wrappers_for_service, write_wrappers

        generated_files = generate_wrappers_for_service(
            service=service,
            env=env,
            generated_client_path=openapi_path,
        )

        if generated_files:
            write_wrappers(generated_files)
            typer.echo(f"✅ Generated {len(generated_files)} wrapper modules")
            typer.echo(f"   Location: src/stolon/generated/{service.replace('-', '_')}_{env}/")
        else:
            typer.echo("⚠️  No API functions found to wrap")

    except Exception as e:
        typer.echo(f"⚠️  Wrapper generation failed: {e}")
        typer.echo("   The OpenAPI client was generated successfully, but wrappers could not be created.")
        if "--verbose" in typer.get_app_dir(""):  # Simple verbose check
            import traceback

            typer.echo(traceback.format_exc())


def sync_spec(env: str, service: str, *, overwrite: bool = False) -> None:
    """
    Fetch OpenAPI spec and generate a Python client.

    Args:
        env: Environment name (e.g., 'dev', 'demo', 'prod')
        service: Service name (e.g., 'billing-bookkeeper', 'agreement')
        overwrite: Whether to overwrite existing generated client
    """
    # Service name aliases - allow shorter names that map to full service names
    service_aliases = {
        "agreement": "agreement-k8s",
    }

    # Resolve alias to actual service name
    actual_service = service_aliases.get(service, service)

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

    domain = custom_domain_map.get((env, actual_service), domain_map[env])
    spec_url = f"https://{domain}/{actual_service}/v3/api-docs"

    typer.echo(f"📡 Fetching OpenAPI spec from {spec_url}")

    # Fetch the spec
    spec_data = _fetch_openapi_spec(env, actual_service, domain, spec_url)

    # Determine output paths
    # OpenAPI-generated client goes to openapi_generated (raw output, don't edit)
    # Our proxied wrappers go to generated (higher-level, editable if needed)
    openapi_output_path = Path("src/stolon/openapi_generated") / f"{actual_service.replace('-', '_')}_{env}"
    Path("src/stolon/generated") / f"{actual_service.replace('-', '_')}_{env}"

    if openapi_output_path.exists() and not overwrite:
        typer.echo(f"⚠️  OpenAPI client already exists at {openapi_output_path}")
        typer.echo("   Use --overwrite to regenerate")
        raise typer.Exit(1)

    # Generate the OpenAPI client
    _generate_client_from_spec(spec_data, actual_service, env, openapi_output_path, overwrite)

    typer.echo("")
    typer.echo(f"✅ OpenAPI client generated at {openapi_output_path}")

    # Generate proxied wrappers
    _generate_proxied_wrappers(actual_service, env, openapi_output_path)

    typer.echo("")
    typer.echo("🎉 Done! You can now:")
    typer.echo(f"   - Use raw OpenAPI client: stolon.openapi_generated.{actual_service.replace('-', '_')}_{env}")
    typer.echo(f"   - Use proxied wrappers: stolon.generated.{actual_service.replace('-', '_')}_{env}")
