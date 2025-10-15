#!/usr/bin/env python3
"""
Explore dev1 resellers and their owner accounts to find suitable candidates
for creating test resellers.

We need to find an owner account that has CREATE_RESELLER permission.
"""

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.meta import DevMeta
from rhizome.models.meta.account import Account as AccountModel
from rhizome.models.meta.reseller import Reseller as ResellerModel


def main():
    print("=" * 80)
    print("EXPLORING DEV1 RESELLERS AND OWNER ACCOUNTS")
    print("=" * 80)

    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)

    Account = meta_db.get_versioned(AccountModel)
    Reseller = meta_db.get_versioned(ResellerModel)

    # Get all resellers with owner accounts
    print("\n📋 Querying resellers with owner accounts...")
    resellers = meta_db.select_all(
        select(Reseller)
        .where(Reseller.owner_account_id.is_not(None))  # type: ignore[attr-defined]
        .order_by(Reseller.id)  # type: ignore[attr-defined]
        .limit(50),
        sanitize=False,
    )

    print(f"Found {len(resellers)} resellers with owner accounts")

    # Note: We can't easily query reseller_role and reseller_permissions tables
    # without direct SQL access (RhizomeClient uses SQLModel, not raw queries)
    print("\n⚠️  Note: reseller_role and reseller_permissions require DB write access to query")
    print("   We'll identify candidates based on reseller name/type patterns")

    # Analyze resellers by type and name patterns
    print("\n" + "=" * 80)
    print("ANALYSIS: RESELLERS BY CATEGORY")
    print("=" * 80)

    categories = {
        "Demo/Test": [],
        "Clover": [],
        "Banks/Financial": [],
        "ISOs": [],
        "Other": [],
    }

    for r in resellers:
        if not r.name:
            continue

        name_lower = r.name.lower()
        if any(x in name_lower for x in ["demo", "test", "clover internal"]):
            categories["Demo/Test"].append(r)
        elif "clover" in name_lower:
            categories["Clover"].append(r)
        elif any(x in name_lower for x in ["bank", "wells", "pnc", "financial"]):
            categories["Banks/Financial"].append(r)
        elif "iso" in name_lower:
            categories["ISOs"].append(r)
        else:
            categories["Other"].append(r)

    for category, resellers_list in categories.items():
        if not resellers_list:
            continue

        print(f"\n{category} ({len(resellers_list)} resellers):")
        print(f"{'─' * 80}")

        for r in resellers_list[:10]:  # Show first 10
            # Get owner account
            owner = meta_db.select_first(
                select(Account).where(Account.id == r.owner_account_id),
                sanitize=False,
            )

            owner_email = owner.email if owner else "NOT FOUND"
            reseller_type = r.type if r.type else "UNKNOWN"

            print(f"\n  Reseller: {r.name}")
            print(f"    UUID: {r.uuid}, Type: {reseller_type}")
            print(f"    Owner: {owner_email} (account_id: {r.owner_account_id})")

        if len(resellers_list) > 10:
            print(f"\n  ... and {len(resellers_list) - 10} more")

    # Recommendation
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)

    print("\n💡 Best candidates for test reseller creation:")
    print("\n1. **Demo/Test resellers**: Likely have broad permissions")
    if categories["Demo/Test"]:
        top_demo = categories["Demo/Test"][0]
        owner = meta_db.select_first(
            select(Account).where(Account.id == top_demo.owner_account_id),
            sanitize=False,
        )
        print(f"   → {top_demo.name}")
        print(f"     Owner: {owner.email if owner else 'NOT FOUND'}")
        print(f"     Use in test: This account is most likely to have CREATE_RESELLER permission")

    print("\n2. **Clover resellers**: Official Clover accounts with admin permissions")
    if categories["Clover"]:
        top_clover = categories["Clover"][0]
        owner = meta_db.select_first(
            select(Account).where(Account.id == top_clover.owner_account_id),
            sanitize=False,
        )
        print(f"   → {top_clover.name}")
        print(f"     Owner: {owner.email if owner else 'NOT FOUND'}")

    print("\n📝 To use in your test:")
    print("   Update the test_owner_account fixture to specifically look for:")
    print("   1. Resellers with 'demo' or 'test' in the name (case insensitive)")
    print("   2. Then fall back to 'clover' resellers")
    print("   These are most likely to have CREATE_RESELLER permission")

    print("\n🔐 Permission Investigation (requires DB write access):")
    print("   mysql> SELECT rp.name FROM reseller_permissions rp")
    print("          JOIN reseller_role rr ON rp.id = rr.permissions_id")
    print("          WHERE rr.account_id = <account_id>;")


if __name__ == "__main__":
    main()
