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
