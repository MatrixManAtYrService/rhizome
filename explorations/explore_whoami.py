#!/usr/bin/env python3
"""
Explore Clover API endpoints to discover 'whoami' functionality.

Try various endpoints to figure out which account is associated with
the current session token.
"""

import json
from typing import Any

import httpx

from stolon.client import StolonClient


def pretty_print_response(endpoint: str, response: httpx.Response) -> None:
    """Pretty print an API response."""
    print(f"\n{'=' * 80}")
    print(f"Endpoint: {endpoint}")
    print(f"Status: {response.status_code}")
    print(f"{'=' * 80}")

    if response.status_code == 200:
        try:
            data = response.json()
            print(json.dumps(data, indent=2))
        except Exception:
            print(response.text[:500])
    else:
        print(f"Error: {response.text[:500]}")


def try_endpoint(client: httpx.Client, endpoint: str, method: str = "GET") -> httpx.Response:
    """Try an API endpoint and return the response."""
    print(f"\n🔍 Trying {method} {endpoint}...")

    try:
        if method == "GET":
            response = client.get(endpoint, timeout=10.0)
        elif method == "POST":
            response = client.post(endpoint, timeout=10.0)
        else:
            raise ValueError(f"Unsupported method: {method}")

        print(f"   Status: {response.status_code}")
        return response
    except Exception as e:
        print(f"   Error: {e}")
        raise


def main():
    print("=" * 80)
    print("EXPLORING CLOVER API FOR 'WHOAMI' FUNCTIONALITY")
    print("=" * 80)

    # Initialize Stolon client
    stolon_client = StolonClient(data_in_logs=False)
    domain = "dev1.dev.clover.com"

    # Get authenticated session
    print("\n🔐 Getting authentication token...")
    handle = stolon_client.request_internal_token(domain)
    print(f"✓ Got token: {handle.token[:20]}...")

    # Create httpx client with authentication
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Clover-Appenv": "dev:dev1",
    }
    cookies = {"internalSession": handle.token}

    client = httpx.Client(
        base_url=f"https://{domain}",
        headers=headers,
        cookies=cookies,
        timeout=10.0,
    )

    # List of endpoints to try
    endpoints_to_try = [
        # Common "me" / "current user" patterns
        ("GET", "/v3/me"),
        ("GET", "/v3/current"),
        ("GET", "/v3/account"),
        ("GET", "/v3/accounts/current"),
        ("GET", "/v3/user"),
        ("GET", "/v3/users/current"),
        ("GET", "/v3/whoami"),
        # Employee-related (might show current user)
        ("GET", "/v3/employees/current"),
        ("GET", "/v3/employees"),
        # Merchant-related (might show accessible merchants)
        ("GET", "/v3/merchants"),
        # Reseller-related (might show accessible resellers)
        ("GET", "/v3/resellers"),
        # OAuth/auth endpoints
        ("GET", "/oauth/me"),
        ("GET", "/oauth/userinfo"),
        ("GET", "/v3/oauth/me"),
    ]

    successful_endpoints: list[tuple[str, str, httpx.Response]] = []

    print("\n" + "=" * 80)
    print("TRYING ENDPOINTS")
    print("=" * 80)

    for method, endpoint in endpoints_to_try:
        try:
            response = try_endpoint(client, endpoint, method)

            if response.status_code == 200:
                print(f"   ✅ SUCCESS!")
                successful_endpoints.append((method, endpoint, response))
            elif response.status_code == 401:
                print(f"   🔒 Unauthorized (token might not have access)")
            elif response.status_code == 404:
                print(f"   ❌ Not Found")
            elif response.status_code == 403:
                print(f"   🚫 Forbidden")
            else:
                print(f"   ⚠️  Unexpected status: {response.status_code}")

        except Exception as e:
            print(f"   💥 Exception: {e}")

    # Show successful responses in detail
    print("\n" + "=" * 80)
    print("SUCCESSFUL RESPONSES (Status 200)")
    print("=" * 80)

    if not successful_endpoints:
        print("\n❌ No endpoints returned 200 OK")
        print("\nLet's check response headers from a typical endpoint for clues...")

        # Try a simple endpoint and inspect headers
        try:
            response = client.get("/v3/merchants")
            print(f"\nHeaders from /v3/merchants (status {response.status_code}):")
            for key, value in response.headers.items():
                if any(
                    x in key.lower()
                    for x in ["user", "account", "auth", "session", "clover", "x-"]
                ):
                    print(f"  {key}: {value}")
        except Exception as e:
            print(f"Error getting headers: {e}")

    else:
        for method, endpoint, response in successful_endpoints:
            pretty_print_response(f"{method} {endpoint}", response)

            # Check headers for account info
            print("\n📋 Interesting headers:")
            for key, value in response.headers.items():
                if any(
                    x in key.lower()
                    for x in ["user", "account", "auth", "session", "clover", "x-"]
                ):
                    print(f"  {key}: {value}")

    # Try to extract account info from any successful responses
    print("\n" + "=" * 80)
    print("ACCOUNT INFORMATION EXTRACTION")
    print("=" * 80)

    for method, endpoint, response in successful_endpoints:
        try:
            data = response.json()

            # Look for account-related fields
            account_fields = [
                "account",
                "accountId",
                "account_id",
                "email",
                "userId",
                "user_id",
                "ownerId",
                "owner_id",
                "id",
                "uuid",
            ]

            print(f"\n{method} {endpoint}:")
            for field in account_fields:
                if field in data:
                    print(f"  {field}: {data[field]}")

            # If it's a list, show first item
            if isinstance(data, dict) and "elements" in data:
                elements = data["elements"]
                if elements and len(elements) > 0:
                    print(f"  First element: {json.dumps(elements[0], indent=4)}")

        except Exception as e:
            print(f"  Error parsing response: {e}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    if successful_endpoints:
        print(f"\n✅ Found {len(successful_endpoints)} working endpoint(s):")
        for method, endpoint, _ in successful_endpoints:
            print(f"  • {method} {endpoint}")

        print("\n💡 Recommendation:")
        print("   Review the responses above to find account/user information.")
        print("   This will help us implement a 'whoami' function for the test.")
    else:
        print("\n❌ No direct 'whoami' endpoint found.")
        print("\n💡 Alternative approaches:")
        print("   1. Parse account info from session token (if it's a JWT)")
        print("   2. Check if merchants list includes owner account info")
        print("   3. Use a known test account email from dev1")

    client.close()


if __name__ == "__main__":
    main()
