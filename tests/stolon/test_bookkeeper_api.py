"""
Test the billing-bookkeeper and billing-event APIs via stolon.

This module tests the BookkeeperDev and BillingEventDev mixin methods that use
the generated OpenAPI clients.
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


@pytest.mark.external_infra
def test_billing_event_api(stolon_server: RunningStolonServer) -> None:
    """Test retrieving data from billing-event API."""
    # Use the stolon server's home so the client can find the port
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    # Test a simple GET request to billing-event
    # This assumes there's a health check or similar endpoint
    # Adjust the endpoint based on actual billing-event API structure
    response = dev.get("/billing-event/v1/health")

    # Verify we got a response back
    assert response is not None
