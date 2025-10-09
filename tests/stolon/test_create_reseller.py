"""
Test reseller creation using individual fixture-based approach.

This module demonstrates creating individual billing components using
separate pytest fixtures, following the curl command examples from
create_reseller.md documentation.

Strategy: Check if test resources already exist and reuse them to avoid
accumulating test data. Only revenue_share_group supports DELETE, so all
other resources are reused when found.

Note: Resources cannot be cleaned up (DELETE not supported for most
billing-bookkeeper endpoints), so we reuse existing MFF test resources.
"""

from collections.abc import Generator
from datetime import datetime, timedelta
from typing import Any

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.models.table_list import BillingBookkeeperTable
from tests.conftest import RunningStolonServer


def _get_future_date(days_ahead: int = 30) -> str:
    """Get a future date in YYYY-MM-DD format.

    Args:
        days_ahead: Number of days in the future (default: 30)

    Returns:
        Date string in YYYY-MM-DD format
    """
    future_date = datetime.now() + timedelta(days=days_ahead)
    return future_date.strftime("%Y-%m-%d")


def _print_curl(method: str, url: str, json_data: dict[str, Any] | None = None, token: str = "YOUR-INTERNAL-SESSION") -> None:
    """Print a curl command for manual recreation."""
    import json as json_module

    curl_parts = [
        "curl",
        "-X",
        f"'{method.upper()}'",
        f"'{url}'",
        "--header 'x-clover-appenv: dev1'",
        f"--header 'Cookie: internalSession={token}'",
        "--header 'Content-Type: application/json'",
    ]

    if json_data:
        json_str = json_module.dumps(json_data, indent=2)
        curl_parts.append(f"--data '{json_str}'")

    print("\n" + " \\\n".join(curl_parts) + "\n")


@pytest.fixture
def revenue_share_group(stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Create and cleanup a revenue share group for testing."""
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    # Create revenue share group with MFF prefix
    group_name = f"MFF_Test_{uuid.uuid4().hex[:4]}"
    short_desc = f"MFF-{group_name}"
    description = f"The FirstData/Fiserv reseller in EMEA for {group_name}"

    json_data = {"revenueShareGroup": group_name, "shortDesc": short_desc, "description": description}

    print("\n=== Creating Revenue Share Group ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/revsharegroup", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/revsharegroup", json=json_data)
    group_uuid = create_response.get("uuid")

    yield {"name": group_name, "uuid": group_uuid, "create_response": create_response}

    # Cleanup: Delete the revenue share group
    if group_uuid:
        try:
            print(f"\n🗑️  Deleting revenue share group {group_uuid}")
            dev.delete(f"/billing-bookkeeper/v1/revsharegroup/{group_uuid}")
            print("✅ Cleanup successful")
        except Exception as e:
            print(f"⚠️  Cleanup failed: {e}")


@pytest.fixture(scope="module")
def billing_entity(stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing entity for testing.

    Uses rhizome to check if an MFF test reseller already exists.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    # First, check if an MFF reseller already exists using rhizome
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    BillingEntity = dev_bb.get_model(BillingBookkeeperTable.billing_entity)

    # Query for any MFF reseller (sanitize=False to get real UUIDs for API calls)
    existing_entity = dev_bb.select_first(
        select(BillingEntity)
        .where(BillingEntity.entity_type == "RESELLER")
        .where(BillingEntity.entity_uuid.like("MFF%"))
        .order_by(BillingEntity.created_timestamp.desc()),
        sanitize=False,
    )

    if existing_entity:
        print(f"\n♻️  Reusing existing MFF reseller: {existing_entity.name}")
        print(f"    billing_entity_uuid: {existing_entity.uuid}")
        print(f"    entity_uuid: {existing_entity.entity_uuid}")

        yield {
            "entity_uuid": existing_entity.entity_uuid,
            "billing_entity_uuid": existing_entity.uuid,
            "name": existing_entity.name,
            "create_response": {"uuid": existing_entity.uuid},  # Fake response for compatibility
            "was_reused": True,
        }
        return

    # No existing entity found, create a new one
    print("\n=== Creating New Billing Entity ===")

    stolon_client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(stolon_client)

    # Generate unique 13-char entity UUID
    entity_uuid = f"MFF{uuid.uuid4().hex[:10].upper()}"
    entity_name = f"MFF Test Reseller {entity_uuid[-4:]}"

    json_data = {"entityUuid": entity_uuid, "entityType": "RESELLER", "name": entity_name}

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/entity", json_data)

    # Create billing entity
    create_response = dev.post("/billing-bookkeeper/v1/entity", json=json_data)

    # Extract server-generated billing entity UUID from response
    billing_entity_uuid = create_response.get("uuid")

    if not billing_entity_uuid:
        # Fallback: try to get it via GET (though this seems to 404 in dev1)
        print(f"\n⚠️  Response did not contain uuid field. Response: {create_response}")
        print(f"\n=== Trying to GET Billing Entity by entity UUID ===")
        _print_curl("GET", f"https://dev1.dev.clover.com/billing-bookkeeper/v1/entity/entity/{entity_uuid}")
        entity_get = dev.get(f"/billing-bookkeeper/v1/entity/entity/{entity_uuid}")
        billing_entity_uuid = entity_get.get("uuid")

    print(f"\n✓ Server-generated billing_entity_uuid: {billing_entity_uuid}")

    yield {
        "entity_uuid": entity_uuid,
        "billing_entity_uuid": billing_entity_uuid,
        "name": entity_name,
        "create_response": create_response,
        "was_reused": False,
    }

    # Cleanup not supported - DELETE method returns 405
    print(f"\n⚠️  Note: Billing entity {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def alliance_code(billing_entity: dict[str, Any], stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create an alliance code for testing.

    Checks if the billing entity already has an alliance code.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if alliance code already exists for this billing entity
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    InvoiceAllianceCode = dev_bb.get_model(BillingBookkeeperTable.invoice_alliance_code)

    existing_alliance_code = dev_bb.select_first(
        select(InvoiceAllianceCode).where(InvoiceAllianceCode.billing_entity_uuid == billing_entity_uuid),
        sanitize=False,
    )

    if existing_alliance_code:
        print(f"\n♻️  Reusing existing alliance code: {existing_alliance_code.alliance_code}")
        print(f"    for billing_entity: {billing_entity_uuid}")

        yield {
            "alliance_code": existing_alliance_code.alliance_code,
            "billing_entity_uuid": billing_entity_uuid,
            "create_response": {"uuid": existing_alliance_code.uuid},
            "was_reused": True,
        }
        return

    # No existing alliance code found, create a new one
    print("\n=== Creating New Alliance Code ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    alliance_code_value = f"9{uuid.uuid4().hex[:2].upper()}"

    json_data = {"billingEntityUuid": billing_entity_uuid, "allianceCode": alliance_code_value, "invoiceCount": 1}

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/alliancecode", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/alliancecode", json=json_data)

    yield {
        "alliance_code": alliance_code_value,
        "billing_entity_uuid": billing_entity_uuid,
        "create_response": create_response,
        "was_reused": False,
    }

    # Cleanup not supported - DELETE method returns 405
    print(f"\n⚠️  Note: Alliance code {alliance_code_value} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def billing_schedule(billing_entity: dict[str, Any], stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing schedule for testing.

    Checks if the billing entity already has a billing schedule.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if billing schedule already exists for this billing entity
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    BillingSchedule = dev_bb.get_model(BillingBookkeeperTable.billing_schedule)

    existing_schedule = dev_bb.select_first(
        select(BillingSchedule).where(BillingSchedule.billing_entity_uuid == billing_entity_uuid), sanitize=False
    )

    if existing_schedule:
        print(f"\n♻️  Reusing existing billing schedule")
        print(f"    currency: {existing_schedule.default_currency}, frequency: {existing_schedule.frequency}")
        print(f"    for billing_entity: {billing_entity_uuid}")

        yield {
            "billing_entity_uuid": billing_entity_uuid,
            "create_response": {"uuid": existing_schedule.uuid},
            "was_reused": True,
        }
        return

    # No existing billing schedule found, create a new one
    print("\n=== Creating New Billing Schedule ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    effective_date = _get_future_date(days_ahead=30)
    next_billing_date = _get_future_date(days_ahead=60)

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "effectiveDate": effective_date,
        "frequency": "MONTHLY",
        "billingDay": 1,
        "nextBillingDate": next_billing_date,
        "unitsInNextPeriod": 31,
        "defaultCurrency": "EUR",
    }

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/schedule", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/schedule", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(f"\n⚠️  Note: Billing schedule for {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def fee_rate(billing_entity: dict[str, Any], stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create a fee rate for testing.

    Checks if the billing entity already has a fee rate.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if fee rate already exists for this billing entity
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    FeeRate = dev_bb.get_model(BillingBookkeeperTable.fee_rate)

    existing_fee_rate = dev_bb.select_first(
        select(FeeRate).where(FeeRate.billing_entity_uuid == billing_entity_uuid).order_by(FeeRate.created_timestamp.desc()),
        sanitize=False,
    )

    if existing_fee_rate:
        print(f"\n♻️  Reusing existing fee rate")
        print(f"    {existing_fee_rate.fee_category}/{existing_fee_rate.fee_code}")
        print(f"    for billing_entity: {billing_entity_uuid}")

        yield {
            "billing_entity_uuid": billing_entity_uuid,
            "create_response": {"uuid": existing_fee_rate.uuid},
            "was_reused": True,
        }
        return

    # No existing fee rate found, create a new one
    print("\n=== Creating New Fee Rate ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    effective_date = _get_future_date(days_ahead=30)

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "feeCategory": "PLAN_RETAIL",
        "feeCode": "PaymentsPDVT",
        "currency": "EUR",
        "effectiveDate": effective_date,
        "applyType": "DEFAULT",
        "perItemAmount": 0.0,
    }

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/rate", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/rate", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(f"\n⚠️  Note: Fee rate for {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def processing_group_dates(billing_entity: dict[str, Any], stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create processing group dates for testing.

    Checks if the billing entity already has processing group dates.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if processing group dates already exist for this billing entity
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    ProcessingGroupDates = dev_bb.get_model(BillingBookkeeperTable.processing_group_dates)

    existing_pgd = dev_bb.select_first(
        select(ProcessingGroupDates).where(ProcessingGroupDates.billing_entity_uuid == billing_entity_uuid),
        sanitize=False,
    )

    if existing_pgd:
        print(f"\n♻️  Reusing existing processing group dates")
        print(f"    hierarchy_type: {existing_pgd.hierarchy_type}")
        print(f"    for billing_entity: {billing_entity_uuid}")

        yield {
            "billing_entity_uuid": billing_entity_uuid,
            "create_response": {"uuid": existing_pgd.uuid},
            "was_reused": True,
        }
        return

    # No existing processing group dates found, create new ones
    print("\n=== Creating New Processing Group Dates ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    cycle_date = _get_future_date(days_ahead=30)

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "hierarchyType": "MERCHANT_SCHEDULE",
        "cycleDate": cycle_date,
        "postingDate": cycle_date,
        "billingDate": cycle_date,
        "settlementDate": cycle_date,
    }

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/processgroupdates", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/processgroupdates", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(f"\n⚠️  Note: Processing group dates for {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def plan_action_fee_code(stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create a plan action fee code for testing.

    Plan action fee codes are GLOBAL resources (not tied to billing entity).
    Always checks if one exists before creating.

    Scope: module - reuse across all tests in this module.
    """
    import httpx

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    test_plan_uuid = "YEQMV17H09HHW"

    # Check if plan action fee code already exists (global resource)
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    PlanActionFeeCode = dev_bb.get_model(BillingBookkeeperTable.plan_action_fee_code)

    existing_plan_action_fee_code = dev_bb.select_first(
        select(PlanActionFeeCode)
        .where(PlanActionFeeCode.merchant_plan_uuid == test_plan_uuid)
        .where(PlanActionFeeCode.plan_action_type == "PLAN_ASSIGN")
        .where(PlanActionFeeCode.fee_category == "PLAN_RETAIL")
        .where(PlanActionFeeCode.fee_code == "PaymentsPDVT.PRC"),
        sanitize=False,
    )

    if existing_plan_action_fee_code:
        print(f"\n♻️  Reusing existing plan action fee code (GLOBAL)")
        print(f"    {existing_plan_action_fee_code.fee_category}/{existing_plan_action_fee_code.fee_code}")
        print(f"    plan_uuid: {test_plan_uuid}")

        yield {
            "merchant_plan_uuid": test_plan_uuid,
            "create_response": {"uuid": existing_plan_action_fee_code.uuid},
            "was_reused": True,
        }
        return

    # No existing plan action fee code found, create a new one
    print("\n=== Creating New Plan Action Fee Code (GLOBAL) ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    effective_date = _get_future_date(days_ahead=30)

    json_data = {
        "merchantPlanUuid": test_plan_uuid,
        "planActionType": "PLAN_ASSIGN",
        "effectiveDate": effective_date,
        "feeCategory": "PLAN_RETAIL",
        "feeCode": "PaymentsPDVT.PRC",
    }

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/planactionfeecode", json_data)

    try:
        create_response = dev.post("/billing-bookkeeper/v1/planactionfeecode", json=json_data)
    except httpx.HTTPStatusError as e:
        print(f"\n⚠️  API Error Response: {e.response.text}")
        print(f"⚠️  Status Code: {e.response.status_code}")
        raise

    yield {"merchant_plan_uuid": test_plan_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print("\n⚠️  Note: Plan action fee codes are global configurations and cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def cellular_action_fee_code(stolon_server: RunningStolonServer) -> Generator[dict[str, Any], None, None]:
    """Get or create a cellular action fee code for testing.

    Cellular action fee codes are GLOBAL resources (not tied to billing entity).
    Always checks if one exists before creating.

    Based on query results, we know AT&T/CELLULAR_ARREARS already exists in dev1,
    so this will always reuse the existing one.

    Scope: module - reuse across all tests in this module.
    """
    import httpx

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    carrier = "AT&T"
    cellular_action_type = "CELLULAR_ARREARS"

    # Check if cellular action fee code already exists (global resource)
    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    CellularActionFeeCode = dev_bb.get_model(BillingBookkeeperTable.cellular_action_fee_code)

    existing_cellular_action_fee_code = dev_bb.select_first(
        select(CellularActionFeeCode)
        .where(CellularActionFeeCode.carrier == carrier)
        .where(CellularActionFeeCode.cellular_action_type == cellular_action_type)
        .where(CellularActionFeeCode.fee_category == "CELLULAR_RETAIL")
        .where(CellularActionFeeCode.fee_code == "CellularArr.ATT"),
        sanitize=False,
    )

    if existing_cellular_action_fee_code:
        print(f"\n♻️  Reusing existing cellular action fee code (GLOBAL)")
        print(f"    {existing_cellular_action_fee_code.carrier}/{existing_cellular_action_fee_code.cellular_action_type}")
        print(f"    {existing_cellular_action_fee_code.fee_category}/{existing_cellular_action_fee_code.fee_code}")

        yield {
            "carrier": carrier,
            "create_response": {"uuid": existing_cellular_action_fee_code.uuid},
            "was_reused": True,
        }
        return

    # No existing cellular action fee code found, create a new one
    print("\n=== Creating New Cellular Action Fee Code (GLOBAL) ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    effective_date = _get_future_date(days_ahead=30)

    json_data = {
        "carrier": carrier,
        "cellularActionType": cellular_action_type,
        "effectiveDate": effective_date,
        "feeCategory": "CELLULAR_RETAIL",
        "feeCode": "CellularArr.ATT",
    }

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/cellularactionfeecode", json_data)

    try:
        create_response = dev.post("/billing-bookkeeper/v1/cellularactionfeecode", json=json_data)
    except httpx.HTTPStatusError as e:
        print(f"\n⚠️  API Error Response: {e.response.text}")
        print(f"⚠️  Status Code: {e.response.status_code}")
        raise

    yield {"carrier": carrier, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print("\n⚠️  Note: Cellular action fee codes are global configurations and cannot be automatically deleted (API does not support DELETE)")


# ============================================================================
# Tests
# ============================================================================


@pytest.mark.external_infra
def test_create_revenue_share_group(revenue_share_group: dict[str, Any]) -> None:
    """Test creating a revenue share group."""
    assert revenue_share_group["name"].startswith("MFF_Test_")
    assert revenue_share_group["uuid"]
    assert len(revenue_share_group["uuid"]) == 26


@pytest.mark.external_infra
def test_create_billing_entity(billing_entity: dict[str, Any]) -> None:
    """Test creating a billing entity."""
    # entity_uuid might be masked (starts with "Hash") or real (starts with "MFF")
    entity_uuid = billing_entity["entity_uuid"]
    assert entity_uuid.startswith("MFF") or entity_uuid.startswith("Hash"), f"Unexpected entity_uuid format: {entity_uuid}"
    assert billing_entity["billing_entity_uuid"]
    # billing_entity_uuid might be masked or real (both are 26 chars)
    assert len(billing_entity["billing_entity_uuid"]) == 26


@pytest.mark.external_infra
def test_create_alliance_code(alliance_code: dict[str, Any]) -> None:
    """Test creating an alliance code (depends on billing_entity)."""
    assert alliance_code["alliance_code"].startswith("9")
    assert len(alliance_code["alliance_code"]) == 3
    assert alliance_code["billing_entity_uuid"]


@pytest.mark.external_infra
def test_create_billing_schedule(billing_schedule: dict[str, Any]) -> None:
    """Test creating a billing schedule (depends on billing_entity)."""
    assert billing_schedule["billing_entity_uuid"]
    assert billing_schedule["create_response"]


@pytest.mark.external_infra
def test_create_fee_rate(fee_rate: dict[str, Any]) -> None:
    """Test creating a fee rate (depends on billing_entity)."""
    assert fee_rate["billing_entity_uuid"]
    assert fee_rate["create_response"]


@pytest.mark.external_infra
def test_create_processing_group_dates(processing_group_dates: dict[str, Any]) -> None:
    """Test creating processing group dates (depends on billing_entity)."""
    assert processing_group_dates["billing_entity_uuid"]
    assert processing_group_dates["create_response"]


@pytest.mark.external_infra
def test_create_plan_action_fee_code(plan_action_fee_code: dict[str, Any]) -> None:
    """Test creating a plan action fee code."""
    assert plan_action_fee_code["merchant_plan_uuid"] == "YEQMV17H09HHW"
    assert plan_action_fee_code["create_response"]


@pytest.mark.external_infra
def test_create_cellular_action_fee_code(cellular_action_fee_code: dict[str, Any]) -> None:
    """Test creating a cellular action fee code."""
    assert cellular_action_fee_code["carrier"] == "AT&T"
    assert cellular_action_fee_code["create_response"]
