"""
Test the user-facing API for stolon environments.

This module tests the API patterns that allow users to make authenticated
HTTP requests to Clover APIs without needing to manage tokens directly.

Tests for reseller creation follow a bottom-up approach:
1. Leaf node tests create/delete individual resources
2. Composite tests build up the dependency tree
3. Final test creates a complete reseller hierarchy

Test data should align with demo2 environment structure where possible.

All test resources are idempotent - they check for existence before creating,
and reuse existing resources to avoid accumulating test data that cannot be deleted.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generator

import pytest

from tests.conftest import RunningServer, RunningStolonServer


# Fixed test resource identifiers - reused across test runs to avoid accumulation
FIXED_ENTITY_UUID = "MFFTESTFIXTURE1"  # 13-char entity UUID for test reseller
FIXED_ALLIANCE_CODE = "9TF"  # Test alliance code
FIXED_REVENUE_SHARE_GROUP = "MFF_Test_Fixture"  # Test revenue share group name


@dataclass
class BillingResources:
    """Container for test billing resources used across tests."""

    # Revenue share group
    revenue_share_group_name: str
    revenue_share_group_uuid: str | None

    # Billing entity (reseller)
    entity_uuid: str  # 13-char entity UUID (e.g., MFFTESTFIXTURE1)
    billing_entity_uuid: str  # 26-char server-generated UUID
    reseller_name: str

    # Alliance code
    alliance_code: str
    alliance_code_uuid: str | None

    # Billing schedule
    billing_schedule_uuid: str | None



    # Fee rate
    fee_rate_uuid: str | None

    # Processing group dates
    processing_group_dates_uuid: str | None


@pytest.fixture(scope="session")
def test_billing_resources(
    stolon_server: RunningStolonServer, real_rhizome_client: RhizomeClient
) -> Generator[BillingResources, None, None]:
    """
    Create or reuse test billing resources.

    This fixture is session-scoped and idempotent - it checks for existing resources
    before creating new ones, avoiding accumulation of test data.

    Resources that can be deleted (revenue share groups) are cleaned up after tests.
    Resources that cannot be deleted are reused across test runs.
    """
    from rhizome.client import RhizomeClient
    from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
    from rhizome.models.billing_bookkeeper.billing_entity_v1 import BillingEntityV1
    from rhizome.models.billing_bookkeeper.billing_schedule_v1 import BillingScheduleV1

    from rhizome.models.billing_bookkeeper.fee_rate_v1 import FeeRateV1
    from rhizome.models.billing_bookkeeper.invoice_alliance_code_v1 import InvoiceAllianceCodeV1
    from rhizome.models.billing_bookkeeper.processing_group_dates_v1 import ProcessingGroupDatesV1
    from rhizome.models.billing_bookkeeper.revenue_share_group_v1 import RevenueShareGroupV1
    from sqlmodel import select
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    # Initialize clients
    stolon_client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev_http = DevHttp(stolon_client)

    dev_db = DevBillingBookkeeper(real_rhizome_client)

    # Use specific V1 models for dev environment
    BillingEntity = BillingEntityV1
    RevenueShareGroup = RevenueShareGroupV1
    AllianceCode = InvoiceAllianceCodeV1
    BillingSchedule = BillingScheduleV1

    FeeRate = FeeRateV1
    ProcessingGroupDates = ProcessingGroupDatesV1

    print("\n=== Checking for existing test resources ===")

    # 1. Check/create revenue share group (can be deleted, so create fresh)
    print(f"\n🔍 Checking for revenue share group: {FIXED_REVENUE_SHARE_GROUP}")
    existing_rsg = dev_db.select_first(
        select(RevenueShareGroup).where(RevenueShareGroup.revenue_share_group == FIXED_REVENUE_SHARE_GROUP)
    )

    if existing_rsg:
        print(f"✓ Found existing revenue share group: {existing_rsg.uuid}")
        rsg_uuid = existing_rsg.uuid
    else:
        print("✗ Not found, creating new revenue share group")
        rsg_data = {
            "revenueShareGroup": FIXED_REVENUE_SHARE_GROUP,
            "shortDesc": f"MFF-{FIXED_REVENUE_SHARE_GROUP}",
            "description": f"Test fixture revenue share group for {FIXED_REVENUE_SHARE_GROUP}",
        }
        rsg_response = dev_http.post("/billing-bookkeeper/v1/revsharegroup", json=rsg_data)
        rsg_uuid = rsg_response.get("uuid")
        print(f"✓ Created revenue share group: {rsg_uuid}")

    # 2. Check/create billing entity (cannot be deleted, reuse if exists)
    print(f"\n🔍 Checking for billing entity: {FIXED_ENTITY_UUID}")
    existing_entity = dev_db.select_first(select(BillingEntity).where(BillingEntity.entity_uuid == FIXED_ENTITY_UUID))

    if existing_entity:
        print(f"✓ Found existing billing entity: {existing_entity.uuid}")
        billing_entity_uuid = existing_entity.uuid
        reseller_name = existing_entity.name
    else:
        print("✗ Not found, creating new billing entity")
        reseller_name = "MFF Test Fixture Reseller"
        entity_data = {"entityUuid": FIXED_ENTITY_UUID, "entityType": "RESELLER", "name": reseller_name}
        entity_response = dev_http.post("/billing-bookkeeper/v1/entity", json=entity_data)
        billing_entity_uuid = entity_response.get("uuid")
        print(f"✓ Created billing entity: {billing_entity_uuid}")

    # 3. Check/create alliance code (cannot be deleted, reuse if exists)
    print(f"\n🔍 Checking for alliance code: {FIXED_ALLIANCE_CODE}")
    existing_alliance = dev_db.select_first(
        select(AllianceCode).where(AllianceCode.alliance_code == FIXED_ALLIANCE_CODE)
    )

    if existing_alliance:
        print(f"✓ Found existing alliance code: {existing_alliance.uuid}")
        alliance_code_uuid = existing_alliance.uuid
    else:
        print("✗ Not found, creating new alliance code")
        alliance_data = {
            "billingEntityUuid": billing_entity_uuid,
            "allianceCode": FIXED_ALLIANCE_CODE,
            "invoiceCount": 1,
        }
        alliance_response = dev_http.post("/billing-bookkeeper/v1/alliancecode", json=alliance_data)
        alliance_code_uuid = alliance_response.get("uuid")
        print(f"✓ Created alliance code: {alliance_code_uuid}")

    # 4. Check/create billing schedule (cannot be deleted, reuse if exists)
    print(f"\n🔍 Checking for billing schedule for entity: {billing_entity_uuid}")
    existing_schedule = dev_db.select_first(
        select(BillingSchedule).where(BillingSchedule.billing_entity_uuid == billing_entity_uuid)
    )

    if existing_schedule:
        print(f"✓ Found existing billing schedule: {existing_schedule.uuid}")
        billing_schedule_uuid = existing_schedule.uuid
    else:
        print("✗ Not found, creating new billing schedule")
        schedule_data = {
            "billingEntityUuid": billing_entity_uuid,
            "effectiveDate": "2025-08-01",
            "frequency": "MONTHLY",
            "billingDay": 1,
            "nextBillingDate": "2025-09-01",
            "unitsInNextPeriod": 31,
            "defaultCurrency": "EUR",
        }
        schedule_response = dev_http.post("/billing-bookkeeper/v1/schedule", json=schedule_data)
        billing_schedule_uuid = schedule_response.get("uuid")
        print(f"✓ Created billing schedule: {billing_schedule_uuid}")



    # 5. Check/create fee rate (cannot be deleted, reuse if exists)
    print(f"\n🔍 Checking for fee rate for entity: {billing_entity_uuid}")
    existing_rate = dev_db.select_first(
        select(FeeRate)
        .where(FeeRate.billing_entity_uuid == billing_entity_uuid)
        .where(FeeRate.fee_code == "PaymentsPDVT")
    )

    if existing_rate:
        print(f"✓ Found existing fee rate: {existing_rate.uuid}")
        fee_rate_uuid = existing_rate.uuid
    else:
        print("✗ Not found, creating new fee rate")
        rate_data = {
            "billingEntityUuid": billing_entity_uuid,
            "feeCategory": "PLAN_RETAIL",
            "feeCode": "PaymentsPDVT",
            "currency": "EUR",
            "effectiveDate": "2025-08-01",
            "applyType": "DEFAULT",
            "perItemAmount": 0.0,
        }
        rate_response = dev_http.post("/billing-bookkeeper/v1/rate", json=rate_data)
        fee_rate_uuid = rate_response.get("uuid")
        print(f"✓ Created fee rate: {fee_rate_uuid}")

    # 6. Check/create processing group dates (cannot be deleted, reuse if exists)
    print(f"\n🔍 Checking for processing group dates for entity: {billing_entity_uuid}")
    existing_pgd = dev_db.select_first(
        select(ProcessingGroupDates).where(ProcessingGroupDates.billing_entity_uuid == billing_entity_uuid)
    )

    if existing_pgd:
        print(f"✓ Found existing processing group dates: {existing_pgd.uuid}")
        pgd_uuid = existing_pgd.uuid
    else:
        print("✗ Not found, creating new processing group dates")
        pgd_data = {
            "billingEntityUuid": billing_entity_uuid,
            "hierarchyType": "MERCHANT_SCHEDULE",
            "cycleDate": "2025-08-01",
            "postingDate": "2025-08-01",
            "billingDate": "2025-08-01",
            "settlementDate": "2025-08-01",
        }
        pgd_response = dev_http.post("/billing-bookkeeper/v1/processgroupdates", json=pgd_data)
        pgd_uuid = pgd_response.get("uuid")
        print(f"✓ Created processing group dates: {pgd_uuid}")

    print("\n=== Test resources ready ===")

    # Yield resources for tests
    resources = BillingResources(
        revenue_share_group_name=FIXED_REVENUE_SHARE_GROUP,
        revenue_share_group_uuid=rsg_uuid,
        entity_uuid=FIXED_ENTITY_UUID,
        billing_entity_uuid=billing_entity_uuid,
        reseller_name=reseller_name,
        alliance_code=FIXED_ALLIANCE_CODE,
        alliance_code_uuid=alliance_code_uuid,
        billing_schedule_uuid=billing_schedule_uuid,

        fee_rate_uuid=fee_rate_uuid,
        processing_group_dates_uuid=pgd_uuid,
    )

    yield resources

    # Cleanup: Only delete revenue share group (others cannot be deleted)
    if rsg_uuid:
        try:
            print(f"\n🗑️  Deleting revenue share group {rsg_uuid}")
            dev_http.delete(f"/billing-bookkeeper/v1/revsharegroup/{rsg_uuid}")
            print("✅ Cleanup successful")
        except Exception as e:
            print(f"⚠️  Cleanup failed: {e}")

    # Note about resources that cannot be cleaned up
    print(
        f"""
⚠️  Note: The following test resources cannot be automatically deleted:
   - Billing entity: {billing_entity_uuid}
   - Alliance code: {FIXED_ALLIANCE_CODE}
   - Billing schedule, fee rate, processing group dates

   These will be reused in future test runs (idempotent).
"""
    )


# ============================================================================
# Tests
# ============================================================================


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


# --- Leaf Node Tests: Verify Individual Resources ---
# These tests verify the test resources fixture creates all required components


@pytest.mark.external_infra
def test_revenue_share_group_exists(test_billing_resources: BillingResources) -> None:
    """Verify revenue share group was created or found."""
    assert test_billing_resources.revenue_share_group_name == FIXED_REVENUE_SHARE_GROUP
    assert test_billing_resources.revenue_share_group_uuid
    assert len(test_billing_resources.revenue_share_group_uuid) == 26


@pytest.mark.external_infra
def test_billing_entity_exists(test_billing_resources: BillingResources) -> None:
    """Verify billing entity (reseller) was created or found."""
    assert test_billing_resources.entity_uuid == FIXED_ENTITY_UUID
    assert test_billing_resources.billing_entity_uuid
    assert len(test_billing_resources.billing_entity_uuid) == 26
    assert test_billing_resources.reseller_name


@pytest.mark.external_infra
def test_alliance_code_exists(test_billing_resources: BillingResources) -> None:
    """Verify alliance code was created or found."""
    assert test_billing_resources.alliance_code == FIXED_ALLIANCE_CODE
    assert test_billing_resources.alliance_code_uuid
    assert len(test_billing_resources.alliance_code_uuid) == 26


@pytest.mark.external_infra
def test_billing_schedule_exists(test_billing_resources: BillingResources) -> None:
    """Verify billing schedule was created or found."""
    assert test_billing_resources.billing_schedule_uuid
    assert len(test_billing_resources.billing_schedule_uuid) == 26





@pytest.mark.external_infra
def test_fee_rate_exists(test_billing_resources: BillingResources) -> None:
    """Verify fee rate was created or found."""
    assert test_billing_resources.fee_rate_uuid
    assert len(test_billing_resources.fee_rate_uuid) == 26


@pytest.mark.external_infra
def test_processing_group_dates_exists(test_billing_resources: BillingResources) -> None:
    """Verify processing group dates were created or found."""
    assert test_billing_resources.processing_group_dates_uuid
    assert len(test_billing_resources.processing_group_dates_uuid) == 26
