"""Base classes for stolon environments."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from stolon.client import HttpHandle, StolonClient


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

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
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

        headers = kwargs.pop("headers", {})
        headers["Cookie"] = f"internalSession={self._handle.token}"
        headers["Content-Type"] = "application/json"
        headers["X-Clover-Appenv"] = f"{self.name}:{self.domain.split('.')[0]}"

        with httpx.Client() as client:
            response = client.request(method, f"{self._handle.base_url}{path}", headers=headers, **kwargs)

            # If we get a 401, the token is expired - invalidate cache and get fresh token
            if response.status_code == 401:
                self._handle = None
                self._ensure_authenticated(force_refresh=True)
                assert self._handle is not None

                # Retry with the new token
                headers["Cookie"] = f"internalSession={self._handle.token}"
                response = client.request(method, f"{self._handle.base_url}{path}", headers=headers, **kwargs)

            response.raise_for_status()
            # Return JSON if available, None otherwise
            if response.text:
                return response.json()
            return None

    def get(self, path: str, **kwargs: Any) -> Any:
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

    def post(self, path: str, **kwargs: Any) -> Any:
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

    def delete(self, path: str, **kwargs: Any) -> Any:
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
