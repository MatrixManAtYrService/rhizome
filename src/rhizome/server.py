import asyncio
import json
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import structlog
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rhizome.logging import setup_logging
from rhizome.portforward import start_portforward
from rhizome.proc import NewProcessResponse, ProcessListResponse, process_manager
from rhizome.sleeper import start_sleeper
from trifolium.config import Home


class PortforwardRequest(BaseModel):
    """Request model for port forward requests."""

    kube_context: str
    kube_namespace: str
    kube_deployment: str
    sql_connection: str
    local_port: int = 3306


class SleeperRequest(BaseModel):
    """Request model for sleeper requests."""

    iterations: int = 5


class LocalK8sRequest(BaseModel):
    """Request model for local K8s port forward with credentials."""

    kube_context: str
    kube_namespace: str
    kube_deployment: str
    local_port: int = 3306
    delay: float = 2.0  # Delay before supplying credentials (for testing)


class WriteQueryRequest(BaseModel):
    """Request model for prompted write query execution."""

    query_name: str
    environment_name: str  # e.g., "DevMeta"
    params: dict[str, str | int | float | None]


class WriteQueryResponse(BaseModel):
    """Response model for write query execution."""

    approved: bool
    executed: bool
    rows_affected: int | None = None
    error: str | None = None


logger = structlog.get_logger()

# Global variable to store the home instance for cleanup
_home: Home | None = None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle app startup and shutdown."""
    # Startup
    yield
    # Shutdown
    logger.info("Shutting down server, cleaning up processes")

    # Clean up all processes and tasks
    await process_manager.cleanup()

    # Clean up port file
    if _home is not None:
        port_file = _home.state / "rhizome_port"
        if port_file.exists():
            port_file.unlink()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint for server status."""
    return {"status": "ok"}


@app.post("/sleeper")
async def sleeper(request: SleeperRequest) -> NewProcessResponse:
    """Start a sleeper subprocess for testing rhizome process management."""
    return await start_sleeper(iterations=request.iterations)


@app.post("/portforward")
async def portforward(request: PortforwardRequest) -> NewProcessResponse:
    """Start a kubectl port-forward subprocess for database access."""
    return await start_portforward(
        kube_context=request.kube_context,
        kube_namespace=request.kube_namespace,
        kube_deployment=request.kube_deployment,
        sql_connection=request.sql_connection,
        local_port=request.local_port,
    )


async def localk8s_credentials_generator(request: LocalK8sRequest) -> AsyncGenerator[str, None]:
    """
    Generate SSE stream for local K8s credentials.

    This simulates the credential retrieval process that would normally
    involve vault, auth flows, etc. For testing, it uses hard-coded credentials
    with a configurable delay.
    """
    # First, start the port forward process
    logger.info(f"Starting port forward for {request.kube_deployment}")

    try:
        # Start port forward (but with a fake sql_connection for local k8s)
        port_forward_response = await start_portforward(
            kube_context=request.kube_context,
            kube_namespace=request.kube_namespace,
            kube_deployment=request.kube_deployment,
            sql_connection=f"localk8s:{request.kube_namespace}:{request.kube_deployment}",
            local_port=request.local_port,
        )
        logger.info(f"Port forward started with PID {port_forward_response.pid}")
    except Exception as e:
        logger.error(f"Failed to start port forward: {e}")
        yield f"event: error\ndata: {json.dumps({'error': f'Failed to start port forward: {e}'})}\n\n"
        return

    # Send initial status
    yield f"event: status\ndata: {json.dumps({'status': 'port_forward_started', 'pid': port_forward_response.pid})}\n\n"

    # Give kubectl a moment to establish the port forward
    await asyncio.sleep(1.0)

    # Wait for the specified delay (simulating credential retrieval)
    logger.info(f"Waiting {request.delay}s for credentials...")
    yield f"event: status\ndata: {json.dumps({'status': 'retrieving_credentials', 'delay': request.delay})}\n\n"

    await asyncio.sleep(request.delay)

    # Send credentials (hard-coded for local testing)
    credentials = {
        "username": "user",
        "password": "pass",
        "database": "test",
        "connection_string": f"mysql+pymysql://user:pass@localhost:{request.local_port}/test",
    }

    logger.info("Credentials retrieved, sending to client")
    yield f"event: credentials\ndata: {json.dumps(credentials)}\n\n"


@app.post("/localk8s")
async def localk8s(request: LocalK8sRequest) -> StreamingResponse:
    """Start local K8s port forward and stream credentials via SSE."""
    return StreamingResponse(
        localk8s_credentials_generator(request),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


@app.get("/ps")
def ps() -> ProcessListResponse:
    """List running processes."""
    return process_manager.list_processes()


@app.post("/write_query")
def write_query(request: WriteQueryRequest) -> WriteQueryResponse:
    """
    Execute a canned write query with user approval.

    This endpoint:
    1. Looks up the pre-defined query
    2. Renders it with parameters
    3. Prompts the user for approval (yes/no)
    4. If approved, executes with RW credentials
    5. Returns the result

    Args:
        request: Query name, environment, and parameters

    Returns:
        WriteQueryResponse with execution results
    """
    from urllib.parse import quote_plus

    import sqlalchemy
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm
    from sqlmodel import create_engine

    from rhizome.canned_queries import get_query, render_query
    from rhizome.environments.environment_list import environment_type

    console = Console()

    try:
        # Get the canned query
        query = get_query(request.query_name)

        # Get the environment class
        env_class = environment_type.get(request.environment_name)  # type: ignore[arg-type]
        if not env_class:
            return WriteQueryResponse(
                approved=False,
                executed=False,
                error=f"Unknown environment: {request.environment_name}",
            )

        # Create environment instance (needs a dummy client for now)
        from rhizome.client import RhizomeClient

        env = env_class(RhizomeClient(data_in_logs=False))

        # Get RW database config
        db_config_rw = env.get_database_config_rw()
        if not db_config_rw:
            return WriteQueryResponse(
                approved=False,
                executed=False,
                error=f"Environment {request.environment_name} does not support write operations",
            )

        # Render query for display
        rendered = render_query(request.query_name, request.params)

        # Show query to user with rich formatting
        console.print()
        console.print(
            Panel.fit(
                f"[bold cyan]Query:[/bold cyan] {query.name}\n"
                f"[bold cyan]Description:[/bold cyan] {query.description}\n"
                f"[bold cyan]Environment:[/bold cyan] {request.environment_name}\n"
                f"[bold cyan]Database:[/bold cyan] {db_config_rw.database}\n\n"
                f"[yellow]{rendered}[/yellow]",
                title="[bold red]⚠️  WRITE OPERATION[/bold red]",
                border_style="red",
            )
        )
        console.print()

        # Prompt user
        approved = Confirm.ask("[bold]Execute this query?[/bold]", default=False)

        if not approved:
            console.print("[yellow]Query execution cancelled by user[/yellow]")
            return WriteQueryResponse(approved=False, executed=False)

        # Execute with RW credentials
        console.print("[green]Executing query with RW credentials...[/green]")

        encoded_password = quote_plus(db_config_rw.rw_password)
        connection_string = f"mysql+pymysql://{db_config_rw.rw_username}:{encoded_password}@{db_config_rw.host}:{db_config_rw.port}/{db_config_rw.database}"

        engine = create_engine(connection_string)
        # For raw SQL with parameters, use engine connection directly
        with engine.connect() as connection:
            result = connection.execute(sqlalchemy.text(query.sql), request.params)
            connection.commit()
            rows_affected = result.rowcount

        console.print(f"[green]✓ Query executed successfully. Rows affected: {rows_affected}[/green]")
        console.print()

        return WriteQueryResponse(approved=True, executed=True, rows_affected=rows_affected)

    except Exception as e:
        error_msg = str(e)
        console.print(f"[red]✗ Error: {error_msg}[/red]")
        console.print()
        return WriteQueryResponse(approved=False, executed=False, error=error_msg)


def message() -> str:
    return "rhizome is waiting for connections."


def run(home: Home | None = None) -> None:
    global _home
    _home = home or Home()
    port = _home.get_port()
    if port is None:
        raise ValueError("No port found in home configuration")

    # Set up unified logging before starting uvicorn
    setup_logging()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=port,
        log_config=None,  # Disable uvicorn's default logging config
        access_log=True,  # Keep access logs but they'll go through our handler
    )
