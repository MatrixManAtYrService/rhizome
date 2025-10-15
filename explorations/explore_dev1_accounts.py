#!/usr/bin/env python3
"""
Quick script to find valid owner accounts in dev1 meta database.
"""

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.dev.meta import DevMeta
from rhizome.models.meta.account import Account as AccountModel
from rhizome.models.meta.reseller import Reseller as ResellerModel


def main():
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)

    Account = meta_db.get_versioned(AccountModel)
    Reseller = meta_db.get_versioned(ResellerModel)

    # Get some resellers with their owner account IDs
    print("Sample resellers with owner accounts:")
    resellers = meta_db.select_all(
        select(Reseller)
        .where(Reseller.owner_account_id.is_not(None))  # type: ignore
        .limit(10),
        sanitize=False,
    )

    for r in resellers:
        print(f"  Reseller: {r.name} (uuid={r.uuid})")
        print(f"    Owner Account ID: {r.owner_account_id}")

        # Try to get the account details
        if r.owner_account_id:
            account = meta_db.select_first(
                select(Account).where(Account.id == r.owner_account_id),
                sanitize=False,
            )
            if account:
                print(f"    Owner Email: {account.email}")
            else:
                print(f"    ⚠️  Account {r.owner_account_id} not found in account table")
        print()

    # Get a commonly used account
    print("\nLooking for test/demo accounts:")
    test_accounts = meta_db.select_all(
        select(Account)
        .where(Account.email.like("%test%") | Account.email.like("%demo%"))  # type: ignore
        .limit(5),
        sanitize=False,
    )

    for acc in test_accounts:
        print(f"  ID: {acc.id}, Email: {acc.email}")


if __name__ == "__main__":
    main()
