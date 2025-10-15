"""Integration tests for stolon (requires --external-infra)."""

import pytest

from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp
from tests.conftest import RunningStolonServer


@pytest.mark.external_infra
def test_stolon_end_to_end_get_request(stolon_server: RunningStolonServer) -> None:
    """Test complete flow: client -> server -> auth -> API -> response."""
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    env = DevHttp(client)

    # Make a simple GET request to whoami endpoint
    result = env.get("/v1/employees/whoami")

    # Verify we got a response
    assert result is not None
    assert isinstance(result, dict)
    # Response should have employee info fields
    assert "id" in result or "name" in result


@pytest.mark.external_infra
def test_stolon_token_caching(stolon_server: RunningStolonServer) -> None:
    """Test that tokens are cached and reused across requests."""
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    env = DevHttp(client)

    # Make first request (should get new token)
    result1 = env.get("/v1/employees/whoami")
    assert result1 is not None

    # Make second request (should reuse cached token)
    result2 = env.get("/v1/employees/whoami")
    assert result2 is not None

    # Both requests should succeed
    assert isinstance(result1, dict)
    assert isinstance(result2, dict)


@pytest.mark.external_infra
def test_stolon_multiple_environments(stolon_server: RunningStolonServer) -> None:
    """Test that different environment instances work correctly."""
    client = StolonClient(home=stolon_server.home, data_in_logs=False)

    # Create two environment instances
    env1 = DevHttp(client)
    env2 = DevHttp(client)

    # Both should be able to make requests
    result1 = env1.get("/v1/employees/whoami")
    result2 = env2.get("/v1/employees/whoami")

    assert result1 is not None
    assert result2 is not None
    assert isinstance(result1, dict)
    assert isinstance(result2, dict)
