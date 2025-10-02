"""
Test the billing-bookkeeper API via stolon.

This module tests the BookkeeperDev mixin methods that use the generated
OpenAPI client for the billing-bookkeeper service.
"""

import pytest

from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp
from tests.conftest import RunningStolonServer


@pytest.mark.external_infra
def test_get_billing_entity(stolon_server: RunningStolonServer) -> None:
    """Test retrieving a billing entity from billing-bookkeeper API."""
    # Use the stolon server's home so the client can find the port
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    # Test getting a billing entity by entity UUID
    # Using a known test entity UUID from dev environment
    entity_uuid = "CQ81XSCG2WGW5"

    response = dev.get(f"/billing-bookkeeper/v1/entity/entityuuid/{entity_uuid}")

    # Verify we got a response back
    assert response is not None
    assert isinstance(response, dict)

    # The response should contain entity information
    # Based on the curl examples in create_reseller.md, we expect fields like:
    # - billingEntityUuid
    # - entityUuid
    # - entityType (e.g., "RESELLER")
    # - name (e.g., "Netherlands Support")
    if "billingEntityUuid" in response:
        assert response["billingEntityUuid"]
        assert response["entityUuid"] == entity_uuid
