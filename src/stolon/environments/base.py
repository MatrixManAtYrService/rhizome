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
        self._handle: HttpHandle | None = None

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
            try:
                # Extract response body if present
                body_str: str | None = None
                if response.content:
                    try:
                        body_str = response.content.decode("utf-8")
                    except Exception:
                        body_str = f"<binary data, {len(response.content)} bytes>"

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

    def _ensure_authenticated(self, *, force_refresh: bool = False) -> None:
        """
        Ensure we have a valid authentication token.

        Args:
            force_refresh: If True, force getting a fresh token even if one is cached
        """
        if self._handle is None or force_refresh:
            self._handle = self.client.request_internal_token(self.domain, force_refresh=force_refresh)

    def _request(self, method: str, path: str, **kwargs: Unpack[HttpxKwargs]) -> dict[str, Any] | list[Any] | None:
        """
        Make an authenticated HTTP request with automatic 401 retry.

        Args:
            method: HTTP method (GET, POST, DELETE, etc.)
            path: API path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data (JSON if available, None otherwise)
        """
        self._ensure_authenticated()
        assert self._handle is not None  # For type checker

        logger = structlog.get_logger()

        # Build headers dict, merging any provided headers with our auth headers
        # Extract headers from kwargs to avoid conflict when passing **kwargs
        provided_headers = kwargs.pop("headers", None)  # type: ignore[misc]
        headers: dict[str, str] = provided_headers.copy() if provided_headers else {}
        headers["Cookie"] = f"internalSession={self._handle.token}"
        headers["Content-Type"] = "application/json"
        headers["X-Clover-Appenv"] = f"{self.name}:{self.domain.split('.')[0]}"

        # Extract other common kwargs
        json_data: Any = kwargs.pop("json", None)  # type: ignore[misc]
        params: dict[str, Any] | None = kwargs.pop("params", None)  # type: ignore[misc]
        timeout_val: float | None = kwargs.pop("timeout", None)  # type: ignore[misc]

        # Build full URL
        full_url = f"{self._handle.base_url}{path}"

        with self._create_httpx_client() as client:
            response: httpx.Response = client.request(
                method,
                full_url,
                headers=headers,
                json=json_data,  # type: ignore[arg-type]
                params=params,
                timeout=timeout_val,
            )

            # If we get a 401, the token is expired - invalidate cache and get fresh token
            if response.status_code == 401:
                logger.warning("Received 401, refreshing token and retrying")
                self._handle = None
                self._ensure_authenticated(force_refresh=True)
                assert self._handle is not None

                # Retry with the new token
                headers["Cookie"] = f"internalSession={self._handle.token}"
                response = client.request(
                    method,
                    full_url,
                    headers=headers,
                    json=json_data,  # type: ignore[arg-type]
                    params=params,
                    timeout=timeout_val,
                )

                logger.info(
                    "Retry response after token refresh",
                    method=method,
                    url=full_url,
                    status_code=response.status_code,
                )

            # Log error details before raising
            if response.status_code >= 400:
                logger.error(
                    "HTTP request failed",
                    method=method,
                    url=full_url,
                    status_code=response.status_code,
                    response_text=response.text[:500] if response.text else None,  # First 500 chars
                    response_headers=dict(response.headers),
                )

            response.raise_for_status()
            # Return JSON if available, None otherwise
            if response.text:
                response_data: dict[str, Any] | list[Any] = response.json()
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
