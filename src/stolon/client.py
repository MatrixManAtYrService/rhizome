"""Stolon client for communicating with the stolon server to manage HTTP API access."""

from dataclasses import dataclass
from typing import Any

import httpx
import structlog

from stolon.models import OpenAPIInvokeRequest, OpenAPIInvokeResponse, OpenAPIService, ProxyRequest, ProxyResponse
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

    def proxy_request(
        self,
        domain: str,
        method: str,
        path: str,
        environment_name: str,
        json_body: dict[str, Any] | None = None,
        content: str | None = None,
        content_type: str | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> ProxyResponse:
        """
        Proxy an HTTP request through the stolon server.

        This is the primary method for making API calls.
        The server handles:
        - Authentication token management
        - 401 retry logic
        - Request/response logging

        Args:
            domain: Target domain (e.g., "dev1.dev.clover.com")
            method: HTTP method (GET, POST, DELETE, etc.)
            path: API path (e.g., "/v3/merchants/ABC123")
            environment_name: Environment name for headers
            json_body: Optional JSON body for POST/PUT (mutually exclusive with content)
            content: Optional raw content (e.g., XML) (mutually exclusive with json_body)
            content_type: Optional Content-Type header (e.g., "application/xml")
            params: Optional query parameters
            timeout: Optional timeout in seconds

        Returns:
            ProxyResponse with status code, headers, and body
        """
        request = ProxyRequest(
            domain=domain,
            method=method,
            path=path,
            json_body=json_body,
            content=content,
            content_type=content_type,
            params=params,
            timeout=timeout,
            environment_name=environment_name,
        )

        with httpx.Client(timeout=timeout or 30.0) as client:
            response = client.post(
                f"{self.base_url}/proxy",
                json=request.model_dump(),
            )
            response.raise_for_status()

            proxy_response = ProxyResponse(**response.json())
            return proxy_response

    def invoke_openapi(
        self,
        service: OpenAPIService,
        function_path: str,
        variant: str,
        domain: str,
        environment_name: str,
        kwargs: dict[str, Any],
        timeout: float | None = None,
    ) -> OpenAPIInvokeResponse:
        """
        Invoke an OpenAPI-generated function on the stolon server.

        The server handles:
        - Dynamic function import
        - Authentication token management
        - 401 retry logic
        - Request/response serialization

        Args:
            service: OpenAPI service to invoke (e.g., OpenAPIService.BILLING_BOOKKEEPER_DEV)
            function_path: Function path (e.g., "acceptance_controller_impl.get_bulk_acceptances_service_scope")
            variant: Function variant ("sync", "sync_detailed", "asyncio", "asyncio_detailed")
            domain: Target domain (e.g., "dev1.dev.clover.com")
            environment_name: Environment name for headers
            kwargs: Serialized function arguments
            timeout: Optional timeout in seconds

        Returns:
            OpenAPIInvokeResponse with success status, result data, and optional error
        """
        request = OpenAPIInvokeRequest(
            service=service,
            function_path=function_path,
            variant=variant,
            kwargs=kwargs,
            domain=domain,
            environment_name=environment_name,
        )

        with httpx.Client(timeout=timeout or 30.0) as client:
            response = client.post(
                f"{self.base_url}/invoke_openapi",
                json=request.model_dump(),
            )
            response.raise_for_status()

            invoke_response = OpenAPIInvokeResponse(**response.json())
            return invoke_response
