"""
Test complete reseller creation with proper meta.reseller → billing_bookkeeper linking.

RUNNING THIS TEST:
================================================================================
This test requires both rhizome and stolon servers to be running in separate
terminals BEFORE running pytest. This allows the servers to prompt for user
approval before executing database write operations.

Terminal 1: rhizome serve
Terminal 2: stolon serve
Terminal 3: pytest tests/stolon/test_create_reseller.py --external-infra

The servers will save their ports to ~/.trifolium/config automatically.
Keep terminals 1 and 2 open while running tests.
================================================================================

CORRECT CREATION ORDER (discovered via exploration):
1. Create meta.reseller first (via POST /v3/resellers) → get reseller_uuid
2. Create billing_bookkeeper.billing_entity with entity_uuid=reseller_uuid
3. Create all billing configuration components linked via billing_entity.uuid

KEY INSIGHT: The billing_entity does NOT create the reseller - it provides the
billing configuration for an existing meta.reseller. The link is established by
setting billing_entity.entity_uuid = meta.reseller.uuid.

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
from typing import Any

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.models.billing_bookkeeper.billing_entity import BillingEntity as BillingEntityModel
from rhizome.models.billing_bookkeeper.billing_hierarchy import BillingHierarchy as BillingHierarchyModel
from rhizome.models.billing_bookkeeper.billing_schedule import BillingSchedule as BillingScheduleModel
from rhizome.models.billing_bookkeeper.cellular_action_fee_code import (
    CellularActionFeeCode as CellularActionFeeCodeModel,
)
from rhizome.models.billing_bookkeeper.fee_rate import FeeRate as FeeRateModel
from rhizome.models.billing_bookkeeper.invoice_alliance_code import InvoiceAllianceCode as InvoiceAllianceCodeModel
from rhizome.models.billing_bookkeeper.partner_config import PartnerConfig as PartnerConfigModel
from rhizome.models.billing_bookkeeper.plan_action_fee_code import PlanActionFeeCode as PlanActionFeeCodeModel
from rhizome.models.billing_bookkeeper.processing_group_dates import ProcessingGroupDates as ProcessingGroupDatesModel
from stolon.client import StolonClient
from tests.conftest import RunningStolonServer
from trifolium.environments import dev

# Enable httpx debug logging to see all HTTP requests
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.DEBUG)

# Framework identification prefix for all created resources
# ⚠️  CHANGING THIS PREFIX WILL CREATE NEW RESOURCES:
# - This prefix is applied to resources created by this test framework:
#   * Billing entity entity_uuid: "{PREFIX}{hex}" (e.g., "MFF9535862249")
#   * Revenue share groups: "{PREFIX}_Test_{uuid}" (e.g., "MFF_Test_a1b2")
# - Alliance codes are NOT prefixed (API requires exactly 3 chars: ^[A-Z0-9]{3}$)
#   They use sequential 3-digit numbers (001, 002, etc.) and are tied to the reseller
#   via billing_entity_uuid foreign key
# - Changing this value (e.g., "MFF" -> "TEST") will cause the fixtures to create
#   NEW billing entities and supporting resources instead of reusing existing ones
# - This allows testing the full creation process from scratch
# - Resources CANNOT be deleted (API does not support DELETE), so they will accumulate in dev1
# - Use different prefixes to create separate test resellers (e.g., "TEST", "TST", "DEV")
# - Keep as "MFF" to reuse the existing shared test reseller
# - To find all framework-created resources, search for this prefix in:
#   * billing_entity.entity_uuid
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
def environment(stolon_server: RunningStolonServer) -> dev.Environment:
    """Unified dev environment with both database and HTTP access.

    This fixture creates a single Dev instance that provides:
    - environment.db.billing_bookkeeper: Database queries via Rhizome
    - environment.api.billing_bookkeeper: HTTP API calls via Stolon (wrapped generated client)

    Scope: module - one instance shared across all tests in this file.
    """
    rhizome_client = RhizomeClient(data_in_logs=False)
    stolon_client = StolonClient(home=stolon_server.home, data_in_logs=False)
    return dev.Environment(rhizome_client=rhizome_client, stolon_client=stolon_client)


@pytest.fixture
def revenue_share_group(environment: dev.Environment) -> Generator[dict[str, Any], None, None]:
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
def test_owner_account(environment: dev.Environment) -> Generator[dict[str, Any], None, None]:
    """Get or create the MFF Reseller Owner account.

    This fixture ensures the MFF User account exists with Super Administrator privileges
    for the Clover reseller. The account can create test resellers and serves as their owner.

    The fixture is idempotent - if the account already exists, it will be reused.

    Scope: module - reuse across all tests in this module.
    """
    from trifolium.util.models import TestOwnerAccount
    from trifolium.util.reseller import create_reseller_owner

    # Create or retrieve the MFF Reseller Owner account
    account_info = create_reseller_owner(environment)

    # Convert to TestOwnerAccount and yield as dict for compatibility
    test_account = TestOwnerAccount(
        account_id=account_info.id,
        uuid=account_info.uuid,
        email=account_info.email,
        name=account_info.name,
        was_reused=True,  # Will be True if account existed, effectively True always after first run
    )

    yield test_account.to_dict()


@pytest.fixture(scope="module")
def merchant_plan_group(environment: dev.Environment) -> Generator[dict[str, Any], None, None]:
    """Get or create a merchant plan group for testing.

    Checks if a test plan group with RESELLER_PREFIX already exists.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from rhizome.client import RhizomeClient
    from rhizome.environments.dev.meta import DevMeta
    from rhizome.models.meta.merchant_plan_group import MerchantPlanGroup as MerchantPlanGroupModel

    # Check if a plan group with our prefix name already exists
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)
    MerchantPlanGroup = meta_db.get_versioned(MerchantPlanGroupModel)

    existing_group = meta_db.select_first(
        select(MerchantPlanGroup)
        .where(MerchantPlanGroup.name.like(f"{RESELLER_PREFIX} Test Plan Group%"))  # type: ignore[attr-defined]
        .where(MerchantPlanGroup.deleted_time.is_(None))  # type: ignore[attr-defined]
        .order_by(MerchantPlanGroup.id.desc()),  # type: ignore[attr-defined]
        sanitize=False,
    )

    if existing_group:
        print(f"\n♻️  Reusing existing {RESELLER_PREFIX} merchant plan group: {existing_group.name}")
        print(f"    plan_group_id: {existing_group.id}")
        print(f"    plan_group_uuid: {existing_group.uuid}")

        yield {
            "plan_group_id": existing_group.id,
            "plan_group_uuid": existing_group.uuid,
            "name": existing_group.name,
            "was_reused": True,
        }
        return

    # No existing plan group found, create a new one
    print("\n=== Creating New Merchant Plan Group ===")

    group_name = f"{RESELLER_PREFIX} Test Plan Group {uuid_module.uuid4().hex[:4].upper()}"

    created_group = environment.api.resellers.create_merchant_plan_group(name=group_name)

    plan_group_id = created_group.get("id")
    plan_group_uuid = created_group.get("uuid")

    if not plan_group_id:
        raise Exception(f"Response did not contain id field. Response: {created_group}")

    print(f"\n✓ Created merchant plan group: {group_name}")
    print(f"    plan_group_id: {plan_group_id}")
    print(f"    plan_group_uuid: {plan_group_uuid}")

    yield {
        "plan_group_id": plan_group_id,
        "plan_group_uuid": plan_group_uuid,
        "name": group_name,
        "was_reused": False,
    }

    # Cleanup: Try to delete the merchant plan group (only works if empty)
    # Note: This will only succeed if all plans in the group have been deleted first
    try:
        print(f"\n🗑️  Attempting to delete merchant plan group {plan_group_id}")
        environment.api.resellers.delete_merchant_plan_group(str(plan_group_id))
        print("✅ Merchant plan group deleted successfully")
    except Exception as e:
        print(f"⚠️  Note: Merchant plan group {plan_group_id} could not be deleted: {e}")
        print("    (Plan groups can only be deleted when empty)")


@pytest.fixture(scope="module")
def merchant_plan(
    merchant_plan_group: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create a merchant plan for testing.

    Checks if the plan group already has a plan with RESELLER_PREFIX.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    from rhizome.client import RhizomeClient
    from rhizome.environments.dev.meta import DevMeta
    from rhizome.models.meta.merchant_plan import MerchantPlan as MerchantPlanModel

    plan_group_id = merchant_plan_group["plan_group_id"]

    # Check if a plan already exists in this group
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)
    MerchantPlan = meta_db.get_versioned(MerchantPlanModel)

    # Look for a default plan first (needed for merchant boarding)
    existing_plan = meta_db.select_first(
        select(MerchantPlan)
        .where(MerchantPlan.merchant_plan_group_id == plan_group_id)
        .where(MerchantPlan.name.like(f"{RESELLER_PREFIX} Test Plan%"))  # type: ignore[attr-defined]
        .where(MerchantPlan.deactivation_time.is_(None))  # type: ignore[attr-defined]  # Exclude deactivated plans
        .where(MerchantPlan.default_plan == True)  # type: ignore[attr-defined]  # Prefer default plans
        .order_by(MerchantPlan.id.desc()),  # type: ignore[attr-defined]
        sanitize=False,
    )

    if existing_plan:
        print(f"\n♻️  Reusing existing {RESELLER_PREFIX} merchant plan: {existing_plan.name}")
        print(f"    plan_uuid: {existing_plan.uuid}")
        print(f"    plan_code: {existing_plan.plan_code}")

        yield {
            "plan_uuid": existing_plan.uuid,
            "name": existing_plan.name,
            "plan_code": existing_plan.plan_code,
            "plan_group_id": plan_group_id,
            "was_reused": True,
        }
        return

    # No existing plan found, create a new one
    print("\n=== Creating New Merchant Plan ===")

    plan_name = f"{RESELLER_PREFIX} Test Plan {uuid_module.uuid4().hex[:4].upper()}"
    plan_code = f"{RESELLER_PREFIX}_TEST"

    # Convert plan_group_id to string if it's an int
    plan_group_id_str = str(plan_group_id) if isinstance(plan_group_id, int) else plan_group_id

    created_plan = environment.api.resellers.create_merchant_plan(
        merchant_plan_group_id=plan_group_id_str,
        name=plan_name,
        plan_code=plan_code,
        plan_type="PAYMENTS",
        default_plan=True,  # Mark as default so merchants can be boarded
    )

    plan_uuid = created_plan.get("uuid")
    if not plan_uuid:
        raise Exception(f"Response did not contain uuid field. Response: {created_plan}")

    print(f"\n✓ Created merchant plan: {plan_name}")
    print(f"    plan_uuid: {plan_uuid}")
    print(f"    plan_code: {plan_code}")

    yield {
        "plan_uuid": plan_uuid,
        "name": plan_name,
        "plan_code": plan_code,
        "plan_group_id": plan_group_id,
        "was_reused": False,
    }

    # Cleanup: Try to delete the merchant plan
    try:
        print(f"\n🗑️  Attempting to delete merchant plan {plan_uuid}")
        environment.api.resellers.delete_merchant_plan(str(plan_group_id), plan_uuid)
        print("✅ Merchant plan deleted successfully")
    except Exception as e:
        print(f"⚠️  Note: Merchant plan {plan_uuid} could not be deleted: {e}")


@pytest.fixture(scope="module")
def meta_reseller(
    test_owner_account: dict[str, Any], merchant_plan_group: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create a meta.reseller for testing.

    This must be created FIRST before any billing_bookkeeper entities.
    The reseller's UUID will be used as the entity_uuid in billing_entity.

    Checks if a test reseller with RESELLER_PREFIX already exists in meta.reseller.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    # Check if a meta reseller with our prefix name already exists
    # We need to use rhizome to query the meta database
    from rhizome.client import RhizomeClient
    from rhizome.environments.dev.meta import DevMeta
    from rhizome.models.meta.reseller import Reseller as ResellerModel

    # Create a new rhizome client for meta database access
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)
    Reseller = meta_db.get_versioned(ResellerModel)

    # Query for any reseller with our prefix name
    existing_reseller = meta_db.select_first(
        select(Reseller)
        .where(Reseller.name.like(f"{RESELLER_PREFIX} Test Reseller%"))  # type: ignore[attr-defined]
        .order_by(Reseller.id.desc()),  # type: ignore[attr-defined]
        sanitize=False,
    )

    if existing_reseller:
        print(f"\n♻️  Reusing existing {RESELLER_PREFIX} meta.reseller: {existing_reseller.name}")
        print(f"    reseller_uuid: {existing_reseller.uuid}")
        print(f"    reseller_id: {existing_reseller.id}")

        yield {
            "reseller_uuid": existing_reseller.uuid,
            "reseller_id": existing_reseller.id,
            "name": existing_reseller.name,
            "was_reused": True,
        }
        return

    # No existing reseller found, create a new one
    print("\n=== Creating New Meta Reseller ===")

    # Generate unique name using prefix
    reseller_name = f"{RESELLER_PREFIX} Test Reseller {uuid_module.uuid4().hex[:4].upper()}"

    # Get parent reseller ID and merchant plan group ID
    # Try to find the Demo reseller first
    demo_reseller = meta_db.select_first(
        select(Reseller).where(Reseller.name == "Demo"),
        sanitize=False,
    )

    # If Demo doesn't exist (e.g., in dev environment), use any reseller with type=DEMO
    if not demo_reseller:
        demo_reseller = meta_db.select_first(
            select(Reseller).where(Reseller.type == "DEMO"),  # type: ignore[attr-defined]
            sanitize=False,
        )

    # If still not found, use any reseller as parent
    if not demo_reseller:
        demo_reseller = meta_db.select_first(
            select(Reseller).where(Reseller.id.is_not(None)).order_by(Reseller.id),  # type: ignore[attr-defined]
            sanitize=False,
        )

    if not demo_reseller:
        raise Exception("Could not find any reseller to use as parent. The meta.reseller table may be empty.")

    print(f"\n📋 Using parent reseller: {demo_reseller.name} (id={demo_reseller.id}, uuid={demo_reseller.uuid})")
    print(f"    Test owner account: {test_owner_account['email']} (id={test_owner_account['account_id']})")
    print(f"    Merchant plan group: {merchant_plan_group['name']} (id={merchant_plan_group['plan_group_id']})")

    # Create meta.reseller using the API
    # Use the merchant_plan_group fixture (created/reused with MFF prefix)
    plan_group_id = merchant_plan_group["plan_group_id"]
    if isinstance(plan_group_id, int):
        plan_group_id = str(plan_group_id)

    # Use the test owner account (specific to this prefix for isolation)
    created_reseller = environment.api.resellers.create_reseller(
        name=reseller_name,
        owner_email=test_owner_account["email"],
        parent_reseller_id=demo_reseller.uuid,
        merchant_plan_group_id=plan_group_id,
        support_email="test@clover.com",
        support_phone="555-0100",
    )

    reseller_uuid = created_reseller.get("id")
    if not reseller_uuid:
        raise Exception(f"Response did not contain id field. Response: {created_reseller}")

    print(f"\n✓ Created meta.reseller: {reseller_name}")
    print(f"    reseller_uuid: {reseller_uuid}")

    yield {
        "reseller_uuid": reseller_uuid,
        "reseller_id": reseller_uuid,  # The API returns the UUID in the "id" field
        "name": reseller_name,
        "was_reused": False,
    }

    # Cleanup not supported for meta.reseller
    print(f"\n⚠️  Note: Meta reseller {reseller_uuid} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def boarded_merchant(
    meta_reseller: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Board a merchant to the test reseller.

    This creates a merchant associated with the reseller we created.
    Merchants are boarded via the IPG (Integrated Partner Gateway) endpoint.

    Scope: module - reuse across all tests in this module.
    """
    # Generate unique merchant ID using prefix + random hex
    merchant_id = f"{RESELLER_PREFIX}_{uuid_module.uuid4().hex[:8].upper()}"
    dba_name = f"{RESELLER_PREFIX} Test Merchant {uuid_module.uuid4().hex[:4].upper()}"
    legal_name = f"{RESELLER_PREFIX} Test LLC"

    print("\n=== Boarding Merchant to Reseller ===")
    print(f"    Reseller: {meta_reseller['name']}")
    print(f"    Reseller Code: {RESELLER_PREFIX}")
    print(f"    Merchant ID: {merchant_id}")
    print(f"    DBA Name: {dba_name}")

    # Get reseller code from meta_reseller fixture
    # The code is extracted from the reseller name (first word)
    reseller_code = RESELLER_PREFIX

    # Board the merchant
    boarding_response = environment.api.resellers.board_merchant(
        reseller_code=reseller_code,
        merchant_id=merchant_id,
        dba_name=dba_name,
        legal_name=legal_name,
        email="test@clover.com",
        country="US",
        currency="USD",
        timezone="America/Los_Angeles",
    )

    merchant_uuid = boarding_response["merchant_uuid"]

    print(f"\n✓ Merchant boarded successfully")
    print(f"    Merchant UUID: {merchant_uuid}")
    print(f"    Merchant ID (MID): {merchant_id}")

    yield {
        "merchant_uuid": merchant_uuid,
        "merchant_id": merchant_id,
        "dba_name": dba_name,
        "legal_name": legal_name,
        "reseller_code": reseller_code,
        "reseller_uuid": meta_reseller["reseller_uuid"],
        "boarding_response": boarding_response,
    }

    # Cleanup: Merchants cannot be deleted via API
    print(f"\n⚠️  Note: Merchant {merchant_uuid} cannot be automatically deleted (API does not support DELETE)")


@pytest.fixture(scope="module")
def billing_entity(
    meta_reseller: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing entity for testing.

    This links to the meta.reseller via entity_uuid = reseller_uuid.
    Creates the billing configuration side of the reseller.

    Scope: module - reuse across all tests in this module.
    """
    reseller_uuid = meta_reseller["reseller_uuid"]
    reseller_name = meta_reseller["name"]

    # Check if billing entity already exists for this reseller UUID
    BillingEntity = environment.db.billing_bookkeeper.get_versioned(BillingEntityModel)

    existing_entity = environment.db.billing_bookkeeper.select_first(
        select(BillingEntity)
        .where(BillingEntity.entity_type == "RESELLER")
        .where(BillingEntity.entity_uuid == reseller_uuid),
        sanitize=False,
    )

    if existing_entity:
        print(f"\n♻️  Reusing existing billing_entity for reseller: {reseller_name}")
        print(f"    billing_entity_uuid: {existing_entity.uuid}")
        print(f"    entity_uuid (reseller_uuid): {existing_entity.entity_uuid}")

        yield {
            "entity_uuid": existing_entity.entity_uuid,
            "billing_entity_uuid": existing_entity.uuid,
            "name": existing_entity.name,
            "reseller_uuid": reseller_uuid,
            "create_response": {"uuid": existing_entity.uuid},
            "was_reused": True,
        }
        return

    # No existing billing entity found, create a new one
    print("\n=== Creating New Billing Entity ===")
    print(f"    Linking to meta.reseller UUID: {reseller_uuid}")

    # Create billing entity with entity_uuid = reseller_uuid
    created_entity = environment.api.billing_bookkeeper.create_entity(
        entity_uuid=reseller_uuid,
        entity_type="RESELLER",
        name=reseller_name,
    )

    billing_entity_uuid = created_entity.get("uuid")
    if not billing_entity_uuid:
        raise Exception(f"Response did not contain uuid field. Response: {created_entity}")

    print(f"\n✓ Server-generated billing_entity_uuid: {billing_entity_uuid}")
    print(f"    Linked to reseller via entity_uuid: {reseller_uuid}")

    yield {
        "entity_uuid": reseller_uuid,
        "billing_entity_uuid": billing_entity_uuid,
        "name": reseller_name,
        "reseller_uuid": reseller_uuid,
        "create_response": created_entity,
        "was_reused": False,
    }

    # Cleanup not supported - DELETE method returns 405
    print(
        f"\n⚠️  Note: Billing entity {billing_entity_uuid} cannot be automatically deleted (API does not support DELETE)"
    )


@pytest.fixture(scope="module")
def alliance_code(
    billing_entity: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create an alliance code for testing.

    Checks if the billing entity already has an alliance code.
    If found, reuses it. Otherwise, creates a new one with sequential 3-digit number.

    Alliance codes must be exactly 3 characters (API validation: ^[A-Z0-9]{3}$).
    Uses format: 3-digit numbers (001, 002, ..., 999).
    The alliance code is tied to the reseller via the billing_entity_uuid foreign key.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if alliance code already exists for this billing entity
    InvoiceAllianceCode = environment.db.billing_bookkeeper.get_versioned(InvoiceAllianceCodeModel)

    existing_alliance_code = environment.db.billing_bookkeeper.select_first(
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

    # Alliance codes must be exactly 3 characters (API validation: ^[A-Z0-9]{3}$)
    # Since we can't include the reseller prefix, we use simple sequential 3-char codes
    # The billing_entity_uuid foreign key ties it to the reseller
    # Format: 3-digit number (001, 002, ..., 999)
    existing_codes = environment.db.billing_bookkeeper.select_all(
        select(InvoiceAllianceCode)
        .where(InvoiceAllianceCode.alliance_code.regexp_match(r"^\d{3}$"))  # type: ignore[attr-defined]
        .order_by(InvoiceAllianceCode.alliance_code.desc()),  # type: ignore[attr-defined]
        sanitize=False,
    )

    # Find the highest numeric code used
    max_num = 0
    for existing_code in existing_codes:
        code = existing_code.alliance_code
        if code.isdigit():
            max_num = max(max_num, int(code))

    # Increment to get next number
    next_num = max_num + 1

    # Format as 3-digit code (001, 002, ..., 999)
    alliance_code_value = f"{next_num:03d}"

    print(f"    Using alliance code: {alliance_code_value} (next after {max_num:03d})")
    print(f"    Note: Alliance codes are tied to reseller via billing_entity_uuid: {billing_entity_uuid}")

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
def billing_schedule(
    billing_entity: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create a billing schedule for testing.

    Checks if the billing entity already has a billing schedule.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if billing schedule already exists for this billing entity
    BillingSchedule = environment.db.billing_bookkeeper.get_versioned(BillingScheduleModel)

    existing_schedule = environment.db.billing_bookkeeper.select_first(
        select(BillingSchedule).where(BillingSchedule.billing_entity_uuid == billing_entity_uuid),
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
def fee_rate(billing_entity: dict[str, Any], environment: dev.Environment) -> Generator[dict[str, Any], None, None]:
    """Get or create a fee rate for testing.

    Checks if the billing entity already has a fee rate.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if fee rate already exists for this billing entity
    FeeRate = environment.db.billing_bookkeeper.get_versioned(FeeRateModel)

    existing_fee_rate = environment.db.billing_bookkeeper.select_first(
        select(FeeRate)
        .where(FeeRate.billing_entity_uuid == billing_entity_uuid)
        .order_by(FeeRate.created_timestamp.desc()),  # type: ignore[attr-defined]  # SQLModel columns have .desc()
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
    billing_entity: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create processing group dates for testing.

    Checks if the billing entity already has processing group dates.
    If found, reuses it. Otherwise, creates a new one.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if processing group dates already exist for this billing entity
    ProcessingGroupDates = environment.db.billing_bookkeeper.get_versioned(ProcessingGroupDatesModel)

    existing_pgd = environment.db.billing_bookkeeper.select_first(
        select(ProcessingGroupDates).where(ProcessingGroupDates.billing_entity_uuid == billing_entity_uuid),
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
def billing_hierarchy(
    billing_entity: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
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
    BillingHierarchy = environment.db.billing_bookkeeper.get_versioned(BillingHierarchyModel)

    # Query for common parent hierarchies in dev1
    # Find the most commonly used parent hierarchies for each type
    merchant_schedule_parent = environment.db.billing_bookkeeper.select_first(
        select(BillingHierarchy.parent_billing_hierarchy_uuid)
        .where(BillingHierarchy.hierarchy_type == "MERCHANT_SCHEDULE")
        .where(BillingHierarchy.parent_billing_hierarchy_uuid.is_not(None))  # type: ignore[attr-defined]
        .limit(1),
        sanitize=False,
    )

    merchant_fee_rate_parent = environment.db.billing_bookkeeper.select_first(
        select(BillingHierarchy.parent_billing_hierarchy_uuid)
        .where(BillingHierarchy.hierarchy_type == "MERCHANT_FEE_RATE")
        .where(BillingHierarchy.parent_billing_hierarchy_uuid.is_not(None))  # type: ignore[attr-defined]
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
        select(BillingHierarchy)
        .where(BillingHierarchy.billing_entity_uuid == billing_entity_uuid)
        .where(BillingHierarchy.hierarchy_type == "MERCHANT_SCHEDULE"),
        sanitize=False,
    )

    existing_fee_rate_hierarchy = environment.db.billing_bookkeeper.select_first(
        select(BillingHierarchy)
        .where(BillingHierarchy.billing_entity_uuid == billing_entity_uuid)
        .where(BillingHierarchy.hierarchy_type == "MERCHANT_FEE_RATE"),
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
def partner_config(
    billing_entity: dict[str, Any], environment: dev.Environment
) -> Generator[dict[str, Any], None, None]:
    """Get or create a partner config for testing.

    Checks if the billing entity already has a partner config for MERCHANT_SCHEDULE.
    If found, reuses it. Otherwise, creates a new one.

    Partner config is required for resellers to process invoices and settlements.

    Scope: module - reuse across all tests in this module.
    """
    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    # Check if partner config already exists for this billing entity
    PartnerConfig = environment.db.billing_bookkeeper.get_versioned(PartnerConfigModel)

    existing_partner_config = environment.db.billing_bookkeeper.select_first(
        select(PartnerConfig)
        .where(PartnerConfig.billing_entity_uuid == billing_entity_uuid)
        .where(PartnerConfig.hierarchy_type == "MERCHANT_SCHEDULE"),
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
def plan_action_fee_code(environment: dev.Environment) -> Generator[dict[str, Any], None, None]:
    """Get or create a plan action fee code for testing.

    Plan action fee codes are GLOBAL resources (not tied to billing entity).
    Always checks if one exists before creating.

    Scope: module - reuse across all tests in this module.
    """
    import httpx

    test_plan_uuid = "YEQMV17H09HHW"

    # Check if plan action fee code already exists (global resource)
    PlanActionFeeCode = environment.db.billing_bookkeeper.get_versioned(PlanActionFeeCodeModel)

    existing_plan_action_fee_code = environment.db.billing_bookkeeper.select_first(
        select(PlanActionFeeCode)
        .where(PlanActionFeeCode.merchant_plan_uuid == test_plan_uuid)
        .where(PlanActionFeeCode.plan_action_type == "PLAN_ASSIGN")
        .where(PlanActionFeeCode.fee_category == "PLAN_RETAIL")
        .where(PlanActionFeeCode.fee_code == "PaymentsPDVT.PRC"),
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
def cellular_action_fee_code(environment: dev.Environment) -> Generator[dict[str, Any], None, None]:
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
    CellularActionFeeCode = environment.db.billing_bookkeeper.get_versioned(CellularActionFeeCodeModel)

    existing_cellular_action_fee_code = environment.db.billing_bookkeeper.select_first(
        select(CellularActionFeeCode)
        .where(CellularActionFeeCode.carrier == carrier)
        .where(CellularActionFeeCode.cellular_action_type == cellular_action_type)
        .where(CellularActionFeeCode.fee_category == "CELLULAR_RETAIL")
        .where(CellularActionFeeCode.fee_code == "CellularArr.ATT"),
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
    meta_reseller: dict[str, Any],
    boarded_merchant: dict[str, Any],
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
    """Test creating a complete reseller with all required components and boarding a merchant.

    This test follows the correct creation order discovered via exploration:
    1. meta.reseller (core reseller entity via /v3/resellers)
    2. Merchant boarding (associate a test merchant with the reseller)
    3. billing_bookkeeper.billing_entity (billing config, links via entity_uuid=reseller.uuid)
    4. All billing configuration components (link via billing_entity_uuid)

    Components tested:
    - Meta reseller (the core reseller record in meta.reseller table)
    - Boarded merchant (merchant associated with the reseller)
    - Billing entity (billing configuration, entity_uuid = reseller UUID)
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
    # Validate meta reseller
    reseller_uuid = meta_reseller["reseller_uuid"]
    assert reseller_uuid, "Reseller UUID must exist"
    assert len(reseller_uuid) == 13, "Reseller UUID should be 13 chars"

    # Validate boarded merchant
    merchant_uuid = boarded_merchant["merchant_uuid"]
    assert merchant_uuid, "Merchant UUID must exist"
    assert len(merchant_uuid) == 13, "Merchant UUID should be 13 chars"
    assert boarded_merchant["reseller_uuid"] == reseller_uuid, "Merchant should be linked to the reseller"
    assert boarded_merchant["reseller_code"] == RESELLER_PREFIX, f"Merchant should use reseller code {RESELLER_PREFIX}"
    assert boarded_merchant["merchant_id"], "Merchant ID (MID) must exist"
    assert RESELLER_PREFIX in boarded_merchant["merchant_id"], f"Merchant ID should contain prefix {RESELLER_PREFIX}"

    # Validate billing entity links to meta reseller
    billing_entity_uuid = billing_entity["billing_entity_uuid"]
    assert billing_entity_uuid, "Billing entity UUID must exist"
    assert len(billing_entity_uuid) == 26, "Billing entity UUID should be 26 chars"

    # CRITICAL: Validate the link between meta.reseller and billing_bookkeeper.billing_entity
    assert billing_entity["entity_uuid"] == reseller_uuid, (
        f"Billing entity entity_uuid ({billing_entity['entity_uuid']}) must match reseller UUID ({reseller_uuid})"
    )
    assert billing_entity["reseller_uuid"] == reseller_uuid

    # Validate all components reference the same billing entity
    assert alliance_code["billing_entity_uuid"] == billing_entity_uuid
    assert billing_schedule["billing_entity_uuid"] == billing_entity_uuid
    assert fee_rate["billing_entity_uuid"] == billing_entity_uuid
    assert processing_group_dates["billing_entity_uuid"] == billing_entity_uuid
    assert billing_hierarchy["billing_entity_uuid"] == billing_entity_uuid
    assert partner_config["billing_entity_uuid"] == billing_entity_uuid

    # Validate alliance code format (must be exactly 3 characters)
    assert len(alliance_code["alliance_code"]) == 3, "Alliance code must be exactly 3 characters"

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

    print("\n" + "=" * 80)
    print("✅ COMPLETE RESELLER SETUP VALIDATED")
    print("=" * 80)
    print("\n📋 Meta Reseller:")
    print(f"   Name: {meta_reseller['name']}")
    print(f"   UUID: {reseller_uuid}")
    print(f"   Code: {RESELLER_PREFIX}")
    print(f"   Was Reused: {meta_reseller.get('was_reused', False)}")
    print("\n🏪 Boarded Merchant:")
    print(f"   DBA Name: {boarded_merchant['dba_name']}")
    print(f"   Legal Name: {boarded_merchant['legal_name']}")
    print(f"   Merchant UUID: {merchant_uuid}")
    print(f"   Merchant ID (MID): {boarded_merchant['merchant_id']}")
    print(f"   Reseller Code: {boarded_merchant['reseller_code']}")
    print("\n💰 Billing Entity:")
    print(f"   Billing Entity UUID: {billing_entity_uuid}")
    print(f"   Entity UUID (links to reseller): {billing_entity['entity_uuid']}")
    print(f"   Was Reused: {billing_entity.get('was_reused', False)}")
    print("\n🔗 Links Verified:")
    print("   meta.reseller.uuid == billing_entity.entity_uuid: ✓")
    print("   merchant.reseller_code == meta.reseller.code: ✓")
    print("\n📇 Billing Configuration:")
    print(f"   Alliance code: {alliance_code['alliance_code']}")
    print("   Billing schedule: Created")
    print("   Fee rates: Created")
    print("   Processing group dates: Created")
    print("   Billing hierarchies: 2 types")
    print("   Partner config: Created")
    print("\n🎉 Reseller is fully configured with a boarded merchant!")
