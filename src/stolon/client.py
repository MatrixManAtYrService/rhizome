"""Stolon client for communicating with the stolon server to manage HTTP API access."""

import structlog
import httpx
from dataclasses import dataclass

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

    def request_internal_token(self, domain: str) -> HttpHandle:
        """
        Request an internal session token from the stolon server.

        Args:
            domain: Clover domain to authenticate with (e.g., "dev1.dev.clover.com")

        Returns:
            HttpHandle: Authentication handle with token and domain info
        """
        # Make request to stolon server to get internal token
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/internal_token",
                json={"domain": domain},
            )
            response.raise_for_status()
            data = response.json()

        token = data["token"]
        domain = data["domain"]

        return HttpHandle(token=token, domain=domain, base_url=f"https://{domain}")
