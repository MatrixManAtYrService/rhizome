"""Stolon server for managing HTTP API access and authentication."""

import asyncio
from collections.abc import AsyncGenerator
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
from functools import partial
from typing import Any

import httpx
import structlog
import uvicorn
from fastapi import FastAPI, HTTPException

from rhizome.logging import setup_logging
from stolon.get_internal_token import get_internal_token
from stolon.models import (
    HttpRequestLog,
    HttpResponseLog,
    InternalTokenRequest,
    InternalTokenResponse,
    ProxyRequest,
    ProxyResponse,
)
from trifolium.config import Home

logger = structlog.get_logger()

# Global variable to store the home instance for cleanup
_home: Home | None = None

# Token cache: domain -> token mapping
_token_cache: dict[str, str] = {}


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


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint for server status."""
    return {"status": "ok"}


@app.post("/internal_token")
async def internal_token(request: InternalTokenRequest) -> InternalTokenResponse:
    """
    Get an internal session token via browser authentication.

    Checks cache first. If token exists in cache, returns it immediately.
    Otherwise, initiates browser authentication flow and caches the result.
    """
    # Check if we already have a cached token for this domain
    if request.domain in _token_cache:
        logger.info(f"Using cached token for {request.domain}")
        return InternalTokenResponse(token=_token_cache[request.domain], domain=request.domain, cached=True)

    # No cached token, get a new one
    logger.info(f"No cached token for {request.domain}, initiating authentication")
    # Use _skip_server_check=True to prevent recursion (server shouldn't call itself)
    # Run in thread pool to avoid blocking event loop and allow signal handling
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        token = await loop.run_in_executor(
            executor, partial(get_internal_token, request.domain, _skip_server_check=True)
        )

    # Cache the token for future requests
    _token_cache[request.domain] = token
    logger.info(f"Cached new token for {request.domain}")

    return InternalTokenResponse(token=token, domain=request.domain, cached=False)


@app.get("/internal_token/{domain}")
async def get_cached_token(domain: str) -> InternalTokenResponse:
    """
    Get a cached token for a specific domain.

    Returns:
        The cached token if it exists

    Raises:
        HTTPException: 404 if no token is cached for this domain
    """
    if domain not in _token_cache:
        raise HTTPException(status_code=404, detail=f"No cached token for domain: {domain}")

    return InternalTokenResponse(token=_token_cache[domain], domain=domain, cached=True)


@app.delete("/internal_token/{domain}")
async def delete_cached_token(domain: str) -> dict[str, str]:
    """
    Delete a cached token for a specific domain.

    This forces re-authentication on the next request.

    Returns:
        Success message

    Raises:
        HTTPException: 404 if no token is cached for this domain
    """
    if domain not in _token_cache:
        raise HTTPException(status_code=404, detail=f"No cached token for domain: {domain}")

    del _token_cache[domain]
    logger.info(f"Deleted cached token for {domain}")

    return {"message": f"Cached token for {domain} deleted successfully"}


async def _make_http_request(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    headers: dict[str, str],
    request: ProxyRequest,
) -> httpx.Response:
    """Helper to make HTTP request with appropriate body type."""
    if request.json_body is not None:
        return await client.request(
            method=method,
            url=url,
            headers=headers,
            json=request.json_body,
            params=request.params,
            timeout=request.timeout or 30.0,
        )
    if request.content is not None:
        return await client.request(
            method=method,
            url=url,
            headers=headers,
            content=request.content,
            params=request.params,
            timeout=request.timeout or 30.0,
        )
    return await client.request(
        method=method,
        url=url,
        headers=headers,
        params=request.params,
        timeout=request.timeout or 30.0,
    )


def _prepare_proxy_log_data(request: ProxyRequest, full_url: str, status_code: int) -> dict[str, Any]:
    """Helper to prepare log data for proxied requests."""
    from typing import Any as TypingAny
    from urllib.parse import urlparse

    # Parse URL to extract hostname and path
    parsed = urlparse(full_url)
    hostname = parsed.netloc
    path = parsed.path or "/"

    # Prepare log data
    log_data: dict[str, TypingAny] = {
        "method": request.method,
        "hostname": hostname,
        "path": path,
        "url": full_url,
        "status_code": status_code,
    }

    # Handle request body - show up to 1028 chars with length indicator if longer
    body_str: str | None = None
    if request.json_body is not None:
        import json as json_module

        body_str = json_module.dumps(request.json_body, ensure_ascii=False)
    elif request.content is not None:
        body_str = request.content

    if body_str is not None:
        if len(body_str) <= 1028:
            log_data["data"] = body_str
        else:
            log_data["data"] = body_str[:1028] + "..."
            log_data["data_length"] = f"{len(body_str)} characters (showing first 1028)"

    return log_data


@app.post("/proxy")
async def proxy_request(request: ProxyRequest) -> ProxyResponse:
    """
    Proxy an HTTP request through the stolon server.

    This endpoint:
    1. Receives request intent from client (method, path, body, params)
    2. Retrieves/refreshes authentication token
    3. Makes the actual HTTP call to target domain
    4. Returns response to client

    Benefits:
    - Server handles all auth token management
    - Logging happens automatically server-side
    """
    domain = request.domain
    method = request.method
    path = request.path

    # Get or refresh token (uses existing cache)
    token_response = await internal_token(InternalTokenRequest(domain=domain))
    token = token_response.token

    # Build full URL
    full_url = f"https://{domain}{path}"

    # Make the actual HTTP call
    headers = {
        "Cookie": f"internalSession={token}",
        "X-Clover-Appenv": f"{request.environment_name}:{domain.split('.')[0]}",
    }

    # Set Content-Type based on what's provided
    if request.json_body is not None:
        headers["Content-Type"] = "application/json"
    elif request.content_type is not None:
        headers["Content-Type"] = request.content_type
    else:
        headers["Content-Type"] = "application/json"  # Default

    async with httpx.AsyncClient() as client:
        # Make initial request
        response = await _make_http_request(client, method, full_url, headers, request)

        # Handle 401 - token expired, refresh and retry
        if response.status_code == 401:
            logger.warning(f"Received 401 for {domain}, refreshing token and retrying")
            # Invalidate cached token
            if domain in _token_cache:
                del _token_cache[domain]
            # Get fresh token
            token_response = await internal_token(InternalTokenRequest(domain=domain))
            token = token_response.token
            headers["Cookie"] = f"internalSession={token}"

            # Retry request
            response = await _make_http_request(client, method, full_url, headers, request)

        # Log request/response automatically
        log_data = _prepare_proxy_log_data(request, full_url, response.status_code)
        logger.info("Proxied HTTP request", **log_data)

        # Return response to client
        return ProxyResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            body=response.text,
        )


@app.post("/log_request")
async def log_request(request: HttpRequestLog) -> dict[str, str]:
    """
    Log HTTP request details.

    Logs method, hostname, path, and data (truncated if too long).
    Headers are not logged for security.
    """
    from typing import Any
    from urllib.parse import urlparse

    # Parse URL to extract hostname and path
    parsed = urlparse(request.url)
    hostname = parsed.netloc
    path = parsed.path or "/"

    # Prepare log data
    log_data: dict[str, Any] = {
        "method": request.method,
        "hostname": hostname,
        "path": path,
        "url": request.url,
    }

    # Handle data field - show up to 1028 chars with length indicator if longer
    if request.data is not None:
        if len(request.data) <= 1028:
            log_data["data"] = request.data
        else:
            log_data["data"] = request.data[:1028] + "..."
            log_data["data_length"] = f"{len(request.data)} characters (showing first 1028)"

    logger.info("HTTP request", **log_data)

    return {"status": "logged"}


@app.post("/log_response")
async def log_response(response: HttpResponseLog) -> dict[str, str]:
    """
    Log HTTP response details.

    Logs method, hostname, path, status code, and data (truncated if too long).
    Headers are not logged for security.
    """
    from typing import Any
    from urllib.parse import urlparse

    # Parse URL to extract hostname and path
    parsed = urlparse(response.url)
    hostname = parsed.netloc
    path = parsed.path or "/"

    # Prepare log data
    log_data: dict[str, Any] = {
        "method": response.method,
        "hostname": hostname,
        "path": path,
        "url": response.url,
        "status_code": response.status_code,
    }

    # Handle data field - show up to 1028 chars with length indicator if longer
    if response.data is not None:
        if len(response.data) <= 1028:
            log_data["data"] = response.data
        else:
            log_data["data"] = response.data[:1028] + "..."
            log_data["data_length"] = f"{len(response.data)} characters (showing first 1028)"

    logger.info("HTTP response", **log_data)

    return {"status": "logged"}


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
