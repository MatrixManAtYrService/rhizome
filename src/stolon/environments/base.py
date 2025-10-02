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

    def _ensure_authenticated(self) -> None:
        """Ensure we have a valid authentication token."""
        if self._handle is None:
            self._handle = self.client.request_internal_token(self.domain)

    def get(self, path: str, **kwargs: Any) -> Any:
        """
        Make an authenticated GET request to the Clover API.

        Args:
            path: API path (e.g., '/v3/merchants/MSR15REPHS0N5')
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data
        """
        self._ensure_authenticated()
        assert self._handle is not None  # For type checker - ensured by _ensure_authenticated
        import httpx

        headers = kwargs.pop("headers", {})
        headers["Cookie"] = f"internalSession={self._handle.token}"
        headers["Content-Type"] = "application/json"
        headers["X-Clover-Appenv"] = f"{self.name}:{self.domain.split('.')[0]}"

        with httpx.Client() as client:
            response = client.get(f"{self._handle.base_url}{path}", headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()

    def post(self, path: str, **kwargs: Any) -> Any:
        """
        Make an authenticated POST request to the Clover API.

        Args:
            path: API path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Response data
        """
        self._ensure_authenticated()
        assert self._handle is not None  # For type checker - ensured by _ensure_authenticated
        import httpx

        headers = kwargs.pop("headers", {})
        headers["Cookie"] = f"internalSession={self._handle.token}"
        headers["Content-Type"] = "application/json"
        headers["X-Clover-Appenv"] = f"{self.name}:{self.domain.split('.')[0]}"

        with httpx.Client() as client:
            response = client.post(f"{self._handle.base_url}{path}", headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
