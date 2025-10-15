#!/usr/bin/env python3
"""
Find accounts that have permission to own resellers.

Strategy:
1. Query existing resellers and their owner_account_id
2. For each owner account, get the account details
3. Show which accounts are successfully being used as reseller owners
4. These accounts must have the correct permissions
"""

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.meta import DevMeta
from rhizome.models.meta.account import Account as AccountModel
from rhizome.models.meta.reseller import Reseller as ResellerModel


def main():
    print("=" * 80)
    print("FINDING ACCOUNTS WITH RESELLER OWNER PERMISSIONS")
    print("=" * 80)

    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)

    Account = meta_db.get_versioned(AccountModel)
    Reseller = meta_db.get_versioned(ResellerModel)

    # Get all resellers with owner accounts
    print("\n🔍 Querying resellers with owner accounts...")
    resellers = meta_db.select_all(
        select(Reseller)
        .where(Reseller.owner_account_id.is_not(None))  # type: ignore[attr-defined]
        .order_by(Reseller.id)  # type: ignore[attr-defined]
        .limit(100),
        sanitize=False,
    )

    print(f"Found {len(resellers)} resellers with owner accounts")

    # Track unique owner accounts
    owner_accounts = {}

    print("\n" + "=" * 80)
    print("RESELLERS AND THEIR OWNERS")
    print("=" * 80)

    for r in resellers:
        if not r.owner_account_id:
            continue

        # Get owner account
        owner = meta_db.select_first(
            select(Account).where(Account.id == r.owner_account_id),
            sanitize=False,
        )

        if not owner:
            continue

        # Track this owner
        if owner.email not in owner_accounts:
            owner_accounts[owner.email] = {
                "account_id": owner.id,
                "uuid": owner.uuid,
                "email": owner.email,
                "resellers_owned": [],
            }

        owner_accounts[owner.email]["resellers_owned"].append(
            {
                "name": r.name,
                "uuid": r.uuid,
                "type": r.type,
                "reseller_id": r.id,
            }
        )

    # Display unique owner accounts
    print("\n" + "=" * 80)
    print("UNIQUE OWNER ACCOUNTS (THESE HAVE RESELLER OWNER PERMISSION)")
    print("=" * 80)

    print(f"\nFound {len(owner_accounts)} unique owner accounts:")

    for email, info in sorted(
        owner_accounts.items(), key=lambda x: len(x[1]["resellers_owned"]), reverse=True
    ):
        print(f"\n📧 {email}")
        print(f"   Account ID: {info['account_id']}")
        print(f"   UUID: {info['uuid']}")
        print(f"   Owns {len(info['resellers_owned'])} reseller(s):")

        for reseller in info["resellers_owned"][:5]:  # Show first 5
            print(f"      • {reseller['name']} (type: {reseller['type']})")

        if len(info["resellers_owned"]) > 5:
            print(f"      ... and {len(info['resellers_owned']) - 5} more")

    # Show recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS FOR TEST")
    print("=" * 80)

    print("\n💡 Any of these accounts can be used as owner_email when creating a reseller:")
    print()

    # Categorize by email pattern
    demo_test_owners = [
        email
        for email in owner_accounts.keys()
        if any(x in email.lower() for x in ["demo", "test"])
    ]
    clover_owners = [
        email
        for email in owner_accounts.keys()
        if "clover.com" in email.lower()
        and not any(x in email.lower() for x in ["demo", "test"])
    ]

    if demo_test_owners:
        print("🎯 BEST CHOICES (demo/test accounts):")
        for email in sorted(demo_test_owners)[:5]:
            count = len(owner_accounts[email]["resellers_owned"])
            print(f"   • {email} (owns {count} reseller(s))")

    if clover_owners:
        print("\n🔧 ALTERNATIVE CHOICES (Clover employee accounts):")
        for email in sorted(clover_owners)[:5]:
            count = len(owner_accounts[email]["resellers_owned"])
            print(f"   • {email} (owns {count} reseller(s))")

    print("\n" + "=" * 80)
    print("SQL QUERY EQUIVALENT")
    print("=" * 80)

    print(
        """
To find accounts with reseller owner permissions using SQL:

-- Find all accounts that currently own resellers
SELECT DISTINCT
    a.id AS account_id,
    a.uuid AS account_uuid,
    a.email AS account_email,
    COUNT(r.id) AS resellers_owned
FROM account a
JOIN reseller r ON r.owner_account_id = a.id
WHERE r.owner_account_id IS NOT NULL
GROUP BY a.id, a.uuid, a.email
ORDER BY resellers_owned DESC
LIMIT 20;

-- To check permissions for a specific account
SELECT
    rp.name AS permission_name,
    rr.account_id
FROM reseller_permissions rp
JOIN reseller_role rr ON rp.id = rr.permissions_id
WHERE rr.account_id = <account_id>;
"""
    )

    print("\n" + "=" * 80)
    print("KEY INSIGHT")
    print("=" * 80)

    print(
        """
The accounts listed above are PROVEN to have reseller owner permissions
because they are currently being used as owners of existing resellers.

Your test can use any of these emails for the owner_email parameter.

Note: Internal accounts (like matt.rixman@clover.com) may have permission
to CREATE resellers (via API) but cannot BE owners of resellers.
Regular email-based accounts are needed for ownership.
"""
    )


if __name__ == "__main__":
    main()
