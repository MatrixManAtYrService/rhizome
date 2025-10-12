"""Pydantic models for stolon server."""

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
