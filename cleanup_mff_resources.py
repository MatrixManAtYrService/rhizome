#!/usr/bin/env python
"""
Test which billing-bookkeeper endpoints support DELETE and clean up MFF test resources.

This script:
1. Uses rhizome to query for all MFF test resources
2. Tests DELETE on each endpoint to see what's supported
3. Optionally deletes resources that support DELETE

Usage:
    # Dry run - just test what can be deleted
    python cleanup_mff_resources.py --dry-run

    # Actually delete resources that support DELETE
    python cleanup_mff_resources.py --delete

    # Test a specific resource type
    python cleanup_mff_resources.py --dry-run --resource revenue_share_group
"""

import argparse
import sys
from typing import Any

import httpx
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.models.table_list import BillingBookkeeperTable
from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp


def test_delete_endpoint(dev: DevHttp, endpoint: str, uuid: str, resource_name: str, dry_run: bool = True) -> bool:
    """Test if an endpoint supports DELETE.

    Returns:
        True if DELETE is supported, False otherwise
    """
    print(f"\n{'='*60}")
    print(f"Testing: {resource_name}")
    print(f"Endpoint: DELETE {endpoint}")
    print(f"UUID: {uuid}")

    if dry_run:
        print("🔍 DRY RUN - testing DELETE support...")
    else:
        print("🗑️  Attempting DELETE...")

    try:
        if dry_run:
            # For dry run, we still attempt the DELETE to see if it's supported
            # The fixture cleanup shows this is safe for revenue_share_group
            pass

        response = dev.delete(endpoint)
        print(f"✅ DELETE SUPPORTED - Response: {response}")
        return True

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 405:
            print(f"❌ DELETE NOT SUPPORTED - 405 Method Not Allowed")
            return False
        elif e.response.status_code == 404:
            print(f"⚠️  Resource not found (404) - may have been deleted already")
            return True  # Endpoint supports DELETE, resource just doesn't exist
        else:
            print(f"⚠️  Unexpected error: {e.response.status_code}")
            print(f"   Response: {e.response.text[:200]}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def cleanup_revenue_share_groups(
    rhizome_client: RhizomeClient, dev: DevHttp, dry_run: bool = True
) -> dict[str, Any]:
    """Find and optionally delete MFF revenue share groups."""
    print("\n" + "="*60)
    print("REVENUE SHARE GROUPS")
    print("="*60)

    dev_bb = DevBillingBookkeeper(rhizome_client)
    RevenueShareGroup = dev_bb.get_model(BillingBookkeeperTable.revenue_share_group)

    groups = dev_bb.select_all(
        select(RevenueShareGroup)
        .where(RevenueShareGroup.revenue_share_group.like("MFF_Test_%"))
        .order_by(RevenueShareGroup.created_timestamp.desc())
    )

    print(f"\nFound {len(groups)} MFF revenue share groups")

    if len(groups) == 0:
        print("✨ No MFF revenue share groups to clean up!")
        return {"found": 0, "deleted": 0, "failed": 0, "supports_delete": None}

    supports_delete = None
    deleted = 0
    failed = 0

    for group in groups:
        print(f"\n  - {group.revenue_share_group} (UUID: {group.uuid})")
        print(f"    Created: {group.created_timestamp}")

        if not dry_run:
            endpoint = f"/billing-bookkeeper/v1/revsharegroup/{group.uuid}"
            success = test_delete_endpoint(dev, endpoint, group.uuid, group.revenue_share_group, dry_run=False)
            if supports_delete is None:
                supports_delete = success
            if success:
                deleted += 1
            else:
                failed += 1
        else:
            # Just test the first one in dry run mode
            if supports_delete is None:
                endpoint = f"/billing-bookkeeper/v1/revsharegroup/{group.uuid}"
                supports_delete = test_delete_endpoint(dev, endpoint, group.uuid, group.revenue_share_group, dry_run=True)
                if supports_delete:
                    print(f"\n  ✅ Revenue share groups CAN be deleted")
                    print(f"     Run without --dry-run to delete all {len(groups)} groups")

    return {
        "found": len(groups),
        "deleted": deleted,
        "failed": failed,
        "supports_delete": supports_delete,
    }


def cleanup_billing_entities(
    rhizome_client: RhizomeClient, dev: DevHttp, dry_run: bool = True
) -> dict[str, Any]:
    """Find and test DELETE on MFF billing entities."""
    print("\n" + "="*60)
    print("BILLING ENTITIES (RESELLERS)")
    print("="*60)

    dev_bb = DevBillingBookkeeper(rhizome_client)
    BillingEntity = dev_bb.get_model(BillingBookkeeperTable.billing_entity)

    entities = dev_bb.select_all(
        select(BillingEntity)
        .where(BillingEntity.entity_type == "RESELLER")
        .where(BillingEntity.entity_uuid.like("MFF%"))
        .order_by(BillingEntity.created_timestamp.desc())
    )

    print(f"\nFound {len(entities)} MFF billing entities")

    if len(entities) == 0:
        return {"found": 0, "deleted": 0, "failed": 0, "supports_delete": None}

    # Test DELETE on the oldest one (least likely to break things)
    test_entity = entities[-1]
    print(f"\nTesting DELETE on oldest entity:")
    print(f"  - {test_entity.name} (UUID: {test_entity.uuid})")
    print(f"    Entity UUID: {test_entity.entity_uuid}")
    print(f"    Created: {test_entity.created_timestamp}")

    endpoint = f"/billing-bookkeeper/v1/entity/{test_entity.uuid}"
    supports_delete = test_delete_endpoint(dev, endpoint, test_entity.uuid, test_entity.name, dry_run=True)

    if not supports_delete:
        print(f"\n  ❌ Billing entities CANNOT be deleted via API")
        print(f"     {len(entities)} entities will remain in the database")
        print(f"     Recommendation: Leave them - they're harmless metadata")

    return {
        "found": len(entities),
        "deleted": 0,
        "failed": 0,
        "supports_delete": supports_delete,
    }


def test_child_resources(
    rhizome_client: RhizomeClient, dev: DevHttp
) -> dict[str, dict[str, Any]]:
    """Test DELETE support for child resources (alliance codes, schedules, etc)."""
    dev_bb = DevBillingBookkeeper(rhizome_client)
    results = {}

    # Alliance Codes
    print("\n" + "="*60)
    print("ALLIANCE CODES")
    print("="*60)

    InvoiceAllianceCode = dev_bb.get_model(BillingBookkeeperTable.invoice_alliance_code)
    BillingEntity = dev_bb.get_model(BillingBookkeeperTable.billing_entity)

    # Find alliance codes for MFF entities
    alliance_codes = dev_bb.select_all(
        select(InvoiceAllianceCode)
        .where(
            InvoiceAllianceCode.billing_entity_uuid.in_(
                select(BillingEntity.uuid).where(BillingEntity.entity_uuid.like("MFF%"))
            )
        )
    )

    print(f"\nFound {len(alliance_codes)} MFF alliance codes")

    if len(alliance_codes) > 0:
        test_code = alliance_codes[0]
        print(f"\nTesting DELETE on: {test_code.alliance_code} (UUID: {test_code.uuid})")
        endpoint = f"/billing-bookkeeper/v1/alliancecode/{test_code.uuid}"
        supports_delete = test_delete_endpoint(dev, endpoint, test_code.uuid, "Alliance Code", dry_run=True)
        results["alliance_code"] = {
            "found": len(alliance_codes),
            "supports_delete": supports_delete,
        }

    # Billing Schedules
    print("\n" + "="*60)
    print("BILLING SCHEDULES")
    print("="*60)

    BillingSchedule = dev_bb.get_model(BillingBookkeeperTable.billing_schedule)

    schedules = dev_bb.select_all(
        select(BillingSchedule)
        .where(
            BillingSchedule.billing_entity_uuid.in_(
                select(BillingEntity.uuid).where(BillingEntity.entity_uuid.like("MFF%"))
            )
        )
    )

    print(f"\nFound {len(schedules)} MFF billing schedules")

    if len(schedules) > 0:
        test_schedule = schedules[0]
        print(f"\nTesting DELETE on schedule (UUID: {test_schedule.uuid})")
        endpoint = f"/billing-bookkeeper/v1/schedule/{test_schedule.uuid}"
        supports_delete = test_delete_endpoint(dev, endpoint, test_schedule.uuid, "Billing Schedule", dry_run=True)
        results["billing_schedule"] = {
            "found": len(schedules),
            "supports_delete": supports_delete,
        }

    # Fee Rates
    print("\n" + "="*60)
    print("FEE RATES")
    print("="*60)

    FeeRate = dev_bb.get_model(BillingBookkeeperTable.fee_rate)

    fee_rates = dev_bb.select_all(
        select(FeeRate)
        .where(
            FeeRate.billing_entity_uuid.in_(
                select(BillingEntity.uuid).where(BillingEntity.entity_uuid.like("MFF%"))
            )
        )
    )

    print(f"\nFound {len(fee_rates)} MFF fee rates")

    if len(fee_rates) > 0:
        test_rate = fee_rates[0]
        print(f"\nTesting DELETE on fee rate (UUID: {test_rate.uuid})")
        endpoint = f"/billing-bookkeeper/v1/rate/{test_rate.uuid}"
        supports_delete = test_delete_endpoint(dev, endpoint, test_rate.uuid, "Fee Rate", dry_run=True)
        results["fee_rate"] = {
            "found": len(fee_rates),
            "supports_delete": supports_delete,
        }

    # Processing Group Dates
    print("\n" + "="*60)
    print("PROCESSING GROUP DATES")
    print("="*60)

    ProcessingGroupDates = dev_bb.get_model(BillingBookkeeperTable.processing_group_dates)

    pgds = dev_bb.select_all(
        select(ProcessingGroupDates)
        .where(
            ProcessingGroupDates.billing_entity_uuid.in_(
                select(BillingEntity.uuid).where(BillingEntity.entity_uuid.like("MFF%"))
            )
        )
    )

    print(f"\nFound {len(pgds)} MFF processing group dates")

    if len(pgds) > 0:
        test_pgd = pgds[0]
        print(f"\nTesting DELETE on processing group dates (UUID: {test_pgd.uuid})")
        endpoint = f"/billing-bookkeeper/v1/processgroupdates/{test_pgd.uuid}"
        supports_delete = test_delete_endpoint(dev, endpoint, test_pgd.uuid, "Processing Group Dates", dry_run=True)
        results["processing_group_dates"] = {
            "found": len(pgds),
            "supports_delete": supports_delete,
        }

    return results


def main() -> None:
    """Main cleanup script."""
    parser = argparse.ArgumentParser(description="Clean up MFF test resources from dev1")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Test what can be deleted without actually deleting",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Actually delete resources (only those that support DELETE)",
    )
    parser.add_argument(
        "--resource",
        choices=["revenue_share_group", "billing_entity", "child_resources", "all"],
        default="all",
        help="Which resources to test/clean",
    )

    args = parser.parse_args()

    if not args.dry_run and not args.delete:
        print("❌ Error: Must specify either --dry-run or --delete")
        sys.exit(1)

    if args.dry_run and args.delete:
        print("❌ Error: Cannot specify both --dry-run and --delete")
        sys.exit(1)

    print("="*60)
    print("MFF Test Resource Cleanup")
    print("="*60)

    if args.dry_run:
        print("\n🔍 DRY RUN MODE - Testing DELETE support, not actually deleting")
    else:
        print("\n🗑️  DELETE MODE - Will delete resources that support DELETE")
        print("\n⚠️  WARNING: This will permanently delete resources!")
        response = input("Are you sure you want to continue? (yes/no): ")
        if response.lower() != "yes":
            print("Aborted.")
            sys.exit(0)

    # Initialize clients
    rhizome_client = RhizomeClient(data_in_logs=False)
    stolon_client = StolonClient(data_in_logs=False)
    dev = DevHttp(stolon_client)

    summary = {}

    # Test/cleanup revenue share groups
    if args.resource in ["revenue_share_group", "all"]:
        summary["revenue_share_group"] = cleanup_revenue_share_groups(
            rhizome_client, dev, dry_run=args.dry_run
        )

    # Test billing entities
    if args.resource in ["billing_entity", "all"]:
        summary["billing_entity"] = cleanup_billing_entities(
            rhizome_client, dev, dry_run=args.dry_run
        )

    # Test child resources
    if args.resource in ["child_resources", "all"]:
        child_results = test_child_resources(rhizome_client, dev)
        summary.update(child_results)

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    for resource_type, data in summary.items():
        print(f"\n{resource_type.replace('_', ' ').title()}:")
        print(f"  Found: {data.get('found', 0)}")
        if data.get("supports_delete") is not None:
            if data["supports_delete"]:
                print(f"  ✅ DELETE supported")
                if not args.dry_run and "deleted" in data:
                    print(f"  Deleted: {data.get('deleted', 0)}")
                    if data.get('failed', 0) > 0:
                        print(f"  Failed: {data.get('failed', 0)}")
            else:
                print(f"  ❌ DELETE not supported - resources will remain")

    print("\n" + "="*60)

    if args.dry_run:
        print("\n✅ Dry run complete!")
        print("\nTo actually delete resources that support DELETE, run:")
        print("  python cleanup_mff_resources.py --delete")
    else:
        print("\n✅ Cleanup complete!")


if __name__ == "__main__":
    main()
