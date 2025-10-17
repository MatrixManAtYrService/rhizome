"""Utilities for working with resellers and reseller owners."""

import asyncio
import json
import secrets
import uuid as uuid_module
from typing import TYPE_CHECKING, Any

import httpx
from sqlmodel import select

from rhizome.environments.base import SecretManager
from rhizome.environments.dev.meta import DevMeta
from rhizome.models.meta.account import Account
from rhizome.models.meta.reseller import Reseller
from trifolium.util.models import ResellerOwnerAccount

if TYPE_CHECKING:
    from trifolium.environments.dev import Environment


def create_reseller_owner(environment: "Environment") -> ResellerOwnerAccount:
    """
    Create or retrieve the MFF Reseller Owner account.

    This account has Super Administrator privileges for the Clover reseller
    and can be used to create test resellers. The function is idempotent -
    it checks if the account already exists before creating it.

    The account details are cached in ~/.trifolium/mff_user.json for quick reuse.

    Args:
        environment: A trifolium environment (e.g., from trifolium.environments.dev.Environment)
                    Must have ._rhizome_client and ._stolon_client attributes

    Returns:
        ResellerOwnerAccount with:
            - uuid: Account UUID
            - id: Account ID
            - email: Account email
            - name: Account name ("MFF User")

    Raises:
        Exception: If account creation fails or required resources don't exist
    """
    print("\n=== MFF Reseller Owner Account Setup ===")

    rhizome_client = environment.rhizome_client
    meta_db = DevMeta(rhizome_client)

    email = "mff_user@example.com"

    # Check if account already exists in database
    print(f"\n1. Checking if MFF Reseller Owner account ({email}) already exists...")
    AccountModel = meta_db.get_versioned(Account)
    existing_account = meta_db.select_first(
        select(AccountModel).where(AccountModel.email == email),
        sanitize=False,
    )

    if existing_account:
        print("   ✅ MFF Reseller Owner account already exists!")
        print(f"      UUID: {existing_account.uuid}")
        print(f"      ID: {existing_account.id}")
        print(f"      Email: {existing_account.email}")

        # Ensure required fields are not None
        if existing_account.id is None or existing_account.email is None:
            raise Exception("Existing account has None id or email, which should not happen")

        account_info = ResellerOwnerAccount(
            uuid=existing_account.uuid,
            id=existing_account.id,
            email=existing_account.email,
            name="MFF User",
        )

        # Save for reuse
        _save_account_info(existing_account.uuid, existing_account.id, existing_account.email)

        return account_info

    # Account doesn't exist, create it
    print("   ⚠️  MFF Reseller Owner account does not exist. Creating it now...")

    # Get Clover reseller ID
    print("\n2. Finding Clover reseller...")
    clover_reseller_id = _get_clover_reseller_id(meta_db)
    print(f"   ✅ Found Clover reseller (id={clover_reseller_id})")

    # Get Super Administrator role ID
    print("\n3. Finding Super Administrator role...")
    super_admin_role_id = _get_super_admin_role_id(meta_db, clover_reseller_id)
    print(f"   ✅ Found Super Administrator role (id={super_admin_role_id})")

    # Generate UUID and claim code
    print("\n4. Generating account credentials...")
    account_uuid = uuid_module.uuid4().hex.upper()[:13]  # 13 chars like Clover UUIDs
    claim_code = _generate_claim_code()
    print(f"   ✅ Generated UUID: {account_uuid}")
    print("   ✅ Generated claim code")

    # Get password from 1Password
    _, password = _get_credentials_from_1password(meta_db)

    # Create account
    print("\n5. Creating account...")
    print("   ⚠️  This requires user approval in the rhizome server terminal")
    account_result = rhizome_client.execute_write_query(
        query_name="create_account",
        database_id="dev_meta",
        params={
            "uuid": account_uuid,
            "name": "MFF User",
            "email": email,
            "claim_code": claim_code,
        },
        reason="Create the MFF Reseller Owner account for test reseller creation",
        entity_descriptions={
            f"account_uuid_{account_uuid}": "New MFF test account UUID",
            f"email_{email}": "MFF test account email address",
        },
    )

    if not account_result["executed"]:
        raise Exception(
            f"Account creation failed: approved={account_result.get('approved')}, error={account_result.get('error')}"
        )

    print("   ✅ Account created successfully")

    # Get the new account ID
    print("\n6. Retrieving new account ID...")
    new_account = meta_db.select_first(
        select(AccountModel).where(AccountModel.email == email),
        sanitize=False,
    )
    if not new_account or new_account.id is None:
        raise Exception("Account was created but could not be retrieved or has None id")
    account_id = new_account.id
    print(f"   ✅ Account ID: {account_id}")

    # Create reseller_role association
    print("\n7. Creating reseller_role association...")
    print("   ⚠️  This requires user approval in the rhizome server terminal")
    role_result = rhizome_client.execute_write_query(
        query_name="create_reseller_role",
        database_id="dev_meta",
        params={
            "reseller_id": clover_reseller_id,
            "account_id": account_id,
            "permissions_id": super_admin_role_id,
        },
        reason="Grant Super Administrator permissions to MFF test account for Clover reseller",
        entity_descriptions={
            f"reseller_id_{clover_reseller_id}": "Clover reseller (parent reseller for test accounts)",
            f"account_id_{account_id}": f"MFF test account ({email})",
            f"permissions_id_{super_admin_role_id}": "Super Administrator role (allows creating resellers)",
        },
    )

    if not role_result["executed"]:
        raise Exception(
            f"Reseller role creation failed: approved={role_result.get('approved')}, error={role_result.get('error')}"
        )

    print("   ✅ Reseller role created successfully")

    # Get reseller_role ID
    print("\n8. Retrieving reseller_role ID...")
    ResellerRole = meta_db.get_versioned(meta_db.ResellerRole)
    reseller_role = meta_db.select_first(
        select(ResellerRole)
        .where(ResellerRole.account_id == account_id)
        .where(ResellerRole.reseller_id == clover_reseller_id),
        sanitize=False,
    )
    if not reseller_role:
        raise Exception("Reseller role was created but could not be retrieved")
    reseller_role_id = reseller_role.id
    print(f"   ✅ Reseller role ID: {reseller_role_id}")

    # Update account's primary role
    print("\n9. Updating account's primary role...")
    print("   ⚠️  This requires user approval in the rhizome server terminal")
    primary_role_result = rhizome_client.execute_write_query(
        query_name="update_account_primary_role",
        database_id="dev_meta",
        params={
            "account_id": account_id,
            "primary_reseller_role_id": reseller_role_id,
        },
        reason="Set the MFF account's primary role to enable reseller management capabilities",
        entity_descriptions={
            f"account_id_{account_id}": f"MFF test account ({email})",
            f"role_id_{reseller_role_id}": (
                f"Super Administrator role for Clover reseller (reseller_id={clover_reseller_id})"
            ),
        },
    )

    if not primary_role_result["executed"]:
        raise Exception(
            f"Primary role update failed: approved={primary_role_result.get('approved')}, "
            f"error={primary_role_result.get('error')}"
        )

    print("   ✅ Primary role updated successfully")

    # Claim the account
    print("\n10. Claiming the account (setting password)...")
    try:
        _claim_account(account_uuid, claim_code, password)
        print("   ✅ Account claimed successfully")
    except httpx.HTTPStatusError as e:
        print(f"   ⚠️  Account claim failed: {e}")
        print(f"      Status: {e.response.status_code}")
        print(f"      Response: {e.response.text}")
        print("   ℹ️  You can claim the account manually later")

    # Save account info
    account_info = ResellerOwnerAccount(
        uuid=account_uuid,
        id=account_id,
        email=email,
        name="MFF User",
    )
    _save_account_info(account_uuid, account_id, email)

    print("\n✨ MFF Reseller Owner Account Setup Complete!")
    print(f"   UUID: {account_uuid}")
    print(f"   ID: {account_id}")
    print(f"   Email: {email}")
    print("   Has Super Administrator privileges for Clover reseller")

    return account_info


def create_reseller(
    environment: "Environment",
    name: str,
    owner_email: str,
    parent_reseller_id: str,
    merchant_plan_group_id: str,
    **kwargs: str | dict[str, str] | bool | None,
) -> dict[str, Any]:
    """
    Create a reseller in the meta.reseller table.

    This is a convenience wrapper around the environment's API for creating resellers.

    Args:
        environment: A trifolium environment (e.g., from trifolium.environments.dev.Environment)
        name: Reseller name
        owner_email: Email for the reseller owner account
        parent_reseller_id: ID of the parent reseller
        merchant_plan_group_id: ID of the merchant plan group
        **kwargs: Additional fields to pass to the API

    Returns:
        dict with created reseller data including UUID

    Raises:
        Exception: If reseller creation fails
    """
    # Cast kwargs to satisfy type checker - values conform to API requirements
    return environment.api.resellers.create_reseller(
        name=name,
        owner_email=owner_email,
        parent_reseller_id=parent_reseller_id,
        merchant_plan_group_id=merchant_plan_group_id,
        **kwargs,  # pyright: ignore[reportArgumentType]
    )


# Helper functions


def _get_credentials_from_1password(meta_db: DevMeta) -> tuple[str, str]:
    """Get username and password from 1Password."""
    from rhizome.environments.base import Environment

    username = asyncio.run(
        Environment.get_secret(
            meta_db.client.tools, "op://Shared/MFF-reseller-owner/username", SecretManager.ONEPASSWORD
        )
    )
    password = asyncio.run(
        Environment.get_secret(
            meta_db.client.tools, "op://Shared/MFF-reseller-owner/password", SecretManager.ONEPASSWORD
        )
    )
    return username, password


def _generate_claim_code(length: int = 32) -> str:
    """Generate a secure random claim code."""
    return secrets.token_urlsafe(length)


def _get_clover_reseller_id(meta_db: DevMeta) -> int:
    """Get the ID of the Clover reseller."""
    ResellerModel = meta_db.get_versioned(Reseller)
    clover_reseller = meta_db.select_first(
        select(ResellerModel).where(ResellerModel.name == "Clover"),
        sanitize=False,
    )
    if not clover_reseller or clover_reseller.id is None:
        raise Exception("Could not find 'Clover' reseller. This is required for creating the MFF User.")
    return clover_reseller.id


def _get_super_admin_role_id(meta_db: DevMeta, clover_reseller_id: int) -> int:
    """Get the ID of the Super Administrator role for the Clover reseller."""
    ResellerPermissions = meta_db.get_versioned(meta_db.ResellerPermissions)

    super_admin_role = meta_db.select_first(
        select(ResellerPermissions)
        .where(ResellerPermissions.reseller_id == clover_reseller_id)
        .where(ResellerPermissions.name == "Super Administrator"),
        sanitize=False,
    )

    if not super_admin_role or super_admin_role.id is None:
        raise Exception(
            f"Could not find 'Super Administrator' role for Clover reseller (id={clover_reseller_id}). "
            "This role is required for creating resellers."
        )
    return super_admin_role.id


def _claim_account(account_uuid: str, claim_code: str, password: str) -> dict[str, Any]:
    """Claim the account by setting its password."""
    domain = "dev1.dev.clover.com"
    url = f"https://{domain}/cos/v1/dashboard/claim_account"

    payload = {
        "email": "mff_user@example.com",
        "uuid": account_uuid,
        "name": "MFF User",
        "ignoreCompany": True,
        "password": password,
        "confirmPassword": password,
        "claimCode": claim_code,
        "pinLength": 4,
    }

    # This endpoint doesn't require authentication (uses claim code instead)
    response = httpx.post(url, json=payload)
    response.raise_for_status()
    return response.json()


def _save_account_info(account_uuid: str, account_id: int, email: str) -> None:
    """Save MFF User account info to state file for reuse."""
    from trifolium.config import Home

    home = Home()
    state_file = home.state / "mff_user.json"

    account_info = {
        "uuid": account_uuid,
        "id": account_id,
        "email": email,
        "name": "MFF User",
    }

    state_file.write_text(json.dumps(account_info, indent=2))
    print(f"\n💾 Saved account info to {state_file}")
