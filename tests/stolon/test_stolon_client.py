"""Unit tests for StolonClient (no --external-infra required)."""

from pathlib import Path
from typing import Never
from unittest.mock import Mock, patch

import pytest

from stolon.client import StolonClient
from trifolium.config import Home


@pytest.fixture
def mock_home(tmp_path: Path) -> Mock:
    """Mock home with stolon port file."""
    home = Mock(spec=Home)
    port_file = tmp_path / "stolon_port"
    port_file.write_text("62382")
    home.get_stolon_port.return_value = 62382
    return home


@pytest.fixture
def stolon_client(mock_home: Mock) -> StolonClient:
    """StolonClient with mocked dependencies."""
    return StolonClient(home=mock_home, data_in_logs=False)


def test_base_url_from_port_file(stolon_client: StolonClient) -> None:
    """Test that base_url is constructed from port file."""
    assert stolon_client.base_url == "http://0.0.0.0:62382"


def test_base_url_missing_port_raises(mock_home: Mock) -> None:
    """Test that missing port file raises clear error."""
    mock_home.get_stolon_port.return_value = None
    client = StolonClient(home=mock_home, data_in_logs=False)

    with pytest.raises(RuntimeError, match="Stolon server port not found"):
        _ = client.base_url


@patch("stolon.client.httpx.Client")
def test_request_internal_token_success(mock_httpx_client_class: Mock, stolon_client: StolonClient) -> None:
    """Test successful token request."""
    # Setup mock response
    mock_response = Mock()
    mock_response.json.return_value = {
        "token": "test_token_123",
        "domain": "dev1.dev.clover.com",
        "cached": False,
    }
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.post.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Make request
    handle = stolon_client.request_internal_token("dev1.dev.clover.com")

    # Verify
    assert handle.token == "test_token_123"
    assert handle.domain == "dev1.dev.clover.com"
    assert handle.base_url == "https://dev1.dev.clover.com"

    mock_client.post.assert_called_once()
    call_args = mock_client.post.call_args
    assert call_args[0][0] == "http://0.0.0.0:62382/internal_token"
    assert call_args[1]["json"] == {"domain": "dev1.dev.clover.com"}


@patch("stolon.client.httpx.Client")
def test_invalidate_token_success(mock_httpx_client_class: Mock, stolon_client: StolonClient) -> None:
    """Test token invalidation."""
    mock_response = Mock()
    mock_response.raise_for_status = Mock()

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.delete.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Invalidate token
    stolon_client.invalidate_token("dev1.dev.clover.com")

    # Verify
    mock_client.delete.assert_called_once_with("http://0.0.0.0:62382/internal_token/dev1.dev.clover.com")


@patch("stolon.client.httpx.Client")
def test_request_internal_token_with_force_refresh(mock_httpx_client_class: Mock, stolon_client: StolonClient) -> None:
    """Test force_refresh invalidates token first."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "token": "new_token_456",
        "domain": "dev1.dev.clover.com",
        "cached": False,
    }
    mock_response.raise_for_status = Mock()
    mock_response.status_code = 200

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.post.return_value = mock_response
    mock_client.delete.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Request with force_refresh
    handle = stolon_client.request_internal_token("dev1.dev.clover.com", force_refresh=True)

    # Verify invalidation happened first
    assert mock_client.delete.call_count == 1
    assert mock_client.post.call_count == 1
    assert handle.token == "new_token_456"


@patch("stolon.client.httpx.Client")
def test_invalidate_token_404_is_ignored(mock_httpx_client_class: Mock, stolon_client: StolonClient) -> None:
    """Test that 404 on token invalidation is silently ignored."""
    # Setup mock 404 response
    mock_response = Mock()
    mock_response.status_code = 404

    def raise_404() -> Never:
        from httpx import HTTPStatusError

        raise HTTPStatusError("Not found", request=Mock(), response=mock_response)

    mock_response.raise_for_status = raise_404

    # Setup mock client with context manager support
    mock_client = Mock()
    mock_client.delete.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=None)
    mock_httpx_client_class.return_value = mock_client

    # Should not raise (404 means no token to invalidate, which is fine)
    stolon_client.invalidate_token("dev1.dev.clover.com")

    # Verify delete was called
    mock_client.delete.assert_called_once()
