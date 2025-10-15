#!/usr/bin/env python3
"""
Explore merchant terms acceptance in dev environment.

This script queries both billing and billing_event databases to understand:
1. How merchant terms acceptance is tracked
2. What agreement types exist
3. What actions/statuses are used
4. Which table should be used to check if a merchant has accepted terms
"""

from collections import defaultdict
from typing import Any

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.billing import DevBilling
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.models.billing.merchant_terms_acceptance import MerchantTermsAcceptance as MerchantTermsAcceptanceModel
from rhizome.models.billing_event.merchant_acceptance import MerchantAcceptance as MerchantAcceptanceModel
from stolon.client import StolonClient
from trifolium.environments import dev


def explore_billing_event_merchant_acceptance() -> None:
    """Explore billing_event.merchant_acceptance table."""
    print("=" * 80)
    print("🔍 EXPLORING: billing_event.merchant_acceptance")
    print("=" * 80)

    rhizome_client = RhizomeClient(data_in_logs=False)
    billing_event_db = DevBillingEvent(rhizome_client)

    # Get the versioned model
    MerchantAcceptance = billing_event_db.get_versioned(MerchantAcceptanceModel)

    # Query recent acceptances
    recent_acceptances = billing_event_db.select_all(
        select(MerchantAcceptance)
        .where(MerchantAcceptance.action == "ACCEPTED")  # type: ignore[attr-defined]
        .order_by(MerchantAcceptance.created_timestamp.desc())  # type: ignore[attr-defined]
        .limit(20),
        sanitize=False,
    )

    if not recent_acceptances:
        print("⚠️  No ACCEPTED records found in billing_event.merchant_acceptance")
        return

    print(f"\n📊 Found {len(recent_acceptances)} recent ACCEPTED records")

    # Track statistics
    stats: dict[str, dict[str, int]] = {
        "agreement_type": defaultdict(int),
        "agreement_event_type": defaultdict(int),
        "action": defaultdict(int),
        "has_serial_number": defaultdict(int),
        "has_iccid": defaultdict(int),
        "is_oobe": defaultdict(int),
    }

    # Sample records for display
    print("\n📝 Sample Records:")
    for i, acceptance in enumerate(recent_acceptances[:3]):
        print(f"\n--- Record {i+1} ---")
        print(f"Merchant UUID: {acceptance.merchant_uuid}")
        print(f"Account ID: {acceptance.account_id}")
        print(f"Acceptance ID: {acceptance.acceptance_id}")
        print(f"Agreement ID: {acceptance.agreement_id}")
        print(f"Agreement Type: {acceptance.agreement_type}")
        print(f"Agreement Event Type: {acceptance.agreement_event_type}")
        print(f"Action: {acceptance.action}")
        print(f"Created: {acceptance.acceptance_created_datetime}")
        print(f"Modified: {acceptance.acceptance_modified_datetime}")
        print(f"Deleted: {acceptance.acceptance_deleted_datetime}")
        print(f"Expiration: {acceptance.acceptance_expiration_datetime}")
        print(f"Serial Number: {acceptance.serial_number}")
        print(f"ICCID: {acceptance.iccid}")
        print(f"Is OOBE: {acceptance.is_oobe}")

    # Collect statistics
    for acceptance in recent_acceptances:
        stats["agreement_type"][acceptance.agreement_type] += 1
        stats["agreement_event_type"][str(acceptance.agreement_event_type)] += 1
        stats["action"][str(acceptance.action)] += 1
        stats["has_serial_number"]["Yes" if acceptance.serial_number else "No"] += 1
        stats["has_iccid"]["Yes" if acceptance.iccid else "No"] += 1
        stats["is_oobe"][str(acceptance.is_oobe)] += 1

    # Print statistics
    print("\n\n📈 STATISTICS (from 20 recent ACCEPTED records)")
    print("=" * 80)
    for field_name, field_stats in stats.items():
        print(f"\n{field_name.replace('_', ' ').title()}:")
        sorted_stats = sorted(field_stats.items(), key=lambda x: x[1], reverse=True)
        total = sum(field_stats.values())
        for value, count in sorted_stats:
            percentage = (count / total) * 100
            print(f"  {value}: {count} ({percentage:.1f}%)")

    # Query all actions to understand state machine
    print("\n\n🔄 ACTION DISTRIBUTION (all records)")
    print("=" * 80)
    all_actions = billing_event_db.select_all(
        select(MerchantAcceptance.action)  # type: ignore[attr-defined]
        .group_by(MerchantAcceptance.action)  # type: ignore[attr-defined]
        .limit(100),
        sanitize=False,
    )
    action_counts: dict[str, int] = defaultdict(int)
    all_records = billing_event_db.select_all(
        select(MerchantAcceptance).limit(1000),
        sanitize=False,
    )
    for record in all_records:
        action_counts[str(record.action)] += 1

    sorted_actions = sorted(action_counts.items(), key=lambda x: x[1], reverse=True)
    total_actions = sum(action_counts.values())
    for action, count in sorted_actions:
        percentage = (count / total_actions) * 100
        print(f"  {action}: {count} ({percentage:.1f}%)")


def explore_billing_merchant_terms_acceptance() -> None:
    """Explore billing.merchant_terms_acceptance table."""
    print("\n\n")
    print("=" * 80)
    print("🔍 EXPLORING: billing.merchant_terms_acceptance")
    print("=" * 80)

    rhizome_client = RhizomeClient(data_in_logs=False)
    billing_db = DevBilling(rhizome_client)

    # Get the versioned model
    MerchantTermsAcceptance = billing_db.get_versioned(MerchantTermsAcceptanceModel)

    # Query recent acceptances
    recent_acceptances = billing_db.select_all(
        select(MerchantTermsAcceptance)
        .where(MerchantTermsAcceptance.action == "ACCEPTED")  # type: ignore[attr-defined]
        .order_by(MerchantTermsAcceptance.created_time.desc())  # type: ignore[attr-defined]
        .limit(20),
        sanitize=False,
    )

    if not recent_acceptances:
        print("⚠️  No ACCEPTED records found in billing.merchant_terms_acceptance")
        return

    print(f"\n📊 Found {len(recent_acceptances)} recent ACCEPTED records")

    # Track statistics
    stats: dict[str, dict[str, int]] = {
        "agreement_type": defaultdict(int),
        "action": defaultdict(int),
        "has_uuid": defaultdict(int),
        "has_acceptance_deleted": defaultdict(int),
    }

    # Sample records for display
    print("\n📝 Sample Records:")
    for i, acceptance in enumerate(recent_acceptances[:3]):
        print(f"\n--- Record {i+1} ---")
        print(f"ID: {acceptance.id}")
        print(f"UUID: {acceptance.uuid}")
        print(f"Merchant ID: {acceptance.merchant_id}")
        print(f"Acceptance ID: {acceptance.acceptance_id}")
        print(f"Agreement Type: {acceptance.agreement_type}")
        print(f"Action: {acceptance.action}")
        print(f"Created: {acceptance.acceptance_created}")
        print(f"Modified: {acceptance.acceptance_modified}")
        print(f"Deleted: {acceptance.acceptance_deleted}")

    # Collect statistics
    for acceptance in recent_acceptances:
        stats["agreement_type"][acceptance.agreement_type or "None"] += 1
        stats["action"][acceptance.action or "None"] += 1
        stats["has_uuid"]["Yes" if acceptance.uuid else "No"] += 1
        stats["has_acceptance_deleted"]["Yes" if acceptance.acceptance_deleted else "No"] += 1

    # Print statistics
    print("\n\n📈 STATISTICS (from 20 recent ACCEPTED records)")
    print("=" * 80)
    for field_name, field_stats in stats.items():
        print(f"\n{field_name.replace('_', ' ').title()}:")
        sorted_stats = sorted(field_stats.items(), key=lambda x: x[1], reverse=True)
        total = sum(field_stats.values())
        for value, count in sorted_stats:
            percentage = (count / total) * 100
            print(f"  {value}: {count} ({percentage:.1f}%)")


def test_api_endpoints(merchant_uuid: str, account_id: str) -> None:
    """Test the API endpoints for checking and accepting terms."""
    print("\n\n")
    print("=" * 80)
    print("🌐 TESTING API ENDPOINTS")
    print("=" * 80)

    rhizome_client = RhizomeClient(data_in_logs=False)
    stolon_client = StolonClient(data_in_logs=False)
    environment = dev.Environment(rhizome_client=rhizome_client, stolon_client=stolon_client)

    # Test 1: Check current acceptances using bulk query endpoint
    print("\n1️⃣  Testing: POST /agreement/v1/acceptances/bulk")
    print(f"   Querying acceptances for merchant: {merchant_uuid}")

    try:
        # Use the merchant_uuid as merchantId (13-char UUID format)
        acceptances_response = environment.api.agreement.get_acceptances_bulk(
            merchant_ids=[merchant_uuid]
        )

        if acceptances_response:
            print(f"   ✅ Found {len(acceptances_response)} acceptance(s)")
            for acceptance in acceptances_response:
                print(f"\n   Acceptance Details:")
                print(f"      ID: {acceptance.get('id')}")
                print(f"      Merchant ID: {acceptance.get('merchantId')}")
                print(f"      Account ID: {acceptance.get('accountId')}")
                print(f"      Agreement Type: {acceptance.get('agreementType')}")
                print(f"      Action: {acceptance.get('action')}")
                print(f"      Current: {acceptance.get('current')}")
                print(f"      Version: {acceptance.get('version')}")
                print(f"      Created: {acceptance.get('createdTime')}")
                print(f"      Deleted: {acceptance.get('deletedTime')}")
        else:
            print("   ❌ No acceptances found")

    except Exception as e:
        print(f"   ⚠️  Error querying acceptances: {e}")

    # Test 2: Show what backfill acceptance would look like (don't actually call it)
    print("\n\n2️⃣  Backfill Acceptance Endpoint (for reference)")
    print("   POST /billing-event/v1/backfill_acceptance")
    print(f"   Payload example:")
    print(f"   {{")
    print(f"     \"accountId\": \"{account_id}\",")
    print(f"     \"type\": \"BILLING\",")
    print(f"     \"locale\": \"en_US\",")
    print(f"     \"comment\": \"Automated test acceptance\",")
    print(f"     \"devices\": [],")
    print(f"     \"merchantId\": \"{merchant_uuid}\"")
    print(f"   }}")
    print(f"\n   ⚠️  Not calling this endpoint during exploration to avoid creating test data")


def check_merchant_acceptance(merchant_uuid: str) -> None:
    """Check if a specific merchant has accepted terms."""
    print("\n\n")
    print("=" * 80)
    print(f"🔍 CHECKING MERCHANT: {merchant_uuid}")
    print("=" * 80)

    rhizome_client = RhizomeClient(data_in_logs=False)

    # Check billing_event
    billing_event_db = DevBillingEvent(rhizome_client)
    MerchantAcceptance = billing_event_db.get_versioned(MerchantAcceptanceModel)

    acceptances = billing_event_db.select_all(
        select(MerchantAcceptance)
        .where(MerchantAcceptance.merchant_uuid == merchant_uuid)  # type: ignore[attr-defined]
        .order_by(MerchantAcceptance.created_timestamp.desc()),  # type: ignore[attr-defined]
        sanitize=False,
    )

    if acceptances:
        print(f"\n✅ Found {len(acceptances)} acceptance record(s) in billing_event.merchant_acceptance")
        for acceptance in acceptances[:5]:  # Show first 5
            print(f"\n  Agreement Type: {acceptance.agreement_type}")
            print(f"  Action: {acceptance.action}")
            print(f"  Created: {acceptance.acceptance_created_datetime}")
            print(f"  Deleted: {acceptance.acceptance_deleted_datetime}")
    else:
        print("\n❌ No acceptance records found in billing_event.merchant_acceptance")


def main() -> None:
    """Main exploration function."""
    print("\n")
    print("🌟 " * 40)
    print("MERCHANT TERMS ACCEPTANCE EXPLORATION")
    print("🌟 " * 40)

    # Explore both tables
    explore_billing_event_merchant_acceptance()
    explore_billing_merchant_terms_acceptance()

    # Recommendations
    print("\n\n")
    print("=" * 80)
    print("💡 RECOMMENDATIONS")
    print("=" * 80)
    print("""
Based on exploration, here's what we learned:

1. **Primary Table**: billing_event.merchant_acceptance appears to be the main table
   - Contains detailed state tracking (ACCEPTED, REVOKED, STALE, etc.)
   - Links merchant_uuid to acceptance_id and agreement_id
   - Tracks agreement_type (e.g., "BILLING_TERMS", "DATA_PRIVACY", etc.)

2. **To Check If Merchant Has Accepted Terms**:
   Query billing_event.merchant_acceptance WHERE:
   - merchant_uuid = <merchant_uuid>
   - action = 'ACCEPTED'
   - acceptance_deleted_datetime IS NULL (not deleted)
   - agreement_type = <type> (e.g., "BILLING_TERMS")

3. **Agreement Types Found**:
   See statistics above for common agreement_type values

4. **Next Steps**:
   - Find API endpoint to accept terms (likely in a merchant or terms service)
   - Create fixture that checks if merchant has accepted terms
   - If not accepted, call API to accept terms
   - Verify acceptance in database

5. **Test Pattern**:
   ```python
   # Check if accepted
   acceptance = environment.db.billing_event.select_first(
       select(MerchantAcceptance)
       .where(MerchantAcceptance.merchant_uuid == merchant_uuid)
       .where(MerchantAcceptance.action == "ACCEPTED")
       .where(MerchantAcceptance.acceptance_deleted_datetime.is_(None))
   )

   if not acceptance:
       # Accept terms via API
       response = environment.api.????.accept_merchant_terms(...)
   ```
""")


if __name__ == "__main__":
    main()
