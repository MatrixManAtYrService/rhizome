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
from typing import Any, cast

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.models.billing_bookkeeper.billing_entity import BillingEntity
from rhizome.models.billing_bookkeeper.billing_hierarchy import BillingHierarchy
from rhizome.models.billing_bookkeeper.billing_schedule import BillingSchedule
from rhizome.models.billing_bookkeeper.cellular_action_fee_code import CellularActionFeeCode
from rhizome.models.billing_bookkeeper.fee_rate import FeeRate
from rhizome.models.billing_bookkeeper.invoice_alliance_code import InvoiceAllianceCode
from rhizome.models.billing_bookkeeper.partner_config import PartnerConfig
from rhizome.models.billing_bookkeeper.plan_action_fee_code import PlanActionFeeCode
from rhizome.models.billing_bookkeeper.processing_group_dates import ProcessingGroupDates
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


def _print_curl(
    method: str, url: str, json_data: dict[str, Any] | None = None, token: str = "YOUR-INTERNAL-SESSION"
) -> None:
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


@pytest.fixture(scope="module")
def dev_bb() -> DevBillingBookkeeper:
    """Shared DevBillingBookkeeper instance for all tests in this module.

    This fixture creates a single rhizome client and billing bookkeeper environment
    that is reused across all tests, avoiding the overhead of setting up multiple
    port-forwards.

    Scope: module - one instance shared across all tests in this file.
    """
    rhizome_client = RhizomeClient(data_in_logs=False)
    return DevBillingBookkeeper(rhizome_client)


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
def billing_entity(
    stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing entity for testing.

    Uses rhizome to check if an MFF test reseller already exists.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    # First, check if an MFF reseller already exists using rhizome
    BillingEntityModel = cast(type[BillingEntity], dev_bb.get_model(BillingBookkeeperTable.billing_entity))

    # Query for any MFF reseller (sanitize=False to get real UUIDs for API calls)
    existing_entity = dev_bb.select_first(
        select(BillingEntityModel)
        .where(BillingEntityModel.entity_type == "RESELLER")
        .where(BillingEntityModel.entity_uuid.like("MFF%"))  # type: ignore[attr-defined]  # SQLModel columns have .like()
        .order_by(BillingEntityModel.created_timestamp.desc()),  # type: ignore[attr-defined]  # SQLModel columns have .desc()
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
        print("\n=== Trying to GET Billing Entity by entity UUID ===")
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
    print(
        f"\n⚠️  Note: Billing entity {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def alliance_code(
    billing_entity: dict[str, Any], stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
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
    InvoiceAllianceCodeModel = cast(
        type[InvoiceAllianceCode], dev_bb.get_model(BillingBookkeeperTable.invoice_alliance_code)
    )

    existing_alliance_code = dev_bb.select_first(
        select(InvoiceAllianceCodeModel).where(InvoiceAllianceCodeModel.billing_entity_uuid == billing_entity_uuid),
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
    print(
        f"\n⚠️  Note: Alliance code {alliance_code_value} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def billing_schedule(
    billing_entity: dict[str, Any], stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing schedule for testing.

    Checks if the billing entity already has a billing schedule.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if billing schedule already exists for this billing entity
    BillingScheduleModel = cast(type[BillingSchedule], dev_bb.get_model(BillingBookkeeperTable.billing_schedule))

    existing_schedule = dev_bb.select_first(
        select(BillingScheduleModel).where(BillingScheduleModel.billing_entity_uuid == billing_entity_uuid),
        sanitize=False,
    )

    if existing_schedule:
        print("\n♻️  Reusing existing billing schedule")
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
    print(
        f"\n⚠️  Note: Billing schedule for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def fee_rate(
    billing_entity: dict[str, Any], stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
    """Get or create a fee rate for testing.

    Checks if the billing entity already has a fee rate.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if fee rate already exists for this billing entity
    FeeRateModel = cast(type[FeeRate], dev_bb.get_model(BillingBookkeeperTable.fee_rate))

    existing_fee_rate = dev_bb.select_first(
        select(FeeRateModel)
        .where(FeeRateModel.billing_entity_uuid == billing_entity_uuid)
        .order_by(FeeRateModel.created_timestamp.desc()),  # type: ignore[attr-defined]  # SQLModel columns have .desc()
        sanitize=False,
    )

    if existing_fee_rate:
        print("\n♻️  Reusing existing fee rate")
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
    print(
        f"\n⚠️  Note: Fee rate for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def processing_group_dates(
    billing_entity: dict[str, Any], stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
    """Get or create processing group dates for testing.

    Checks if the billing entity already has processing group dates.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if processing group dates already exist for this billing entity
    ProcessingGroupDatesModel = cast(
        type[ProcessingGroupDates], dev_bb.get_model(BillingBookkeeperTable.processing_group_dates)
    )

    existing_pgd = dev_bb.select_first(
        select(ProcessingGroupDatesModel).where(ProcessingGroupDatesModel.billing_entity_uuid == billing_entity_uuid),
        sanitize=False,
    )

    if existing_pgd:
        print("\n♻️  Reusing existing processing group dates")
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
    print(
        f"\n⚠️  Note: Processing group dates for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def billing_hierarchy(
    billing_entity: dict[str, Any], stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
    """Get or create billing hierarchy entries for testing.

    Creates two hierarchy entries:
    1. MERCHANT_SCHEDULE - links to common parent hierarchy
    2. MERCHANT_FEE_RATE - links to common parent hierarchy

    Based on demo2 query results, uses common parent hierarchies that
    already exist in the environment.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Common parent hierarchies from demo2 query results
    MERCHANT_SCHEDULE_PARENT = "CP9EA77DEYD963ZK0AK1D0QN4P"
    MERCHANT_FEE_RATE_PARENT = "YHTEVVQ3CHKB15Q27VNQQDZHVJ"

    # Check if billing hierarchy entries already exist for this billing entity
    BillingHierarchyModel = cast(type[BillingHierarchy], dev_bb.get_model(BillingBookkeeperTable.billing_hierarchy))

    existing_schedule_hierarchy = dev_bb.select_first(
        select(BillingHierarchyModel)
        .where(BillingHierarchyModel.billing_entity_uuid == billing_entity_uuid)
        .where(BillingHierarchyModel.hierarchy_type == "MERCHANT_SCHEDULE"),
        sanitize=False,
    )

    existing_fee_rate_hierarchy = dev_bb.select_first(
        select(BillingHierarchyModel)
        .where(BillingHierarchyModel.billing_entity_uuid == billing_entity_uuid)
        .where(BillingHierarchyModel.hierarchy_type == "MERCHANT_FEE_RATE"),
        sanitize=False,
    )

    if existing_schedule_hierarchy and existing_fee_rate_hierarchy:
        print("\n♻️  Reusing existing billing hierarchies")
        print(f"    MERCHANT_SCHEDULE: {existing_schedule_hierarchy.uuid}")
        print(f"    MERCHANT_FEE_RATE: {existing_fee_rate_hierarchy.uuid}")
        print(f"    for billing_entity: {billing_entity_uuid}")

        yield {
            "billing_entity_uuid": billing_entity_uuid,
            "merchant_schedule_uuid": existing_schedule_hierarchy.uuid,
            "merchant_fee_rate_uuid": existing_fee_rate_hierarchy.uuid,
            "was_reused": True,
        }
        return

    # Need to create one or both hierarchy entries
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)
    effective_date = _get_future_date(days_ahead=30)

    created_schedule_uuid = None
    created_fee_rate_uuid = None

    if not existing_schedule_hierarchy:
        print("\n=== Creating New MERCHANT_SCHEDULE Billing Hierarchy ===")

        json_data = {
            "billingEntityUuid": billing_entity_uuid,
            "hierarchyType": "MERCHANT_SCHEDULE",
            "effectiveDate": effective_date,
            "parentBillingHierarchyUuid": MERCHANT_SCHEDULE_PARENT,
        }

        _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/hierarchy", json_data)

        schedule_response = dev.post("/billing-bookkeeper/v1/hierarchy", json=json_data)
        created_schedule_uuid = schedule_response.get("uuid")
        print(f"✓ Created MERCHANT_SCHEDULE hierarchy: {created_schedule_uuid}")
    else:
        created_schedule_uuid = existing_schedule_hierarchy.uuid
        print(f"\n♻️  Reusing existing MERCHANT_SCHEDULE hierarchy: {created_schedule_uuid}")

    if not existing_fee_rate_hierarchy:
        print("\n=== Creating New MERCHANT_FEE_RATE Billing Hierarchy ===")

        json_data = {
            "billingEntityUuid": billing_entity_uuid,
            "hierarchyType": "MERCHANT_FEE_RATE",
            "effectiveDate": effective_date,
            "parentBillingHierarchyUuid": MERCHANT_FEE_RATE_PARENT,
        }

        _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/hierarchy", json_data)

        fee_rate_response = dev.post("/billing-bookkeeper/v1/hierarchy", json=json_data)
        created_fee_rate_uuid = fee_rate_response.get("uuid")
        print(f"✓ Created MERCHANT_FEE_RATE hierarchy: {created_fee_rate_uuid}")
    else:
        created_fee_rate_uuid = existing_fee_rate_hierarchy.uuid
        print(f"\n♻️  Reusing existing MERCHANT_FEE_RATE hierarchy: {created_fee_rate_uuid}")

    yield {
        "billing_entity_uuid": billing_entity_uuid,
        "merchant_schedule_uuid": created_schedule_uuid,
        "merchant_fee_rate_uuid": created_fee_rate_uuid,
        "was_reused": False,
    }

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Billing hierarchies for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def partner_config(
    billing_entity: dict[str, Any], stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
    """Get or create a partner config for testing.

    Checks if the billing entity already has a partner config for MERCHANT_SCHEDULE.
    If found, reuses it. Otherwise, creates a new one.

    Partner config is required for resellers to process invoices and settlements.

    Scope: module - reuse across all tests in this module.
    """
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if partner config already exists for this billing entity
    PartnerConfigModel = cast(type[PartnerConfig], dev_bb.get_model(BillingBookkeeperTable.partner_config))

    existing_partner_config = dev_bb.select_first(
        select(PartnerConfigModel)
        .where(PartnerConfigModel.billing_entity_uuid == billing_entity_uuid)
        .where(PartnerConfigModel.hierarchy_type == "MERCHANT_SCHEDULE"),
        sanitize=False,
    )

    if existing_partner_config:
        print("\n♻️  Reusing existing partner config")
        print(f"    settlement_method: {existing_partner_config.settlement_method}")
        print(f"    revenue_share_group: {existing_partner_config.revenue_share_group}")
        print(f"    for billing_entity: {billing_entity_uuid}")

        yield {
            "billing_entity_uuid": billing_entity_uuid,
            "create_response": {"uuid": existing_partner_config.uuid},
            "was_reused": True,
        }
        return

    # No existing partner config found, create a new one
    print("\n=== Creating New Partner Config ===")

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    effective_date = _get_future_date(days_ahead=30)

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "effectiveDate": effective_date,
        "hierarchyType": "MERCHANT_SCHEDULE",
        "settlementMethod": "Goleo",
        "revenueShareGroup": "Default",
        "postMethod": "PerCycle",
        "invoiceMethod": "ResellerDetail",
        "invoiceNumberFormat": "AllianceCode",
    }

    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/partnerconfig", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/partnerconfig", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Partner config for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def plan_action_fee_code(
    stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
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
    PlanActionFeeCodeModel = cast(
        type[PlanActionFeeCode], dev_bb.get_model(BillingBookkeeperTable.plan_action_fee_code)
    )

    existing_plan_action_fee_code = dev_bb.select_first(
        select(PlanActionFeeCodeModel)
        .where(PlanActionFeeCodeModel.merchant_plan_uuid == test_plan_uuid)
        .where(PlanActionFeeCodeModel.plan_action_type == "PLAN_ASSIGN")
        .where(PlanActionFeeCodeModel.fee_category == "PLAN_RETAIL")
        .where(PlanActionFeeCodeModel.fee_code == "PaymentsPDVT.PRC"),
        sanitize=False,
    )

    if existing_plan_action_fee_code:
        print("\n♻️  Reusing existing plan action fee code (GLOBAL)")
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
    print(
        "\n⚠️  Note: Plan action fee codes are global configurations and cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def cellular_action_fee_code(
    stolon_server: RunningStolonServer, dev_bb: DevBillingBookkeeper
) -> Generator[dict[str, Any], None, None]:
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
    CellularActionFeeCodeModel = cast(
        type[CellularActionFeeCode], dev_bb.get_model(BillingBookkeeperTable.cellular_action_fee_code)
    )

    existing_cellular_action_fee_code = dev_bb.select_first(
        select(CellularActionFeeCodeModel)
        .where(CellularActionFeeCodeModel.carrier == carrier)
        .where(CellularActionFeeCodeModel.cellular_action_type == cellular_action_type)
        .where(CellularActionFeeCodeModel.fee_category == "CELLULAR_RETAIL")
        .where(CellularActionFeeCodeModel.fee_code == "CellularArr.ATT"),
        sanitize=False,
    )

    if existing_cellular_action_fee_code:
        print("\n♻️  Reusing existing cellular action fee code (GLOBAL)")
        print(
            f"    {existing_cellular_action_fee_code.carrier}/"
            f"{existing_cellular_action_fee_code.cellular_action_type}"
        )
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
    print(
        "\n⚠️  Note: Cellular action fee codes are global configurations and cannot be automatically deleted "
        "(API does not support DELETE)"
    )


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
    assert entity_uuid.startswith("MFF") or entity_uuid.startswith(
        "Hash"
    ), f"Unexpected entity_uuid format: {entity_uuid}"
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


@pytest.mark.external_infra
def test_create_billing_hierarchy(billing_hierarchy: dict[str, Any]) -> None:
    """Test creating billing hierarchy entries (depends on billing_entity)."""
    assert billing_hierarchy["billing_entity_uuid"]
    assert billing_hierarchy["merchant_schedule_uuid"]
    assert billing_hierarchy["merchant_fee_rate_uuid"]
    # Both UUIDs should be 26 characters
    assert len(billing_hierarchy["merchant_schedule_uuid"]) == 26
    assert len(billing_hierarchy["merchant_fee_rate_uuid"]) == 26


@pytest.mark.external_infra
def test_create_partner_config(partner_config: dict[str, Any]) -> None:
    """Test creating a partner config (depends on billing_entity)."""
    assert partner_config["billing_entity_uuid"]
    assert partner_config["create_response"]
