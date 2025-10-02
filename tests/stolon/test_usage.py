"""
Test the user-facing API for stolon environments.

This module tests the API patterns that allow users to make authenticated
HTTP requests to Clover APIs without needing to manage tokens directly.
"""

import pytest

from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp


@pytest.mark.external_infra
def test_get_merchant_name_from_dev1() -> None:
    """Test retrieving merchant name from dev environment."""
    dev = DevHttp(StolonClient(data_in_logs=False))
    name = dev.get_merchant_name("MSR15REPHS0N5")

    # Verify we got a name back
    assert name
    assert isinstance(name, str)


"""
This call works:

http get --headers {
  X-Clover-Appenv: "dev:dev1"
  Cookie: "internalSession=3cab0ab0-746a-43ad-8f24-0a762e1d72fa"
  Content-Type: "application/json"
} https://dev1.dev.clover.com/v3/merchants/MSR15REPHS0N5 | to json
{
  "href": "https://dev1.dev.clover.com/v3/merchants/MSR15REPHS0N5",
  "id": "MSR15REPHS0N5",
  "name": "jayesh.hinge+EBB_dev1_48",
}
"""

