"""Utilities for working with user accounts and permissions."""

from stolon.client import StolonClient
from stolon.retry_401 import make_authenticated_get
from trifolium.util.models import CurrentUser


def get_current_user(stolon_client: StolonClient, domain: str = "dev1.dev.clover.com") -> CurrentUser:
    """
    Get the currently authenticated user's information and permissions.

    This function queries the internal accounts API to get details about the
    user authenticated via the stolon internal token.

    Args:
        stolon_client: StolonClient configured with authentication
        domain: The Clover domain to query (default: dev1.dev.clover.com)

    Returns:
        CurrentUser model with:
            - ldap_name: The user's LDAP username
            - account_uuid: The user's account UUID
            - email: The user's email address (ldapName@clover.com)
            - permissions: List of permission objects

    Raises:
        Exception: If the whoami endpoint doesn't return ldapName
        httpx.HTTPStatusError: If API requests fail
    """
    headers = {"X-Clover-Appenv": "dev:dev1"}

    # Get the authenticated user's info
    whoami_url = f"https://{domain}/v3/internal/internal_accounts/current"
    whoami_response = make_authenticated_get(stolon_client, domain, whoami_url, headers=headers, timeout=10.0)

    whoami_data = whoami_response.json()
    ldap_name = whoami_data.get("ldapName")
    account_uuid = whoami_data.get("id")

    if not ldap_name:
        raise Exception(f"No ldapName in whoami response: {whoami_data}")

    # Construct email from ldapName
    email = f"{ldap_name}@clover.com"

    # Query the user's permissions
    permissions_url = f"https://{domain}/v3/internal/internal_accounts/{account_uuid}/internal_account_permissions"
    permissions_response = make_authenticated_get(stolon_client, domain, permissions_url, headers=headers, timeout=10.0)

    permissions = permissions_response.json()

    return CurrentUser(
        ldap_name=ldap_name,
        account_uuid=account_uuid,
        email=email,
        permissions=permissions,
    )
