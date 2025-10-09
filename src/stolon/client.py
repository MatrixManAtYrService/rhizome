"""Stolon client for communicating with the stolon server to manage HTTP API access."""

from dataclasses import dataclass

import httpx
import structlog

from trifolium.config import Home


@dataclass
class HttpHandle:
    """
    HTTP API access handle returned by stolon.

    Contains the authentication token and domain information needed to make
    authenticated requests to Clover HTTP APIs.
    """

    token: str
    domain: str
    base_url: str

    def __post_init__(self) -> None:
        """Set up the base URL from the domain."""
        if not self.base_url:
            self.base_url = f"https://{self.domain}"


class StolonClient:
    """Client for communicating with the stolon server."""

    def __init__(self, home: Home | None = None, *, data_in_logs: bool) -> None:
        self.home = home or Home()
        self.logger = structlog.get_logger("stolon.client")
        self._base_url: str | None = None
        self.data_in_logs = data_in_logs

    @property
    def base_url(self) -> str:
        """Get the stolon server URL from the port file."""
        if self._base_url is None:
            port = self.home.get_stolon_port()
            if port is None:
                raise RuntimeError("Stolon server port not found. Make sure the stolon server is running.")
            self._base_url = f"http://0.0.0.0:{port}"
        return self._base_url

    def invalidate_token(self, domain: str) -> None:
        """
        Invalidate a cached token for a domain on the stolon server.

        This should be called when a token is discovered to be expired or invalid.

        Args:
            domain: Clover domain to invalidate token for
        """
        try:
            with httpx.Client() as client:
                response = client.delete(f"{self.base_url}/internal_token/{domain}")
                response.raise_for_status()
                self.logger.info(f"Invalidated cached token for {domain}")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                # No cached token to invalidate - that's fine
                pass
            else:
                self.logger.warning(f"Failed to invalidate token for {domain}: {e}")

    def request_internal_token(self, domain: str, *, force_refresh: bool = False) -> HttpHandle:
        """
        Request an internal session token from the stolon server.

        Args:
            domain: Clover domain to authenticate with (e.g., "dev1.dev.clover.com")
            force_refresh: If True, force server to get a new token even if cached

        Returns:
            HttpHandle: Authentication handle with token and domain info
        """
        # If forcing refresh, invalidate any cached token first
        if force_refresh:
            self.invalidate_token(domain)

        # Make request to stolon server to get internal token
        # Use a long timeout (5 minutes) to give user time to log in and paste token
        with httpx.Client(timeout=300.0) as client:
            response = client.post(
                f"{self.base_url}/internal_token",
                json={"domain": domain},
            )
            response.raise_for_status()
            data = response.json()

        token = data["token"]
        domain = data["domain"]

        return HttpHandle(token=token, domain=domain, base_url=f"https://{domain}")
