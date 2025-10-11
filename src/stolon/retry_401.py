"""
Retry wrapper for HTTP requests that automatically refreshes tokens on 401 errors.

Uses stamina for retry logic with automatic token refresh.
"""

from typing import Any, Callable

import httpx
import stamina
from stamina.typing import AsyncRetryable, Retryable

from stolon.client import StolonClient


class TokenExpiredError(Exception):
    """Raised when a 401 error indicates the token has expired."""

    pass


def should_retry_for_auth(retry_state: dict[str, Any]) -> bool:
    """
    Determine if we should retry based on a 401 error.

    Args:
        retry_state: State from stamina containing the exception

    Returns:
        True if this is a TokenExpiredError (401), False otherwise
    """
    exc = retry_state.get("exception")
    return isinstance(exc, TokenExpiredError)


def make_authenticated_request(
    stolon_client: StolonClient,
    domain: str,
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    json: dict[str, Any] | None = None,
    **kwargs: Any,
) -> httpx.Response:
    """
    Make an authenticated HTTP request with automatic token refresh on 401.

    This function will:
    1. Get a token from the stolon client
    2. Make the HTTP request
    3. If 401 error occurs, invalidate the cached token and retry with a fresh one
    4. Use stamina for retry logic (max 2 attempts: original + 1 retry)

    Args:
        stolon_client: Stolon client to get tokens from
        domain: Clover domain (e.g., "dev1.dev.clover.com")
        method: HTTP method (GET, POST, etc.)
        url: Full URL to request
        headers: Optional headers (will be merged with auth headers)
        json: Optional JSON body
        **kwargs: Additional arguments passed to httpx

    Returns:
        httpx.Response: The successful response

    Raises:
        TokenExpiredError: If still getting 401 after retry
        httpx.HTTPStatusError: For other HTTP errors

    Example:
        >>> response = make_authenticated_request(
        ...     stolon_client,
        ...     "dev1.dev.clover.com",
        ...     "GET",
        ...     "https://dev1.dev.clover.com/v3/internal/internal_accounts/current"
        ... )
    """

    @stamina.retry(on=TokenExpiredError, attempts=2, wait_initial=0.1, wait_max=1.0)
    def _make_request() -> httpx.Response:
        # Get token (may be cached or fresh)
        handle = stolon_client.request_internal_token(domain)

        # Build headers
        req_headers = headers or {}
        req_headers = {**req_headers, "Accept": "application/json"}

        # Build cookies with session token
        cookies = {"internalSession": handle.token}

        # Make the request
        response = httpx.request(method, url, headers=req_headers, cookies=cookies, json=json, **kwargs)

        # Check for 401 and convert to TokenExpiredError for retry
        if response.status_code == 401:
            # Invalidate the cached token so next attempt gets a fresh one
            stolon_client.invalidate_token(domain)
            raise TokenExpiredError(f"Token expired for {domain}: {response.text}")

        # For other errors, raise immediately (no retry)
        response.raise_for_status()

        return response

    return _make_request()


def make_authenticated_get(
    stolon_client: StolonClient,
    domain: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    **kwargs: Any,
) -> httpx.Response:
    """
    Make an authenticated GET request with automatic token refresh on 401.

    Args:
        stolon_client: Stolon client to get tokens from
        domain: Clover domain (e.g., "dev1.dev.clover.com")
        url: Full URL to request
        headers: Optional headers
        **kwargs: Additional arguments passed to httpx

    Returns:
        httpx.Response: The successful response

    Example:
        >>> response = make_authenticated_get(
        ...     stolon_client,
        ...     "dev1.dev.clover.com",
        ...     "https://dev1.dev.clover.com/v3/internal/internal_accounts/current"
        ... )
    """
    return make_authenticated_request(stolon_client, domain, "GET", url, headers=headers, **kwargs)


def make_authenticated_post(
    stolon_client: StolonClient,
    domain: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    json: dict[str, Any] | None = None,
    **kwargs: Any,
) -> httpx.Response:
    """
    Make an authenticated POST request with automatic token refresh on 401.

    Args:
        stolon_client: Stolon client to get tokens from
        domain: Clover domain (e.g., "dev1.dev.clover.com")
        url: Full URL to request
        headers: Optional headers
        json: Optional JSON body
        **kwargs: Additional arguments passed to httpx

    Returns:
        httpx.Response: The successful response

    Example:
        >>> response = make_authenticated_post(
        ...     stolon_client,
        ...     "dev1.dev.clover.com",
        ...     "https://dev1.dev.clover.com/v3/resellers",
        ...     json={"name": "Test Reseller"}
        ... )
    """
    return make_authenticated_request(stolon_client, domain, "POST", url, headers=headers, json=json, **kwargs)
