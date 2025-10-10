"""Base classes for stolon environments."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, TypedDict, Unpack

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
        import httpx

        # Build headers dict, merging any provided headers with our auth headers
        # Extract headers from kwargs to avoid conflict when passing **kwargs
        provided_headers = kwargs.pop("headers", None)  # type: ignore[misc]
        headers: dict[str, str] = provided_headers.copy() if provided_headers else {}
        headers["Cookie"] = f"internalSession={self._handle.token}"
        headers["Content-Type"] = "application/json"
        headers["X-Clover-Appenv"] = f"{self.name}:{self.domain.split('.')[0]}"

        # Extract other common kwargs
        json_data = kwargs.pop("json", None)  # type: ignore[misc]
        params = kwargs.pop("params", None)  # type: ignore[misc]
        timeout_val = kwargs.pop("timeout", None)  # type: ignore[misc]

        with httpx.Client() as client:
            response: httpx.Response = client.request(
                method,
                f"{self._handle.base_url}{path}",
                headers=headers,
                json=json_data,
                params=params,
                timeout=timeout_val,
            )

            # If we get a 401, the token is expired - invalidate cache and get fresh token
            if response.status_code == 401:
                self._handle = None
                self._ensure_authenticated(force_refresh=True)
                assert self._handle is not None

                # Retry with the new token
                headers["Cookie"] = f"internalSession={self._handle.token}"
                response = client.request(
                    method,
                    f"{self._handle.base_url}{path}",
                    headers=headers,
                    json=json_data,
                    params=params,
                    timeout=timeout_val,
                )

            response.raise_for_status()
            # Return JSON if available, None otherwise
            if response.text:
                json_data: dict[str, Any] | list[Any] = response.json()
                return json_data
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
