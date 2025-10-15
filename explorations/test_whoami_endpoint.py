#!/usr/bin/env python3
"""
Test the /v3/internal/internal_accounts/current endpoint to get current user info.
"""

import json

import httpx

from stolon.client import StolonClient


def main():
    print("=" * 80)
    print("TESTING /v3/internal/internal_accounts/current ENDPOINT")
    print("=" * 80)

    # Initialize Stolon client
    stolon_client = StolonClient(data_in_logs=False)
    domain = "dev1.dev.clover.com"

    # Get authenticated session
    print("\n🔐 Getting authentication token...")
    handle = stolon_client.request_internal_token(domain)
    print(f"✓ Got token: {handle.token[:20]}...")

    # Make the request
    url = f"https://{domain}/v3/internal/internal_accounts/current"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Clover-Appenv": "dev:dev1",
    }
    cookies = {"internalSession": handle.token}

    print(f"\n🔍 Testing: GET {url}")

    try:
        response = httpx.get(url, headers=headers, cookies=cookies, timeout=10.0)

        print(f"Status: {response.status_code}")

        if response.status_code == 200:
            print("\n✅ SUCCESS! Response:")
            print("=" * 80)

            data = response.json()
            print(json.dumps(data, indent=2))

            print("\n" + "=" * 80)
            print("EXTRACTED ACCOUNT INFORMATION")
            print("=" * 80)

            # Extract key fields
            fields_to_show = ["id", "uuid", "email", "name", "role"]

            for field in fields_to_show:
                if field in data:
                    print(f"  {field}: {data[field]}")

            # Check for nested fields
            if "account" in data:
                print("\n  Nested 'account' field:")
                for key, value in data["account"].items():
                    print(f"    {key}: {value}")

            print("\n💡 This endpoint can be used as 'whoami' for the test!")
            print(f"   Owner email: {data.get('email', 'NOT FOUND')}")

        elif response.status_code == 401:
            print("\n🔒 Unauthorized - token might be invalid")
            print(response.text)

        elif response.status_code == 404:
            print("\n❌ Not Found - endpoint doesn't exist")
            print(response.text)

        elif response.status_code == 403:
            print("\n🚫 Forbidden - token doesn't have access to this endpoint")
            print(response.text)

        else:
            print(f"\n⚠️  Unexpected status: {response.status_code}")
            print(response.text[:500])

        # Show interesting headers
        print("\n" + "=" * 80)
        print("RESPONSE HEADERS")
        print("=" * 80)
        for key, value in response.headers.items():
            if any(
                x in key.lower() for x in ["user", "account", "auth", "session", "clover", "x-"]
            ):
                print(f"  {key}: {value}")

    except Exception as e:
        print(f"\n💥 Exception: {e}")
        raise


if __name__ == "__main__":
    main()
