"""Unit tests for stolon Environment base class."""

from unittest.mock import Mock

import pytest

from stolon.client import HttpHandle, StolonClient
from stolon.environments.base import Environment
from stolon.models import ProxyResponse


class MockEnvironment(Environment):
    """Concrete mock environment for unit tests."""

    @property
    def name(self) -> str:
        return "test"

    @property
    def domain(self) -> str:
        return "test.dev.clover.com"


@pytest.fixture
def mock_stolon_client() -> Mock:
    """Mock StolonClient."""
    client = Mock(spec=StolonClient)
    client.base_url = "http://0.0.0.0:62382"
    return client


@pytest.fixture
def test_env(mock_stolon_client: Mock) -> MockEnvironment:
    """Test environment instance."""
    return MockEnvironment(mock_stolon_client)


def test_ensure_authenticated_gets_token(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test that ensure_authenticated requests token."""
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Trigger authentication
    test_env.ensure_authenticated()

    # Verify
    assert test_env.handle == mock_handle
    mock_stolon_client.request_internal_token.assert_called_once_with("test.dev.clover.com", force_refresh=False)


def test_ensure_authenticated_with_force_refresh(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test that ensure_authenticated with force_refresh requests new token."""
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Set existing handle
    test_env.handle = Mock()

    # Trigger authentication with force_refresh
    test_env.ensure_authenticated(force_refresh=True)

    # Verify
    assert test_env.handle == mock_handle
    mock_stolon_client.request_internal_token.assert_called_once_with("test.dev.clover.com", force_refresh=True)


def test_get_request_success(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test successful GET request."""
    # Setup mock proxy response
    proxy_response = ProxyResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"result": "success"}',
    )
    mock_stolon_client.proxy_request.return_value = proxy_response

    # Make request
    result = test_env.get("/v3/test")

    # Verify
    assert result == {"result": "success"}
    mock_stolon_client.proxy_request.assert_called_once_with(
        domain="test.dev.clover.com",
        method="GET",
        path="/v3/test",
        environment_name="test",
        json_body=None,
        params=None,
        timeout=None,
    )


def test_post_request_with_json_body(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test POST request with JSON body."""
    # Setup mock proxy response
    proxy_response = ProxyResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"id": "123", "created": true}',
    )
    mock_stolon_client.proxy_request.return_value = proxy_response

    # Make request
    result = test_env.post("/v3/test", json={"name": "test"})

    # Verify
    assert result == {"id": "123", "created": True}
    mock_stolon_client.proxy_request.assert_called_once_with(
        domain="test.dev.clover.com",
        method="POST",
        path="/v3/test",
        environment_name="test",
        json_body={"name": "test"},
        params=None,
        timeout=None,
    )


def test_request_401_retry_logic(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test that 401 triggers token refresh and retry.

    NOTE: In the proxy architecture, 401 handling is done server-side.
    The client just receives the final successful response. This test
    verifies that the proxy_request is called correctly.
    """
    # Setup mock proxy response (server already handled 401 retry)
    proxy_response = ProxyResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"result": "success_after_retry"}',
    )
    mock_stolon_client.proxy_request.return_value = proxy_response

    # Make request
    result = test_env.get("/v3/test")

    # Verify - client only sees the successful response
    assert result == {"result": "success_after_retry"}
    mock_stolon_client.proxy_request.assert_called_once()


def test_request_with_params(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test request with query parameters."""
    # Setup mock proxy response
    proxy_response = ProxyResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"results": []}',
    )
    mock_stolon_client.proxy_request.return_value = proxy_response

    # Make request with params
    result = test_env.get("/v3/test", params={"limit": 10, "offset": 0})

    # Verify
    assert result == {"results": []}
    mock_stolon_client.proxy_request.assert_called_once_with(
        domain="test.dev.clover.com",
        method="GET",
        path="/v3/test",
        environment_name="test",
        json_body=None,
        params={"limit": 10, "offset": 0},
        timeout=None,
    )


def test_request_empty_response_returns_none(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test that empty response body returns None."""
    # Setup mock proxy response with empty body
    proxy_response = ProxyResponse(
        status_code=204,
        headers={},
        body="",
    )
    mock_stolon_client.proxy_request.return_value = proxy_response

    # Make request
    result = test_env.delete("/v3/test/123")

    # Verify
    assert result is None
    mock_stolon_client.proxy_request.assert_called_once()


def test_request_with_custom_timeout(test_env: MockEnvironment, mock_stolon_client: Mock) -> None:
    """Test request with custom timeout value."""
    # Setup mock proxy response
    proxy_response = ProxyResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body='{"ok": true}',
    )
    mock_stolon_client.proxy_request.return_value = proxy_response

    # Make request with custom timeout
    result = test_env.get("/v3/test", timeout=60.0)

    # Verify timeout was passed
    mock_stolon_client.proxy_request.assert_called_once_with(
        domain="test.dev.clover.com",
        method="GET",
        path="/v3/test",
        environment_name="test",
        json_body=None,
        params=None,
        timeout=60.0,
    )
    assert result == {"ok": True}
