"""
Test the billing-event API via stolon.

This module tests the BillingEventDev mixin methods that use the generated
OpenAPI client for the billing-event service.
"""

import pytest

from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp
from tests.conftest import RunningStolonServer


@pytest.mark.external_infra
def test_billing_event_api(stolon_server: RunningStolonServer) -> None:
    """Test retrieving merchant acceptances from billing-event API."""
    # Use the stolon server's home so the client can find the port
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    # Test getting merchant acceptances
    # Using a known merchant UUID from dev environment
    merchant_uuid = "MSR15REPHS0N5"

    response = dev.get(f"/billing-event/v1/merchant/acceptances?merchantUuid={merchant_uuid}")

    # Verify we got a response back
    assert response is not None
    assert isinstance(response, dict)

    # The response should contain acceptances information
    # It should have a structure like a list or collection of acceptances
