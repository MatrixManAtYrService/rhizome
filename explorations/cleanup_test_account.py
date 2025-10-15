#!/usr/bin/env python3
"""
Cleanup script to reverse test account creation operations.

This script deletes the test account and associated reseller_role entries
created during test runs. It uses the rhizome server's write_query endpoint
to prompt for user approval before executing each DELETE operation.

Usage:
    python cleanup_test_account.py [--email EMAIL]

The script will:
1. Find the account by email (default: mff_user@example.com)
2. Reset the account's primary_reseller_role_id to NULL
3. Delete all reseller_role entries for the account
4. Delete the account itself

Each operation requires user approval in the rhizome server terminal.
"""

import argparse
import sys

from rhizome.client import RhizomeClient
from rhizome.environments.dev.meta import DevMeta
from rhizome.models.meta.account import Account
from sqlmodel import select


def cleanup_test_account(email: str = "mff_user@example.com", dry_run: bool = False) -> None:
    """
    Clean up a test account and its associated reseller roles.

    Args:
        email: Email address of the account to clean up
        dry_run: If True, only show what would be deleted without executing
    """
    print(f"\n{'=' * 80}")
    print(f"{'DRY RUN - ' if dry_run else ''}Cleanup Test Account: {email}")
    print(f"{'=' * 80}\n")

    # Initialize clients
    rhizome_client = RhizomeClient(data_in_logs=False)
    meta_db = DevMeta(rhizome_client)

    # Step 1: Find the account
    print(f"1. Looking up account with email: {email}")
    AccountModel = meta_db.get_versioned(Account)
    account = meta_db.select_first(
        select(AccountModel).where(AccountModel.email == email),
        sanitize=False,
    )

    if not account:
        print(f"   ❌ No account found with email: {email}")
        print("\nNothing to clean up.")
        return

    if account.id is None:
        print("   ❌ Account has None id, cannot proceed")
        return

    account_id = account.id
    account_uuid = account.uuid
    primary_role_id = account.primary_reseller_role_id

    print(f"   ✅ Found account:")
    print(f"      - ID: {account_id}")
    print(f"      - UUID: {account_uuid}")
    print(f"      - Email: {account.email}")
    print(f"      - Name: {account.name}")
    print(f"      - Primary reseller role ID: {primary_role_id}")

    # Step 2: Find reseller_role entries
    print(f"\n2. Finding reseller_role entries for account_id={account_id}")
    ResellerRole = meta_db.get_versioned(meta_db.ResellerRole)
    reseller_roles = meta_db.select_all(
        select(ResellerRole).where(ResellerRole.account_id == account_id),
        sanitize=False,
    )

    if reseller_roles:
        print(f"   ✅ Found {len(reseller_roles)} reseller_role(s):")
        for role in reseller_roles:
            print(f"      - reseller_role_id={role.id}, reseller_id={role.reseller_id}, permissions_id={role.permissions_id}")
    else:
        print("   ℹ️  No reseller_role entries found")

    if dry_run:
        print("\n" + "=" * 80)
        print("DRY RUN - Operations that would be executed:")
        print("=" * 80)
        if primary_role_id is not None:
            print(f"\n1. UPDATE account SET primary_reseller_role_id = NULL WHERE id = {account_id}")
        for role in reseller_roles:
            print(f"2. DELETE FROM reseller_role WHERE id = {role.id}")
        print(f"3. DELETE FROM account WHERE id = {account_id}")
        print("\nRun without --dry-run to execute these operations.")
        return

    # Step 3: Reset primary_reseller_role_id to NULL (if set)
    if primary_role_id is not None:
        print(f"\n3. Resetting primary_reseller_role_id to NULL for account_id={account_id}")
        print("   ⚠️  This requires user approval in the rhizome server terminal")

        result = rhizome_client.execute_write_query(
            query_name="reset_account_primary_role",
            environment_name="dev_meta",
            params={"account_id": account_id},
            reason="Clean up: Reset primary role before deleting reseller_role and account",
            entity_descriptions={
                f"account_id_{account_id}": f"{account.name} ({account.email})",
                f"role_id_{primary_role_id}": f"Current primary role being removed",
            },
        )

        if not result["executed"]:
            print(f"   ❌ Failed: approved={result.get('approved')}, error={result.get('error')}")
            print("\nAborting cleanup.")
            return
        print("   ✅ Primary role reset successfully")
    else:
        print("\n3. Skipping primary role reset (already NULL)")

    # Step 4: Delete reseller_role entries
    if reseller_roles:
        print(f"\n4. Deleting {len(reseller_roles)} reseller_role(s)")
        for i, role in enumerate(reseller_roles, 1):
            print(f"   Deleting reseller_role {i}/{len(reseller_roles)} (id={role.id})...")
            print("   ⚠️  This requires user approval in the rhizome server terminal")

            result = rhizome_client.execute_write_query(
                query_name="delete_reseller_role",
                environment_name="dev_meta",
                params={"reseller_role_id": role.id},
                reason=f"Clean up: Remove reseller_role association {i}/{len(reseller_roles)} for test account",
                entity_descriptions={
                    f"role_id_{role.id}": f"reseller_role linking account_id={account_id} to reseller_id={role.reseller_id}",
                    f"account_id_{account_id}": f"{account.name} ({account.email})",
                    f"reseller_id_{role.reseller_id}": "Reseller this role grants permissions for",
                },
            )

            if not result["executed"]:
                print(f"   ❌ Failed: approved={result.get('approved')}, error={result.get('error')}")
                print("\nAborting cleanup.")
                return
            print(f"   ✅ Deleted reseller_role {role.id}")
    else:
        print("\n4. No reseller_role entries to delete")

    # Step 5: Delete the account
    print(f"\n5. Deleting account (id={account_id}, email={email})")
    print("   ⚠️  This requires user approval in the rhizome server terminal")

    result = rhizome_client.execute_write_query(
        query_name="delete_account",
        environment_name="dev_meta",
        params={"account_id": account_id},
        reason="Clean up: Remove test account after all associated roles have been deleted",
        entity_descriptions={
            f"account_id_{account_id}": f"{account.name} ({account.email}) - UUID: {account_uuid}",
        },
    )

    if not result["executed"]:
        print(f"   ❌ Failed: approved={result.get('approved')}, error={result.get('error')}")
        print("\nAccount deletion failed but partial cleanup may have occurred.")
        return

    print("   ✅ Account deleted successfully")

    print("\n" + "=" * 80)
    print("✅ CLEANUP COMPLETE")
    print("=" * 80)
    print(f"\nDeleted account {account_uuid} ({email}) and all associated reseller roles.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean up test account created during test runs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Clean up the default MFF test account
  python cleanup_test_account.py

  # Clean up a specific account
  python cleanup_test_account.py --email test@example.com

  # Dry run to see what would be deleted
  python cleanup_test_account.py --dry-run
        """,
    )
    parser.add_argument(
        "--email",
        default="mff_user@example.com",
        help="Email address of the account to clean up (default: mff_user@example.com)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be deleted without executing",
    )

    args = parser.parse_args()

    try:
        cleanup_test_account(email=args.email, dry_run=args.dry_run)
    except KeyboardInterrupt:
        print("\n\n⚠️  Cleanup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during cleanup: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
