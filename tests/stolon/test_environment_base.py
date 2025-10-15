"""Unit tests for stolon Environment base class."""

from unittest.mock import Mock, patch

import pytest

from stolon.client import HttpHandle, StolonClient
from stolon.environments.base import Environment


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


@patch("stolon.environments.base.httpx.Client")
def test_get_request_success(
    mock_httpx_client_class: Mock, test_env: MockEnvironment, mock_stolon_client: Mock
) -> None:
    """Test successful GET request."""
    # Setup mock handle
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Setup mock HTTP response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"result": "success"}'
    mock_response.json.return_value = {"result": "success"}
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.request.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request
    result = test_env.get("/v3/test")

    # Verify
    assert result == {"result": "success"}
    mock_client.request.assert_called_once()
    call_args = mock_client.request.call_args
    assert call_args[0][0] == "GET"
    assert call_args[0][1] == "https://test.dev.clover.com/v3/test"


@patch("stolon.environments.base.httpx.Client")
def test_post_request_with_json_body(
    mock_httpx_client_class: Mock, test_env: MockEnvironment, mock_stolon_client: Mock
) -> None:
    """Test POST request with JSON body."""
    # Setup mock handle
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Setup mock HTTP response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"id": "123", "created": true}'
    mock_response.json.return_value = {"id": "123", "created": True}
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.request.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request
    result = test_env.post("/v3/test", json={"name": "test"})

    # Verify
    assert result == {"id": "123", "created": True}
    mock_client.request.assert_called_once()
    call_args = mock_client.request.call_args
    assert call_args[0][0] == "POST"
    assert call_args[0][1] == "https://test.dev.clover.com/v3/test"
    assert call_args[1]["json"] == {"name": "test"}


@patch("stolon.environments.base.httpx.Client")
def test_request_401_retry_logic(
    mock_httpx_client_class: Mock, test_env: MockEnvironment, mock_stolon_client: Mock
) -> None:
    """Test that 401 triggers token refresh and retry."""
    # Setup mock handles (first expired, second fresh)
    expired_handle = HttpHandle(
        token="expired_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com"
    )
    fresh_handle = HttpHandle(token="fresh_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.side_effect = [expired_handle, fresh_handle]

    # Setup mock HTTP responses (401 then 200)
    mock_401_response = Mock()
    mock_401_response.status_code = 401

    mock_200_response = Mock()
    mock_200_response.status_code = 200
    mock_200_response.text = '{"result": "success_after_retry"}'
    mock_200_response.json.return_value = {"result": "success_after_retry"}
    mock_200_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.request.side_effect = [mock_401_response, mock_200_response]
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request (should retry after 401)
    result = test_env.get("/v3/test")

    # Verify
    assert result == {"result": "success_after_retry"}
    assert mock_client.request.call_count == 2  # Initial + retry
    assert mock_stolon_client.request_internal_token.call_count == 2  # Initial + refresh

    # Verify second call used force_refresh=True
    second_call_kwargs = mock_stolon_client.request_internal_token.call_args_list[1][1]
    assert second_call_kwargs["force_refresh"] is True


@patch("stolon.environments.base.httpx.Client")
def test_request_with_params(
    mock_httpx_client_class: Mock, test_env: MockEnvironment, mock_stolon_client: Mock
) -> None:
    """Test request with query parameters."""
    # Setup mock handle
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Setup mock HTTP response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"results": []}'
    mock_response.json.return_value = {"results": []}
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.request.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request with params
    result = test_env.get("/v3/test", params={"limit": 10, "offset": 0})

    # Verify
    assert result == {"results": []}
    call_args = mock_client.request.call_args
    assert call_args[1]["params"] == {"limit": 10, "offset": 0}


@patch("stolon.environments.base.httpx.Client")
def test_request_empty_response_returns_none(
    mock_httpx_client_class: Mock, test_env: MockEnvironment, mock_stolon_client: Mock
) -> None:
    """Test that empty response body returns None."""
    # Setup mock handle
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Setup mock HTTP response with empty body
    mock_response = Mock()
    mock_response.status_code = 204
    mock_response.text = ""
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.request.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request
    result = test_env.delete("/v3/test/123")

    # Verify
    assert result is None


@patch("stolon.environments.base.httpx.Client")
def test_request_with_custom_timeout(
    mock_httpx_client_class: Mock, test_env: MockEnvironment, mock_stolon_client: Mock
) -> None:
    """Test request with custom timeout value."""
    # Setup mock handle
    mock_handle = HttpHandle(token="test_token", domain="test.dev.clover.com", base_url="https://test.dev.clover.com")
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Setup mock HTTP response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"ok": true}'
    mock_response.json.return_value = {"ok": True}
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.request.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request with custom timeout
    result = test_env.get("/v3/test", timeout=60.0)

    # Verify timeout was passed
    call_args = mock_client.request.call_args
    assert call_args[1]["timeout"] == 60.0
    assert result == {"ok": True}
