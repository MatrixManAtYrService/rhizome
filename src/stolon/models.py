"""Pydantic models for stolon server."""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel


class OpenAPIService(StrEnum):
    """
    Enumeration of available OpenAPI services.

    These values match the directory names in stolon/openapi_generated/.
    """

    AGREEMENT_K8S_DEV = "agreement_k8s_dev"
    BILLING_BOOKKEEPER_DEV = "billing_bookkeeper_dev"
    BILLING_EVENT_DEV = "billing_event_dev"


# Service base path mapping for services that need context path prefixes
# These are the URL path prefixes needed for certain services
SERVICE_BASE_PATHS: dict[OpenAPIService, str] = {
    OpenAPIService.AGREEMENT_K8S_DEV: "/agreement",
    OpenAPIService.BILLING_BOOKKEEPER_DEV: "/billing-bookkeeper",
    OpenAPIService.BILLING_EVENT_DEV: "/billing-event",
}


class InternalTokenRequest(BaseModel):
    """Request model for internal token requests."""

    domain: str


class InternalTokenResponse(BaseModel):
    """Response model for internal token responses."""

    token: str
    domain: str
    cached: bool = False


class HttpRequestLog(BaseModel):
    """Request model for HTTP request logging."""

    method: str
    url: str
    data: str | None = None


class HttpResponseLog(BaseModel):
    """Request model for HTTP response logging."""

    method: str
    url: str
    status_code: int
    data: str | None = None


class ProxyRequest(BaseModel):
    """Request to proxy an HTTP call through stolon server."""

    domain: str
    method: str  # GET, POST, DELETE, etc.
    path: str  # e.g., "/v3/merchants/ABC123"
    json_body: dict[str, Any] | None = None
    content: str | None = None  # Raw content (e.g., XML) - mutually exclusive with json_body
    content_type: str | None = None  # Content-Type header (e.g., "application/xml")
    params: dict[str, Any] | None = None
    timeout: float | None = None
    environment_name: str  # For X-Clover-Appenv header


class ProxyResponse(BaseModel):
    """Response from proxied HTTP call."""

    status_code: int
    headers: dict[str, str]
    body: str  # JSON string or other response body


class OpenAPIInvokeRequest(BaseModel):
    """Request to invoke an OpenAPI-generated function on the server."""

    service: OpenAPIService  # e.g., OpenAPIService.BILLING_BOOKKEEPER_DEV
    function_path: str  # e.g., "acceptance_controller_impl.get_bulk_acceptances_service_scope"
    variant: str  # "sync", "sync_detailed", "asyncio", "asyncio_detailed"
    kwargs: dict[str, Any]  # Serialized function arguments
    domain: str  # e.g., "dev1.dev.clover.com"
    environment_name: str  # For X-Clover-Appenv header


class OpenAPIInvokeResponse(BaseModel):
    """Response from OpenAPI function invocation."""

    success: bool
    result: Any = None  # Serialized result from the function
    error: str | None = None  # Error message if success=False
    status_code: int | None = None  # HTTP status code if available
