#!/usr/bin/env python3
"""
Explore demo2 resellers and their relationship to billing entities.

This script helps understand:
1. What resellers exist in demo2's meta database
2. How they link to billing_bookkeeper.billing_entity via entity_uuid
3. The naming patterns and structure we should emulate in dev1 tests
"""

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.demo.meta import DemoMeta
from rhizome.models.billing_bookkeeper.billing_entity import BillingEntity as BillingEntityModel
from rhizome.models.meta.reseller import Reseller as ResellerModel


def main():
    print("=" * 80)
    print("DEMO2 RESELLER EXPLORATION")
    print("=" * 80)

    # Initialize clients
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DemoMeta(rhizome_client)
    billing_db = DemoBillingBookkeeper(rhizome_client)

    # Get versioned models
    Reseller = meta_db.get_versioned(ResellerModel)
    BillingEntity = billing_db.get_versioned(BillingEntityModel)

    # Query all resellers
    print("\n" + "=" * 80)
    print("RESELLERS IN DEMO2 META DATABASE")
    print("=" * 80)

    resellers = meta_db.select_all(
        select(Reseller)
        .order_by(Reseller.id)  # type: ignore[attr-defined]
        .limit(50),  # Reasonable limit to avoid too much output
        sanitize=False,
    )

    print(f"\nFound {len(resellers)} resellers:")
    print(f"\n{'ID':<8} {'UUID':<15} {'Type':<12} {'Name':<40}")
    print("-" * 80)
    for r in resellers:
        name_truncated = (r.name[:37] + "...") if len(r.name) > 40 else r.name
        reseller_type = r.type if r.type else "None"
        print(f"{r.id:<8} {r.uuid:<15} {reseller_type:<12} {name_truncated:<40}")

    # Query billing entities with entity_type = RESELLER
    print("\n" + "=" * 80)
    print("BILLING ENTITIES (TYPE=RESELLER) IN DEMO2")
    print("=" * 80)

    billing_entities = billing_db.select_all(
        select(BillingEntity)
        .where(BillingEntity.entity_type == "RESELLER")
        .order_by(BillingEntity.created_timestamp)  # type: ignore[attr-defined]
        .limit(50),
        sanitize=False,
    )

    print(f"\nFound {len(billing_entities)} billing entities with entity_type=RESELLER:")
    print(f"\n{'Billing UUID':<28} {'Entity UUID':<15} {'Name':<40}")
    print("-" * 80)
    for be in billing_entities:
        name_truncated = (be.name[:37] + "...") if len(be.name) > 40 else be.name
        print(f"{be.uuid:<28} {be.entity_uuid:<15} {name_truncated:<40}")

    # Now find the relationships
    print("\n" + "=" * 80)
    print("RELATIONSHIP: META.RESELLER → BILLING_BOOKKEEPER.BILLING_ENTITY")
    print("=" * 80)
    print("\nLinking pattern: billing_entity.entity_uuid = reseller.uuid")
    print("\nMatched pairs:")
    print(f"\n{'Reseller UUID':<15} {'Reseller Name':<40} {'Billing Entity UUID':<28}")
    print("-" * 80)

    # Create a map of entity_uuid to billing_entity
    entity_map = {be.entity_uuid: be for be in billing_entities}

    matched_count = 0
    unmatched_resellers = []

    for r in resellers:
        if r.uuid in entity_map:
            matched_count += 1
            be = entity_map[r.uuid]
            name_truncated = (r.name[:37] + "...") if len(r.name) > 40 else r.name
            print(f"{r.uuid:<15} {name_truncated:<40} {be.uuid:<28}")
        else:
            unmatched_resellers.append(r)

    print(f"\n✓ {matched_count} resellers have matching billing entities")

    if unmatched_resellers:
        print(f"\n⚠️  {len(unmatched_resellers)} resellers WITHOUT billing entities:")
        print(f"\n{'Reseller UUID':<15} {'Type':<12} {'Name':<40}")
        print("-" * 80)
        for r in unmatched_resellers[:20]:  # Limit to first 20
            name_truncated = (r.name[:37] + "...") if len(r.name) > 40 else r.name
            reseller_type = r.type if r.type else "None"
            print(f"{r.uuid:<15} {reseller_type:<12} {name_truncated:<40}")
        if len(unmatched_resellers) > 20:
            print(f"... and {len(unmatched_resellers) - 20} more")

    # Orphaned billing entities (entity_uuid doesn't match any reseller)
    reseller_uuid_set = {r.uuid for r in resellers}
    orphaned_entities = [be for be in billing_entities if be.entity_uuid not in reseller_uuid_set]

    if orphaned_entities:
        print(f"\n⚠️  {len(orphaned_entities)} billing entities WITHOUT matching resellers:")
        print(f"\n{'Billing UUID':<28} {'Entity UUID':<15} {'Name':<40}")
        print("-" * 80)
        for be in orphaned_entities[:20]:  # Limit to first 20
            name_truncated = (be.name[:37] + "...") if len(be.name) > 40 else be.name
            print(f"{be.uuid:<28} {be.entity_uuid:<15} {name_truncated:<40}")
        if len(orphaned_entities) > 20:
            print(f"... and {len(orphaned_entities) - 20} more")

    # Look for test/demo pattern resellers
    print("\n" + "=" * 80)
    print("RESELLERS WITH TEST/DEMO/PREFIX PATTERNS")
    print("=" * 80)

    test_patterns = ["Test", "test", "TEST", "Demo", "demo", "DEMO", "MFF", "TST", "DEV"]
    print(f"\nSearching for resellers containing: {', '.join(test_patterns)}")

    for pattern in test_patterns:
        pattern_resellers = meta_db.select_all(
            select(Reseller)
            .where(Reseller.name.like(f"%{pattern}%"))  # type: ignore[attr-defined]
            .order_by(Reseller.id)  # type: ignore[attr-defined]
            .limit(10),
            sanitize=False,
        )

        if pattern_resellers:
            print(f"\n  Pattern '{pattern}': {len(pattern_resellers)} found")
            for r in pattern_resellers[:5]:  # Show first 5
                has_billing = "✓" if r.uuid in entity_map else "✗"
                print(f"    [{has_billing}] {r.uuid} - {r.name}")
            if len(pattern_resellers) > 5:
                print(f"    ... and {len(pattern_resellers) - 5} more")

    # Sample detailed reseller info
    print("\n" + "=" * 80)
    print("SAMPLE RESELLER DETAIL (First reseller with billing entity)")
    print("=" * 80)

    sample_reseller = next((r for r in resellers if r.uuid in entity_map), None)
    if sample_reseller:
        print("\n📋 Reseller (from meta.reseller):")
        print(f"  ID: {sample_reseller.id}")
        print(f"  UUID: {sample_reseller.uuid}")
        print(f"  Name: {sample_reseller.name}")
        print(f"  Type: {sample_reseller.type}")
        print(f"  Parent ID: {sample_reseller.parent_id}")
        print(f"  Plan Group ID: {sample_reseller.plan_group_id}")
        print(f"  Owner Account ID: {sample_reseller.owner_account_id}")

        if sample_reseller.uuid in entity_map:
            be = entity_map[sample_reseller.uuid]
            print("\n💰 Linked Billing Entity (from billing_bookkeeper.billing_entity):")
            print(f"  Billing Entity UUID: {be.uuid}")
            print(f"  Entity UUID (link): {be.entity_uuid}")
            print(f"  Entity Type: {be.entity_type}")
            print(f"  Name: {be.name}")
            print(f"  Created: {be.created_timestamp}")

            print("\n🔗 Link verification:")
            print(f"  reseller.uuid == billing_entity.entity_uuid: {sample_reseller.uuid == be.entity_uuid}")

    # Summary recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS FOR DEV1 TEST")
    print("=" * 80)
    print("""
Based on demo2 structure:

1. CREATION ORDER:
   a. Create meta.reseller first (via API /v3/resellers)
   b. Create billing_bookkeeper.billing_entity with entity_uuid=reseller.uuid

2. NAMING PATTERN:
   - Use a prefix (e.g., "MFF", "TEST") at the start of the reseller name
   - Example: "MFF Test Reseller A1B2"
   - This allows finding existing test resellers with: WHERE name LIKE 'MFF%'

3. PARENT RESELLER:
   - Find a suitable parent reseller (type=DEMO or any existing reseller)
   - Use its UUID as parent_reseller_id when creating new reseller
   - Use its plan_group_id (or default to known good one)

4. REUSE STRATEGY:
   - Query for resellers with your prefix: WHERE name LIKE 'PREFIX%'
   - If found: reuse it (check if billing_entity exists too)
   - If not found: create new reseller + billing_entity
   - Changing prefix = new reseller = tests full creation flow

5. LINKING:
   - Always verify: billing_entity.entity_uuid == reseller.uuid
   - This is the critical link between the two systems
""")

    print("=" * 80)
    print("END OF EXPLORATION")
    print("=" * 80)


if __name__ == "__main__":
    main()
