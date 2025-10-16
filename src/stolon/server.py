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
    SERVICE_BASE_PATHS,
    HttpRequestLog,
    HttpResponseLog,
    InternalTokenRequest,
    InternalTokenResponse,
    OpenAPIInvokeRequest,
    OpenAPIInvokeResponse,
    OpenAPIService,
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


def _get_service_base_path(service: OpenAPIService) -> str:
    """
    Get the base path for services that need context path prefixes.

    Args:
        service: The OpenAPI service

    Returns:
        Base path string (empty string if service doesn't need a prefix)

    Raises:
        NotImplementedError: If the service is not recognized
    """
    try:
        return SERVICE_BASE_PATHS.get(service, "")
    except KeyError as e:
        raise NotImplementedError(f"Service {service} is not supported") from e


def _import_openapi_function(service: OpenAPIService, function_path: str, variant: str) -> object:
    """Import an OpenAPI-generated function dynamically."""
    import importlib

    module_path = f"stolon.openapi_generated.{service.value}.open_api_definition_client.api.{function_path}"
    module = importlib.import_module(module_path)
    return getattr(module, variant)


def _create_authenticated_client(
    service: OpenAPIService, domain: str, token: str, environment_name: str, base_path: str
) -> object:
    """Create an authenticated OpenAPI client."""
    import importlib

    client_module_path = f"stolon.openapi_generated.{service.value}.open_api_definition_client"
    client_module = importlib.import_module(client_module_path)
    # Use Client (not AuthenticatedClient) since Clover uses cookie auth, not Bearer tokens
    Client = client_module.Client

    base_url = f"https://{domain}{base_path}"

    return Client(
        base_url=base_url,
        cookies={"internalSession": token},
        headers={"X-Clover-Appenv": f"{environment_name}:{domain.split('.')[0]}"},
    )


def _extract_status_code(result: object) -> int | None:
    """Extract status code from a result object if it has one."""
    from stolon.serialization import ResponseObject

    if hasattr(result, "status_code") and hasattr(result, "parsed"):
        # Type narrow to ResponseObject
        response: ResponseObject = result  # type: ignore[assignment]
        return response.status_code.value
    return None


def _deserialize_kwargs(func: object, kwargs: dict[str, object], service: OpenAPIService) -> dict[str, object]:
    """Deserialize kwargs based on function signature."""
    import inspect

    from stolon.serialization import deserialize_argument

    # Get function signature
    sig = inspect.signature(func)  # type: ignore[arg-type]

    deserialized: dict[str, object] = {}

    for param_name, param_value in kwargs.items():
        if param_name in sig.parameters:
            param = sig.parameters[param_name]
            # Get type hint as string
            if param.annotation != inspect.Parameter.empty:
                type_hint = str(param.annotation)
                # Remove module prefixes to get just the class name
                # (e.g., "stolon.openapi_generated...models.ModelName" -> "ModelName")
                if "." in type_hint:
                    parts = type_hint.split(".")
                    type_hint = parts[-1].strip("'>")  # Handle forward references like "<class 'ModelName'>"

                # Deserialize the parameter
                deserialized[param_name] = deserialize_argument(param_value, type_hint, service.value)  # type: ignore[arg-type]
            else:
                # No type hint, pass as-is
                deserialized[param_name] = param_value
        else:
            # Parameter not in signature, pass as-is
            deserialized[param_name] = param_value

    return deserialized


async def _execute_openapi_call(
    func: object, auth_client: object, kwargs: dict[str, object], request: OpenAPIInvokeRequest
) -> OpenAPIInvokeResponse:
    """Execute OpenAPI function call and serialize result."""
    from stolon.serialization import serialize_result

    try:
        # Deserialize kwargs based on function signature
        deserialized_kwargs = _deserialize_kwargs(func, kwargs, request.service)

        result = func(client=auth_client, **deserialized_kwargs)  # type: ignore[operator]

        if asyncio.iscoroutine(result):  # type: ignore[arg-type]
            result = await result

        serialized_result = serialize_result(result)  # type: ignore[arg-type]
        status_code = _extract_status_code(result)  # type: ignore[arg-type]

        logger.info(
            "OpenAPI function succeeded",
            service=request.service,
            function_path=request.function_path,
            status_code=status_code,
        )

        return OpenAPIInvokeResponse(
            success=True,
            result=serialized_result,
            status_code=status_code,
        )
    except Exception as e:
        logger.error(
            "OpenAPI function failed",
            service=request.service,
            function_path=request.function_path,
            error=str(e),
        )
        return OpenAPIInvokeResponse(
            success=False,
            error=str(e),
        )


def _is_auth_error(error: Exception) -> bool:
    """Check if an error is a 401 authentication error."""
    error_str = str(error)
    return "401" in error_str or "Unauthorized" in error_str


@app.post("/invoke_openapi")
async def invoke_openapi(request: OpenAPIInvokeRequest) -> OpenAPIInvokeResponse:
    """
    Invoke an OpenAPI-generated function on the server.

    This endpoint:
    1. Receives function path and serialized arguments
    2. Dynamically imports the OpenAPI function
    3. Creates an authenticated client with cached token
    4. Calls the function and handles auth retries
    5. Returns serialized result

    Benefits:
    - Server executes the full OpenAPI client (no parsing bugs)
    - Auth token management stays on server
    - Client code is simpler (just serialize/deserialize)
    """
    try:
        # Import the OpenAPI function
        logger.info(
            "Invoking OpenAPI function",
            service=request.service,
            function_path=request.function_path,
            variant=request.variant,
        )

        try:
            func = _import_openapi_function(request.service, request.function_path, request.variant)
        except (ImportError, AttributeError) as e:
            logger.error("Failed to import OpenAPI function", error=str(e))
            return OpenAPIInvokeResponse(success=False, error=f"Failed to import function: {e}")

        # Get token and create client
        token_response = await internal_token(InternalTokenRequest(domain=request.domain))
        token = token_response.token

        base_path = _get_service_base_path(request.service)
        auth_client = _create_authenticated_client(
            request.service, request.domain, token, request.environment_name, base_path
        )

        # Call the function
        response = await _execute_openapi_call(func, auth_client, request.kwargs, request)

        # Check if we got a 401 (either as exception or status code)
        needs_retry = False
        if (
            not response.success
            and response.error
            and _is_auth_error(Exception(response.error))
            or response.success
            and response.status_code == 401
        ):
            needs_retry = True

        if needs_retry:
            logger.warning(
                f"Received 401 for {request.domain}, refreshing token and retrying",
                service=request.service,
            )

            # Invalidate cached token
            if request.domain in _token_cache:
                del _token_cache[request.domain]

            # Get fresh token and create new client
            token_response = await internal_token(InternalTokenRequest(domain=request.domain))
            token = token_response.token
            auth_client = _create_authenticated_client(
                request.service, request.domain, token, request.environment_name, base_path
            )

            # Retry the function call
            response = await _execute_openapi_call(func, auth_client, request.kwargs, request)

            if response.success:
                logger.info(
                    "OpenAPI function succeeded after retry",
                    service=request.service,
                    function_path=request.function_path,
                    status_code=response.status_code,
                )

        return response

    except Exception as e:
        logger.error("invoke_openapi failed", error=str(e))
        return OpenAPIInvokeResponse(
            success=False,
            error=f"Server error: {e}",
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
