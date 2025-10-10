"""
Test reseller creation using individual fixture-based approach.

Strategy: Check if test resources already exist and reuse them to avoid
accumulating test data. Only revenue_share_group supports DELETE, so all
other resources are reused when found.

Note: Resources cannot be cleaned up (DELETE not supported for most
billing-bookkeeper endpoints), so we reuse existing MFF test resources.

This test uses the generated OpenAPI client for type-safe API calls.
Enable httpx debug logging with: pytest --log-cli-level=DEBUG
"""

import logging
import uuid as uuid_module
from collections.abc import Generator
from datetime import datetime, timedelta
from typing import Any, cast

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
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
from stolon.client import StolonClient
from tests.conftest import RunningStolonServer
from trifolium.environments import dev

# Enable httpx debug logging to see all HTTP requests
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.DEBUG)

# Framework identification prefix for all created resources
# ⚠️  CHANGING THIS PREFIX WILL CREATE NEW RESOURCES:
# - This prefix is applied to ALL resources created by this test framework:
#   * Billing entity entity_uuid: "{PREFIX}{index}" (e.g., "MFF9535862249")
#   * Alliance codes: "{PREFIX}{0001}" (e.g., "MFF0001", "MFF0002")
#   * Revenue share groups: "{PREFIX}_Test_{uuid}" (e.g., "MFF_Test_a1b2")
# - Changing this value (e.g., "MFF" -> "TEST") will cause the fixtures to create
#   NEW billing entities and supporting resources instead of reusing existing ones
# - This allows testing the full creation process from scratch
# - Resources CANNOT be deleted (API does not support DELETE), so they will accumulate in dev1
# - Use different prefixes to create separate test resellers (e.g., "TEST1", "TEST2")
# - Keep as "MFF" to reuse the existing shared test reseller
# - To find all framework-created resources, search for this prefix in:
#   * billing_entity.entity_uuid
#   * invoice_alliance_code.alliance_code
#   * revenue_share_group.revenue_share_group
RESELLER_PREFIX = "MFF"


def _get_future_date(days_ahead: int = 30) -> str:
    """Get a future date in YYYY-MM-DD format.

    Args:
        days_ahead: Number of days in the future (default: 30)

    Returns:
        Date string in YYYY-MM-DD format
    """
    future_date = datetime.now() + timedelta(days=days_ahead)
    return future_date.strftime("%Y-%m-%d")


@pytest.fixture(scope="module")
def environment(stolon_server: RunningStolonServer) -> dev.Dev:
    """Unified dev environment with both database and HTTP access.

    This fixture creates a single Dev instance that provides:
    - environment.db.billing_bookkeeper: Database queries via Rhizome
    - environment.api.billing_bookkeeper: HTTP API calls via Stolon (wrapped generated client)

    Scope: module - one instance shared across all tests in this file.
    """
    rhizome_client = RhizomeClient(data_in_logs=False)
    stolon_client = StolonClient(home=stolon_server.home, data_in_logs=False)
    return dev.Dev(rhizome_client=rhizome_client, stolon_client=stolon_client)


@pytest.fixture
def revenue_share_group(environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Create and cleanup a revenue share group for testing."""
    # Create revenue share group with reseller prefix
    group_name = f"{RESELLER_PREFIX}_Test_{uuid_module.uuid4().hex[:4]}"
    short_desc = f"{RESELLER_PREFIX}-{group_name}"
    description = f"The FirstData/Fiserv reseller in EMEA for {group_name}"

    print("\n=== Creating Revenue Share Group ===")
    created_group = environment.api.billing_bookkeeper.create_revenue_share_group(
        revenue_share_group_name=group_name,
        short_desc=short_desc,
        description=description,
    )

    group_uuid = created_group.get("uuid")

    yield {"name": group_name, "uuid": group_uuid, "create_response": created_group}

    # Cleanup: Delete the revenue share group
    if group_uuid:
        try:
            print(f"\n🗑️  Deleting revenue share group {group_uuid}")
            environment.api.billing_bookkeeper.delete_revenue_share_group(uuid=group_uuid)
            print("✅ Cleanup successful")
        except Exception as e:
            print(f"⚠️  Cleanup failed: {e}")


@pytest.fixture(scope="module")
def billing_entity(environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing entity for testing.

    Uses rhizome to check if a test reseller with RESELLER_PREFIX already exists.
    If found, reuses it. Otherwise, creates a new one using the generated API client.

    Scope: module - reuse across all tests in this module.
    """
    # First, check if a reseller with our prefix already exists using rhizome
    BillingEntityModel = cast(
        type[BillingEntity], environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.billing_entity)
    )

    # Query for any reseller with our prefix (sanitize=False to get real UUIDs for API calls)
    existing_entity = environment.db.billing_bookkeeper.select_first(
        select(BillingEntityModel)
        .where(BillingEntityModel.entity_type == "RESELLER")
        .where(BillingEntityModel.entity_uuid.like(f"{RESELLER_PREFIX}%"))  # type: ignore[attr-defined]  # SQLModel columns have .like()
        .order_by(BillingEntityModel.created_timestamp.desc()),  # type: ignore[attr-defined]  # SQLModel columns have .desc()
        sanitize=False,
    )

    if existing_entity:
        print(f"\n♻️  Reusing existing {RESELLER_PREFIX} reseller: {existing_entity.name}")
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

    # Generate unique 13-char entity UUID using prefix
    # UUID format: PREFIX + random hex (total 13 chars)
    remaining_chars = 13 - len(RESELLER_PREFIX)
    entity_uuid = f"{RESELLER_PREFIX}{uuid_module.uuid4().hex[:remaining_chars].upper()}"
    entity_name = f"{RESELLER_PREFIX} Test Reseller {entity_uuid[-4:]}"

    # Create using wrapped API
    created_entity = environment.api.billing_bookkeeper.create_entity(
        entity_uuid=entity_uuid,
        entity_type="RESELLER",
        name=entity_name,
    )

    billing_entity_uuid = created_entity.get("uuid")
    if not billing_entity_uuid:
        raise Exception(f"Response did not contain uuid field. Response: {created_entity}")

    print(f"\n✓ Server-generated billing_entity_uuid: {billing_entity_uuid}")

    yield {
        "entity_uuid": entity_uuid,
        "billing_entity_uuid": billing_entity_uuid,
        "name": entity_name,
        "create_response": created_entity,
        "was_reused": False,
    }

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Billing entity {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def alliance_code(billing_entity: dict[str, Any], environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create an alliance code for testing.

    Checks if the billing entity already has an alliance code.
    If found, reuses it. Otherwise, creates a new one with framework prefix + incremented number.

    Alliance codes use format: {RESELLER_PREFIX}{0000} (e.g., "MFF0001", "MFF0002")

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if alliance code already exists for this billing entity
    InvoiceAllianceCodeModel = cast(
        type[InvoiceAllianceCode],
        environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.invoice_alliance_code),
    )

    existing_alliance_code = environment.db.billing_bookkeeper.select_first(
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

    # Query for existing alliance codes with our prefix to find next available number
    # Alliance codes are 3 chars, so format: PREFIX + 4-digit padded number (e.g., "MFF0001")
    # We'll use the format that fits: if prefix is "MFF", result is "MFF0001" (7 chars total)
    existing_codes = environment.db.billing_bookkeeper.select_all(
        select(InvoiceAllianceCodeModel)
        .where(InvoiceAllianceCodeModel.alliance_code.like(f"{RESELLER_PREFIX}%"))  # type: ignore[attr-defined]
        .order_by(InvoiceAllianceCodeModel.alliance_code.desc()),  # type: ignore[attr-defined]
        sanitize=False,
    )

    # Find the highest number used
    max_num = 0
    for code_obj in existing_codes:
        code = code_obj.alliance_code
        # Extract numeric suffix after prefix
        numeric_part = code[len(RESELLER_PREFIX) :]
        if numeric_part.isdigit():
            max_num = max(max_num, int(numeric_part))

    # Increment to get next number
    next_num = max_num + 1

    # Format with 4 digits of padding (0001, 0002, ..., 9999)
    alliance_code_value = f"{RESELLER_PREFIX}{next_num:04d}"

    print(f"    Using alliance code: {alliance_code_value} (next after {max_num:04d})")

    create_response = environment.api.billing_bookkeeper.create_alliance_code(
        billing_entity_uuid=billing_entity_uuid,
        alliance_code_value=alliance_code_value,
        invoice_count=1,
    )

    yield {
        "alliance_code": alliance_code_value,
        "billing_entity_uuid": billing_entity_uuid,
        "create_response": create_response,
        "was_reused": False,
    }

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Alliance code {alliance_code_value} cannot be automatically deleted (API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def billing_schedule(billing_entity: dict[str, Any], environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing schedule for testing.

    Checks if the billing entity already has a billing schedule.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if billing schedule already exists for this billing entity
    BillingScheduleModel = cast(
        type[BillingSchedule], environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.billing_schedule)
    )

    existing_schedule = environment.db.billing_bookkeeper.select_first(
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

    effective_date = _get_future_date(days_ahead=30)
    next_billing_date = _get_future_date(days_ahead=60)

    create_response = environment.api.billing_bookkeeper.create_billing_schedule(
        billing_entity_uuid=billing_entity_uuid,
        effective_date=effective_date,
        frequency="MONTHLY",
        billing_day=1,
        next_billing_date=next_billing_date,
        units_in_next_period=31,
        default_currency="EUR",
    )

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Billing schedule for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def fee_rate(billing_entity: dict[str, Any], environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create a fee rate for testing.

    Checks if the billing entity already has a fee rate.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if fee rate already exists for this billing entity
    FeeRateModel = cast(type[FeeRate], environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.fee_rate))

    existing_fee_rate = environment.db.billing_bookkeeper.select_first(
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

    effective_date = _get_future_date(days_ahead=30)

    create_response = environment.api.billing_bookkeeper.create_fee_rate(
        billing_entity_uuid=billing_entity_uuid,
        fee_category="PLAN_RETAIL",
        fee_code="PaymentsPDVT",
        currency="EUR",
        effective_date=effective_date,
        apply_type="DEFAULT",
        per_item_amount=0.0,
    )

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Fee rate for {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def processing_group_dates(
    billing_entity: dict[str, Any], environment: dev.Dev
) -> Generator[dict[str, Any], None, None]:
    """Get or create processing group dates for testing.

    Checks if the billing entity already has processing group dates.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if processing group dates already exist for this billing entity
    ProcessingGroupDatesModel = cast(
        type[ProcessingGroupDates],
        environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.processing_group_dates),
    )

    existing_pgd = environment.db.billing_bookkeeper.select_first(
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

    cycle_date = _get_future_date(days_ahead=30)

    create_response = environment.api.billing_bookkeeper.create_processing_group_dates(
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type="MERCHANT_SCHEDULE",
        cycle_date=cycle_date,
        posting_date=cycle_date,
        billing_date=cycle_date,
        settlement_date=cycle_date,
    )

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Processing group dates for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def billing_hierarchy(billing_entity: dict[str, Any], environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create billing hierarchy entries for testing.

    Creates two hierarchy entries:
    1. MERCHANT_SCHEDULE - links to common parent hierarchy
    2. MERCHANT_FEE_RATE - links to common parent hierarchy

    Based on demo2 query results, uses common parent hierarchies that
    already exist in the environment.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Get the model first so we can use it in queries
    BillingHierarchyModel = cast(
        type[BillingHierarchy], environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.billing_hierarchy)
    )

    # Query for common parent hierarchies in dev1
    # Find the most commonly used parent hierarchies for each type
    merchant_schedule_parent = environment.db.billing_bookkeeper.select_first(
        select(BillingHierarchyModel.parent_billing_hierarchy_uuid)
        .where(BillingHierarchyModel.hierarchy_type == "MERCHANT_SCHEDULE")
        .where(BillingHierarchyModel.parent_billing_hierarchy_uuid.is_not(None))  # type: ignore[attr-defined]
        .limit(1),
        sanitize=False,
    )

    merchant_fee_rate_parent = environment.db.billing_bookkeeper.select_first(
        select(BillingHierarchyModel.parent_billing_hierarchy_uuid)
        .where(BillingHierarchyModel.hierarchy_type == "MERCHANT_FEE_RATE")
        .where(BillingHierarchyModel.parent_billing_hierarchy_uuid.is_not(None))  # type: ignore[attr-defined]
        .limit(1),
        sanitize=False,
    )

    if not merchant_schedule_parent or not merchant_fee_rate_parent:
        raise ValueError(
            "Could not find parent hierarchies in dev1. "
            "MERCHANT_SCHEDULE and MERCHANT_FEE_RATE parent hierarchies are required."
        )

    MERCHANT_SCHEDULE_PARENT = merchant_schedule_parent
    MERCHANT_FEE_RATE_PARENT = merchant_fee_rate_parent

    print("\n📋 Using parent hierarchies from dev1:")
    print(f"    MERCHANT_SCHEDULE parent: {MERCHANT_SCHEDULE_PARENT}")
    print(f"    MERCHANT_FEE_RATE parent: {MERCHANT_FEE_RATE_PARENT}")

    # Check if billing hierarchy entries already exist for this billing entity
    existing_schedule_hierarchy = environment.db.billing_bookkeeper.select_first(
        select(BillingHierarchyModel)
        .where(BillingHierarchyModel.billing_entity_uuid == billing_entity_uuid)
        .where(BillingHierarchyModel.hierarchy_type == "MERCHANT_SCHEDULE"),
        sanitize=False,
    )

    existing_fee_rate_hierarchy = environment.db.billing_bookkeeper.select_first(
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
    effective_date = _get_future_date(days_ahead=30)

    created_schedule_uuid = None
    created_fee_rate_uuid = None

    if not existing_schedule_hierarchy:
        print("\n=== Creating New MERCHANT_SCHEDULE Billing Hierarchy ===")

        schedule_response = environment.api.billing_bookkeeper.create_billing_hierarchy(
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type="MERCHANT_SCHEDULE",
            effective_date=effective_date,
            parent_billing_hierarchy_uuid=MERCHANT_SCHEDULE_PARENT,
        )
        created_schedule_uuid = schedule_response.get("uuid")
        print(f"✓ Created MERCHANT_SCHEDULE hierarchy: {created_schedule_uuid}")
    else:
        created_schedule_uuid = existing_schedule_hierarchy.uuid
        print(f"\n♻️  Reusing existing MERCHANT_SCHEDULE hierarchy: {created_schedule_uuid}")

    if not existing_fee_rate_hierarchy:
        print("\n=== Creating New MERCHANT_FEE_RATE Billing Hierarchy ===")

        fee_rate_response = environment.api.billing_bookkeeper.create_billing_hierarchy(
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type="MERCHANT_FEE_RATE",
            effective_date=effective_date,
            parent_billing_hierarchy_uuid=MERCHANT_FEE_RATE_PARENT,
        )
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
def partner_config(billing_entity: dict[str, Any], environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create a partner config for testing.

    Checks if the billing entity already has a partner config for MERCHANT_SCHEDULE.
    If found, reuses it. Otherwise, creates a new one.

    Partner config is required for resellers to process invoices and settlements.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if partner config already exists for this billing entity
    PartnerConfigModel = cast(
        type[PartnerConfig], environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.partner_config)
    )

    existing_partner_config = environment.db.billing_bookkeeper.select_first(
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

    effective_date = _get_future_date(days_ahead=30)

    # Use minimal config pattern based on Surega's MERCHANT_SCHEDULE configs in demo
    # Most MERCHANT_SCHEDULE configs only set settlementMethod and invoiceMethod
    create_response = environment.api.billing_bookkeeper.create_partner_config(
        billing_entity_uuid=billing_entity_uuid,
        effective_date=effective_date,
        hierarchy_type="MERCHANT_SCHEDULE",
        settlement_method="Goleo",
        invoice_method="MerchantDetail",
    )

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response, "was_reused": False}

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Partner config for {billing_entity_uuid} cannot be automatically deleted "
        "(API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def plan_action_fee_code(environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create a plan action fee code for testing.

    Plan action fee codes are GLOBAL resources (not tied to billing entity).
    Always checks if one exists before creating.

    Scope: module - reuse across all tests in this module.
    """
    import httpx

    test_plan_uuid = "YEQMV17H09HHW"

    # Check if plan action fee code already exists (global resource)
    PlanActionFeeCodeModel = cast(
        type[PlanActionFeeCode],
        environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.plan_action_fee_code),
    )

    existing_plan_action_fee_code = environment.db.billing_bookkeeper.select_first(
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

    effective_date = _get_future_date(days_ahead=30)

    try:
        create_response = environment.api.billing_bookkeeper.create_plan_action_fee_code(
            merchant_plan_uuid=test_plan_uuid,
            plan_action_type="PLAN_ASSIGN",
            effective_date=effective_date,
            fee_category="PLAN_RETAIL",
            fee_code="PaymentsPDVT.PRC",
        )
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
def cellular_action_fee_code(environment: dev.Dev) -> Generator[dict[str, Any], None, None]:
    """Get or create a cellular action fee code for testing.

    Cellular action fee codes are GLOBAL resources (not tied to billing entity).
    Always checks if one exists before creating.

    Based on query results, we know AT&T/CELLULAR_ARREARS already exists in dev1,
    so this will always reuse the existing one.

    Scope: module - reuse across all tests in this module.
    """
    import httpx

    carrier = "AT&T"
    cellular_action_type = "CELLULAR_ARREARS"

    # Check if cellular action fee code already exists (global resource)
    CellularActionFeeCodeModel = cast(
        type[CellularActionFeeCode],
        environment.db.billing_bookkeeper.get_model(BillingBookkeeperTable.cellular_action_fee_code),
    )

    existing_cellular_action_fee_code = environment.db.billing_bookkeeper.select_first(
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
            f"    {existing_cellular_action_fee_code.carrier}/{existing_cellular_action_fee_code.cellular_action_type}"
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

    effective_date = _get_future_date(days_ahead=30)

    try:
        create_response = environment.api.billing_bookkeeper.create_cellular_action_fee_code(
            carrier=carrier,
            cellular_action_type=cellular_action_type,
            effective_date=effective_date,
            fee_category="CELLULAR_RETAIL",
            fee_code="CellularArr.ATT",
        )
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
def test_create_complete_reseller(
    billing_entity: dict[str, Any],
    alliance_code: dict[str, Any],
    billing_schedule: dict[str, Any],
    fee_rate: dict[str, Any],
    processing_group_dates: dict[str, Any],
    billing_hierarchy: dict[str, Any],
    partner_config: dict[str, Any],
    plan_action_fee_code: dict[str, Any],
    cellular_action_fee_code: dict[str, Any],
) -> None:
    """Test creating a complete reseller with all required components.

    This test exercises all fixtures to ensure a complete reseller setup:
    - Billing entity (the reseller)
    - Alliance code (for invoicing)
    - Billing schedule (monthly billing cycle)
    - Fee rates (pricing configuration)
    - Processing group dates (cycle dates)
    - Billing hierarchies (merchant schedule and fee rate)
    - Partner config (settlement and invoice methods)
    - Plan action fee codes (global plan billing rules)
    - Cellular action fee codes (global cellular billing rules)

    All fixtures use a check-and-reuse strategy, so this test can be run
    repeatedly without accumulating test data in dev1.
    """
    # Validate billing entity
    billing_entity_uuid = billing_entity["billing_entity_uuid"]
    assert billing_entity_uuid, "Billing entity UUID must exist"
    assert len(billing_entity_uuid) == 26, "Billing entity UUID should be 26 chars"

    # Validate all components reference the same billing entity
    assert alliance_code["billing_entity_uuid"] == billing_entity_uuid
    assert billing_schedule["billing_entity_uuid"] == billing_entity_uuid
    assert fee_rate["billing_entity_uuid"] == billing_entity_uuid
    assert processing_group_dates["billing_entity_uuid"] == billing_entity_uuid
    assert billing_hierarchy["billing_entity_uuid"] == billing_entity_uuid
    assert partner_config["billing_entity_uuid"] == billing_entity_uuid

    # Validate alliance code format (only for newly created codes)
    if not alliance_code.get("was_reused"):
        assert alliance_code["alliance_code"].startswith(RESELLER_PREFIX)

    # Validate billing hierarchy has both required hierarchy types
    assert billing_hierarchy["merchant_schedule_uuid"]
    assert billing_hierarchy["merchant_fee_rate_uuid"]
    assert len(billing_hierarchy["merchant_schedule_uuid"]) == 26
    assert len(billing_hierarchy["merchant_fee_rate_uuid"]) == 26

    # Validate global resources
    assert plan_action_fee_code["merchant_plan_uuid"] == "YEQMV17H09HHW"
    assert cellular_action_fee_code["carrier"] == "AT&T"

    # Validate all components have create responses
    assert alliance_code["create_response"]
    assert billing_schedule["create_response"]
    assert fee_rate["create_response"]
    assert processing_group_dates["create_response"]
    assert partner_config["create_response"]
    assert plan_action_fee_code["create_response"]
    assert cellular_action_fee_code["create_response"]

    print(f"\n✅ Complete reseller setup validated for {billing_entity['name']}")
    print(f"   Billing entity UUID: {billing_entity_uuid}")
    print(f"   Alliance code: {alliance_code['alliance_code']}")
    print(f"   Reused existing: {billing_entity.get('was_reused', False)}")
