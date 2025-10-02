"""Stolon server for managing HTTP API access and authentication."""

import structlog
import uvicorn
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from fastapi import FastAPI
from pydantic import BaseModel

from stolon.get_internal_token import get_internal_token
from rhizome.logging import setup_logging
from trifolium.config import Home


class InternalTokenRequest(BaseModel):
    """Request model for internal token requests."""

    domain: str


class InternalTokenResponse(BaseModel):
    """Response model for internal token responses."""

    token: str
    domain: str


logger = structlog.get_logger()

# Global variable to store the home instance for cleanup
_home: Home | None = None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle app startup and shutdown."""
    # Startup
    yield
    # Shutdown
    logger.info("Shutting down server, cleaning up")

    # Clean up port file
    if _home is not None:
        port_file = _home.state / "stolon_port"
        if port_file.exists():
            port_file.unlink()


app = FastAPI(lifespan=lifespan)


@app.post("/internal_token")
async def internal_token(request: InternalTokenRequest) -> InternalTokenResponse:
    """Get an internal session token via browser authentication."""
    token = get_internal_token(request.domain)
    return InternalTokenResponse(token=token, domain=request.domain)


def message() -> str:
    return "stolon is waiting for connections."


def run(home: Home | None = None) -> None:
    global _home
    _home = home or Home()
    port = _home.get_stolon_port()
    if port is None:
        raise ValueError("No port found in home configuration for stolon")

    # Set up unified logging before starting uvicorn
    setup_logging()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=port,
        log_config=None,  # Disable uvicorn's default logging config
        access_log=True,  # Keep access logs but they'll go through our handler
    )
