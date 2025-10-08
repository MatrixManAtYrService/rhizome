"""
Test the user-facing API for stolon environments.

This module tests the API patterns that allow users to make authenticated
HTTP requests to Clover APIs without needing to manage tokens directly.

Tests for reseller creation follow a bottom-up approach:
1. Leaf node tests create/delete individual resources
2. Composite tests build up the dependency tree
3. Final test creates a complete reseller hierarchy

Test data should align with demo2 environment structure where possible.
"""

import pytest

from tests.conftest import RunningStolonServer


@pytest.mark.external_infra
def test_get_merchant_name_from_dev1(stolon_server: RunningStolonServer) -> None:
    """Test retrieving merchant name from dev environment."""
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    # Use the stolon server's home so the client can find the port
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)
    name = dev.get_merchant_name("MSR15REPHS0N5")

    # Verify we got a name back
    assert name
    assert isinstance(name, str)


# --- Leaf Node Tests: Create and Delete Individual Resources ---
# These tests verify we can create the basic building blocks needed for a reseller.
# Data structure should match demo2 environment patterns.


@pytest.mark.external_infra
def test_create_delete_revenue_share_group(revenue_share_group: dict) -> None:
    """Test creating and deleting a revenue share group.

    Revenue share groups define how revenue is split between partners.
    Aligned with demo2 EMS revenue share group structure.
    """
    # Verify creation response
    create_response = revenue_share_group["create_response"]
    assert "uuid" in create_response or create_response.get("status") == "success"


@pytest.mark.external_infra
def test_create_delete_billing_entity(billing_entity: dict) -> None:
    """Test creating and deleting a billing entity.

    Billing entities represent resellers, merchants, or archetypes in the billing system.
    Aligned with demo2 EMS/Netherlands Support reseller patterns.
    """
    # Verify creation response
    create_response = billing_entity["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response

    # Verify billing entity UUID is 26 characters (server-generated)
    billing_entity_uuid = billing_entity["billing_entity_uuid"]
    assert billing_entity_uuid
    assert len(billing_entity_uuid) == 26


@pytest.mark.external_infra
def test_create_delete_alliance_code(alliance_code: dict) -> None:
    """Test creating and deleting an alliance code.

    Alliance codes are used for invoice numbering.
    Aligned with demo2 reseller alliance code patterns.
    """
    # Verify creation response
    create_response = alliance_code["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response


@pytest.mark.external_infra
def test_create_delete_billing_schedule(billing_schedule: dict) -> None:
    """Test creating and deleting a billing schedule.

    Billing schedules define when and how often bills are generated.
    Aligned with demo2 EMS/Netherlands Support billing schedule patterns.
    """
    # Verify creation response
    create_response = billing_schedule["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response


@pytest.mark.external_infra
def test_create_delete_fee_rate(fee_rate: dict) -> None:
    """Test creating and deleting a fee rate.

    Fee rates define pricing for various services (plans, devices, cellular, etc.)
    Aligned with demo2 reseller fee rate patterns.
    """
    # Verify creation response
    create_response = fee_rate["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response


@pytest.mark.external_infra
def test_create_delete_processing_group_dates(processing_group_dates: dict) -> None:
    """Test creating and deleting processing group dates.

    Processing group dates define billing cycle, posting, and settlement dates.
    Aligned with demo2 reseller processing group date patterns.
    """
    # Verify creation response
    create_response = processing_group_dates["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response


@pytest.mark.external_infra
def test_create_delete_plan_action_fee_code(plan_action_fee_code: dict) -> None:
    """Test creating and deleting a plan action fee code mapping.

    Plan action fee codes map merchant plan actions (assign, unassign, etc.) to fee codes.
    These are global configurations, not specific to a reseller.
    Aligned with demo2 plan action fee code patterns.
    """
    # Verify creation response
    create_response = plan_action_fee_code["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response


@pytest.mark.external_infra
def test_create_delete_cellular_action_fee_code(cellular_action_fee_code: dict) -> None:
    """Test creating and deleting a cellular action fee code mapping.

    Cellular action fee codes map cellular service actions to fee codes.
    These are global configurations, not specific to a reseller.
    Aligned with demo2 cellular action fee code patterns.
    """
    # Verify creation response
    create_response = cellular_action_fee_code["create_response"]
    assert create_response.get("status") == "success" or "uuid" in create_response
