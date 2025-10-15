"""Base classes for stolon environments."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, TypedDict, Unpack

import httpx
import structlog

if TYPE_CHECKING:
    from stolon.client import HttpHandle, StolonClient


class HttpxKwargs(TypedDict, total=False):
    """Type definition for httpx request kwargs."""

    json: Any
    data: Any
    params: dict[str, Any] | None
    headers: dict[str, str] | None
    cookies: dict[str, str] | None
    timeout: float | None


class Environment(ABC):
    """Abstract base class for stolon environments."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging."""

    @property
    @abstractmethod
    def domain(self) -> str:
        """Clover domain for this environment (e.g., 'dev1.dev.clover.com')."""

    def __init__(self, client: StolonClient) -> None:
        """Initialize the environment with a stolon client."""
        self.client = client
        self.handle: HttpHandle | None = None

    def _create_httpx_client(self) -> httpx.Client:
        """
        Create an httpx.Client with event hooks for automatic request/response logging.

        All HTTP requests made through this client will be logged to the stolon server
        at the /log_request and /log_response endpoints.

        Returns:
            httpx.Client configured for this environment with logging hooks
        """
        from collections.abc import Callable
        from contextlib import suppress

        def log_request_hook(request: httpx.Request) -> None:
            """Log HTTP request to stolon server (fire-and-forget)."""
            with suppress(Exception):
                # Extract request body if present
                body_str: str | None = None
                if request.content:
                    try:
                        body_str = request.content.decode("utf-8")
                    except Exception:
                        body_str = f"<binary data, {len(request.content)} bytes>"

                httpx.post(
                    f"{self.client.base_url}/log_request",
                    json={
                        "method": request.method,
                        "url": str(request.url),
                        "data": body_str,
                    },
                    timeout=1.0,
                )

        def log_response_hook(response: httpx.Response) -> None:
            """Log HTTP response to stolon server (fire-and-forget)."""
            # Extract response body if present (may fail for streaming responses)
            body_str: str | None = None
            try:
                if response.content:
                    body_str = response.content.decode("utf-8")
            except Exception:
                # Content access failed (streaming response or decode error) - skip body
                pass

            # Send to stolon server (fire-and-forget with fallback logging)
            try:
                httpx.post(
                    f"{self.client.base_url}/log_response",
                    json={
                        "method": response.request.method,
                        "url": str(response.request.url),
                        "status_code": response.status_code,
                        "data": body_str,
                    },
                    timeout=1.0,
                )
            except Exception as e:
                # If server logging fails, log locally as fallback for debugging
                logger = structlog.get_logger()
                logger.warning(
                    "Failed to log response to stolon server",
                    error=str(e),
                    url=str(response.request.url),
                    status_code=response.status_code,
                )

        # Add hooks to lists
        request_hooks: list[Callable[[httpx.Request], None]] = [log_request_hook]
        response_hooks: list[Callable[[httpx.Response], None]] = [log_response_hook]

        event_hooks = {
            "request": request_hooks,
            "response": response_hooks,
        }

        return httpx.Client(event_hooks=event_hooks)

    def ensure_authenticated(self, *, force_refresh: bool = False) -> None:
        """
        Ensure we have a valid authentication token.

        Args:
            force_refresh: If True, force getting a fresh token even if one is cached
        """
        if self.handle is None or force_refresh:
            self.handle = self.client.request_internal_token(self.domain, force_refresh=force_refresh)

    def _request(self, method: str, path: str, **kwargs: Unpack[HttpxKwargs]) -> dict[str, Any] | list[Any] | None:
        """
        Make an authenticated HTTP request via stolon server proxy.

        The stolon server handles:
        - Authentication token management
        - 401 retry logic
        - Request/response logging

        Args:
            method: HTTP method (GET, POST, DELETE, etc.)
            path: API path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data (JSON if available, None otherwise)
        """
        import json as json_module

        logger = structlog.get_logger()

        # Extract kwargs
        json_data: Any = kwargs.get("json")
        params: dict[str, Any] | None = kwargs.get("params")
        timeout_val: float | None = kwargs.get("timeout")

        # Call stolon server proxy endpoint
        proxy_response = self.client.proxy_request(
            domain=self.domain,
            method=method,
            path=path,
            environment_name=self.name,
            json_body=json_data,
            params=params,
            timeout=timeout_val,
        )

        # Parse response
        if proxy_response.status_code >= 400:
            logger.error(
                "HTTP request failed",
                method=method,
                path=path,
                status_code=proxy_response.status_code,
                response_body=proxy_response.body[:500] if proxy_response.body else None,
            )
            raise httpx.HTTPStatusError(
                message=f"HTTP {proxy_response.status_code}",
                request=None,  # type: ignore[arg-type]
                response=None,  # type: ignore[arg-type]
            )

        # Return JSON if available
        if proxy_response.body:
            response_data: dict[str, Any] | list[Any] = json_module.loads(proxy_response.body)
            return response_data
        return None

    def get(self, path: str, **kwargs: Unpack[HttpxKwargs]) -> dict[str, Any] | list[Any] | None:
        """
        Make an authenticated GET request to the Clover API.

        Automatically retries with a fresh token if a 401 Unauthorized response is received.

        Args:
            path: API path (e.g., '/v3/merchants/MSR15REPHS0N5')
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data
        """
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Unpack[HttpxKwargs]) -> dict[str, Any] | list[Any] | None:
        """
        Make an authenticated POST request to the Clover API.

        Automatically retries with a fresh token if a 401 Unauthorized response is received.

        Args:
            path: API path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data
        """
        return self._request("POST", path, **kwargs)

    def delete(self, path: str, **kwargs: Unpack[HttpxKwargs]) -> dict[str, Any] | list[Any] | None:
        """
        Make an authenticated DELETE request to the Clover API.

        Automatically retries with a fresh token if a 401 Unauthorized response is received.

        Args:
            path: API path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data (if any)
        """
        return self._request("DELETE", path, **kwargs)
