"""
Explore merchant plan groups and plans in dev1 to find reasonable defaults.

This script examines existing merchant plan groups, their associated plans,
and the resellers that use them to identify reasonable defaults for test fixtures.

Usage:
    python explore_merchant_plan_groups.py
"""

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.meta import DevMeta
from rhizome.models.meta.merchant_plan import MerchantPlan as MerchantPlanModel
from rhizome.models.meta.merchant_plan_group import MerchantPlanGroup as MerchantPlanGroupModel
from rhizome.models.meta.reseller import Reseller as ResellerModel


def explore_plan_groups_and_resellers():
    """Explore merchant plan groups and which resellers use them."""
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)

    MerchantPlanGroup = meta_db.get_versioned(MerchantPlanGroupModel)
    MerchantPlan = meta_db.get_versioned(MerchantPlanModel)
    Reseller = meta_db.get_versioned(ResellerModel)

    print("\n" + "=" * 80)
    print("MERCHANT PLAN GROUPS IN DEV1")
    print("=" * 80)

    # Get all non-deleted plan groups
    plan_groups = meta_db.select_all(
        select(MerchantPlanGroup)
        .where(MerchantPlanGroup.deleted_time.is_(None))  # type: ignore[attr-defined]
        .order_by(MerchantPlanGroup.id),  # type: ignore[attr-defined]
        sanitize=False,
    )

    print(f"\nFound {len(plan_groups)} active merchant plan groups\n")

    for plan_group in plan_groups[:10]:  # Show first 10
        print(f"Plan Group: {plan_group.name}")
        print(f"  ID: {plan_group.id}")
        print(f"  UUID: {plan_group.uuid}")
        print(f"  Enforce Assignment: {plan_group.enforce_assignment}")
        print(f"  Linkable: {plan_group.linkable}")
        print(f"  Trial Days: {plan_group.trial_days}")

        # Count resellers using this plan group
        resellers_with_group = meta_db.select_all(
            select(Reseller).where(Reseller.plan_group_id == plan_group.id), sanitize=False
        )
        print(f"  Resellers using this group: {len(resellers_with_group)}")

        # Get plans in this group
        plans = meta_db.select_all(
            select(MerchantPlan)
            .where(MerchantPlan.merchant_plan_group_id == plan_group.id)
            .order_by(MerchantPlan.id),  # type: ignore[attr-defined]
            sanitize=False,
        )
        print(f"  Plans in this group: {len(plans)}")

        if plans:
            print("  Plan details:")
            for plan in plans[:3]:  # Show first 3 plans
                print(f"    - {plan.name}")
                print(f"      UUID: {plan.uuid}")
                print(f"      Type: {plan.type}")
                print(f"      Plan Code: {plan.plan_code}")
                print(f"      App Bundle ID: {plan.app_bundle_id}")
                print(f"      Default Plan: {plan.default_plan}")
                print(f"      Hidden: {plan.hidden}")

        print()

    print("\n" + "=" * 80)
    print("SPECIFIC PLAN GROUP FROM URL")
    print("=" * 80)
    print("\nLooking at plan group: 22412CB9BEC6A")

    # Look at the specific plan group from the URL
    specific_group = meta_db.select_first(
        select(MerchantPlanGroup).where(MerchantPlanGroup.uuid == "22412CB9BEC6A"), sanitize=False
    )

    if specific_group:
        print(f"\n✓ Found plan group: {specific_group.name}")
        print(f"  ID: {specific_group.id}")
        print(f"  UUID: {specific_group.uuid}")
        print(f"  Enforce Assignment: {specific_group.enforce_assignment}")
        print(f"  Linkable: {specific_group.linkable}")
        print(f"  Trial Days: {specific_group.trial_days}")

        # Get the specific plan
        specific_plan = meta_db.select_first(
            select(MerchantPlan).where(MerchantPlan.uuid == "9D0AA9YZSN16M"), sanitize=False
        )

        if specific_plan:
            print(f"\n✓ Found plan: {specific_plan.name}")
            print(f"  UUID: {specific_plan.uuid}")
            print(f"  Type: {specific_plan.type}")
            print(f"  Plan Code: {specific_plan.plan_code}")
            print(f"  App Bundle ID: {specific_plan.app_bundle_id}")
            print(f"  Reseller ID: {specific_plan.reseller_id}")
            print(f"  Merchant Plan Group ID: {specific_plan.merchant_plan_group_id}")
            print(f"  Default Plan: {specific_plan.default_plan}")
            print(f"  Hidden: {specific_plan.hidden}")
            print(f"  Enforced: {specific_plan.enforced}")

        # Count resellers using this plan group
        resellers_using = meta_db.select_all(
            select(Reseller).where(Reseller.plan_group_id == specific_group.id), sanitize=False
        )
        print(f"\n  Resellers using this group: {len(resellers_using)}")
        if resellers_using:
            print("  Sample resellers:")
            for reseller in resellers_using[:5]:
                print(f"    - {reseller.name} (UUID: {reseller.uuid}, Type: {reseller.type})")

    else:
        print("\n✗ Plan group 22412CB9BEC6A not found in dev1")

    print("\n" + "=" * 80)
    print("RESELLERS WITHOUT PLAN GROUPS")
    print("=" * 80)

    # Check resellers without plan groups
    resellers_no_plan_group = meta_db.select_all(
        select(Reseller).where(Reseller.plan_group_id.is_(None)).limit(10),  # type: ignore[attr-defined]
        sanitize=False,
    )

    print(f"\nFound {len(resellers_no_plan_group)} resellers without plan_group_id (showing first 10)")
    for reseller in resellers_no_plan_group:
        print(f"  - {reseller.name} (UUID: {reseller.uuid}, Type: {reseller.type})")

    print("\n" + "=" * 80)
    print("MOST COMMONLY USED PLAN GROUPS")
    print("=" * 80)

    # Find the most commonly used plan groups
    all_resellers = meta_db.select_all(
        select(Reseller).where(Reseller.plan_group_id.is_not(None)),  # type: ignore[attr-defined]
        sanitize=False,
    )

    plan_group_usage = {}
    for reseller in all_resellers:
        plan_group_id = reseller.plan_group_id
        if plan_group_id not in plan_group_usage:
            plan_group_usage[plan_group_id] = []
        plan_group_usage[plan_group_id].append(reseller)

    print(f"\nTop 10 most used plan groups:")
    sorted_usage = sorted(plan_group_usage.items(), key=lambda x: len(x[1]), reverse=True)

    for plan_group_id, resellers in sorted_usage[:10]:
        plan_group = meta_db.select_first(
            select(MerchantPlanGroup).where(MerchantPlanGroup.id == plan_group_id), sanitize=False
        )
        if plan_group:
            print(f"\n{plan_group.name} (UUID: {plan_group.uuid})")
            print(f"  Used by {len(resellers)} resellers")

            # Get plans in this group
            plans = meta_db.select_all(
                select(MerchantPlan).where(MerchantPlan.merchant_plan_group_id == plan_group.id), sanitize=False
            )
            print(f"  Contains {len(plans)} plans")

    print("\n" + "=" * 80)
    print("RECOMMENDATIONS FOR TEST FIXTURES")
    print("=" * 80)

    print("""
Based on the exploration above, here are recommendations for test fixtures:

1. OPTION 1: Use an existing plan group with plans
   - Pick a commonly used plan group from the list above
   - This avoids creating new resources
   - Will work immediately in dev1

2. OPTION 2: Create a minimal test plan group
   - POST /v3/merchant_plan_groups with just {"name": "MFF Test Plan Group"}
   - Then POST /v3/merchant_plan_groups/{id}/merchant_plans with:
     {"name": "MFF Test Plan", "planCode": "MFF_TEST"}
   - This gives full control but creates new resources

3. OPTION 3: Allow null plan_group_id
   - Many resellers don't have a plan_group_id
   - Check if the API allows creating resellers without one
   - Simplest approach if supported

For testing purposes, OPTION 2 is recommended because:
- It gives full control over the test data
- It's isolated from production/demo data
- It can be created once and reused (like the MFF prefix resources)
""")


if __name__ == "__main__":
    explore_plan_groups_and_resellers()
