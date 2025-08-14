from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import structlog
import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel

from rhizome.config import Home
from rhizome.logging import setup_logging
from rhizome.portforward import start_portforward, start_portforward_legacy
from rhizome.proc import ProcessListResponse, NewProcessResponse, process_manager
from rhizome.sleeper import start_sleeper


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
        port_file = _home.state / "port"
        if port_file.exists():
            port_file.unlink()


app = FastAPI(lifespan=lifespan)


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
        local_port=request.local_port
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
        access_log=True   # Keep access logs but they'll go through our handler
    )
