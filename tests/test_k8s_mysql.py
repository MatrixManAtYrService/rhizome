"""
Test local Kubernetes MySQL integration.

Verifies rhizome can connect to local Kind cluster MySQL and query expected data.
"""

from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments import LocalTest
from rhizome.models.bookkeeper.fee_summary import FeeSummary
from tests.conftest import RunningServer


def test_mysql_connection_and_sanitization(rhizome_server: RunningServer) -> None:
    """Test MySQL connection, data query, and sanitization functionality."""
    # Create client instance with the test home
    client = RhizomeClient(home=rhizome_server.home)

    # Create LocalTest environment which handles port forwarding and connection
    local_test = LocalTest(client)

    # Execute query with automatic sanitization
    fee_summary = local_test.select_first(
        select(FeeSummary).where(FeeSummary.id == 74347)
    )

    assert fee_summary is not None, "Test data with ID 74347 should exist"

    # Since the result is already sanitized, UUID fields should be hashed
    # We need to test against the hashed versions, not the original values
    assert fee_summary.billing_entity_uuid.startswith("Hash"), "billing_entity_uuid should be sanitized"
    assert fee_summary.uuid.startswith("Hash"), "uuid should be sanitized"
    assert fee_summary.fee_code == "MW63DAWPN6JGY.S"  # Non-UUID field unchanged
    assert fee_summary.currency == "USD"
    assert float(fee_summary.total_fee_amount) == 9.99
