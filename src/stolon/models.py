"""Pydantic models for stolon server."""

from typing import Any

from pydantic import BaseModel


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
    params: dict[str, Any] | None = None
    timeout: float | None = None
    environment_name: str  # For X-Clover-Appenv header


class ProxyResponse(BaseModel):
    """Response from proxied HTTP call."""

    status_code: int
    headers: dict[str, str]
    body: str  # JSON string or other response body
