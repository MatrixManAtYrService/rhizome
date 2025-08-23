"""
Test local Kubernetes MySQL integration.

Verifies rhizome can connect to local Kind cluster MySQL and query expected data.
"""

from sqlmodel import Session, create_engine, select

import rhizome.environments.localtest.localk8s as localk8s
from rhizome.client import RhizomeClient
from rhizome.config import Home
from rhizome.models.bookkeeper.fee_summary import FeeSummary, sanitize
from tests.utils import get_open_port


def test_mysql_connection_and_sanitization(
    local_cluster: None, local_mysql: None, rhizome_server: tuple[int, Home]
) -> None:
    """Test MySQL connection, data query, and sanitization functionality."""
    # Unpack server info
    _server_port, home = rhizome_server

    # Create client instance and configure it with the test home
    client = RhizomeClient()
    client.home = home

    # Connect to MySQL via rhizome port forwarding
    mysql_port = get_open_port()
    print(f"Using MySQL port: {mysql_port}")
    handle = localk8s.get_handle(client=client, local_port=mysql_port, delay=1.5)
    engine = create_engine(handle.connection_string)

    with Session(engine) as session:
        # Query for expected test data
        statement = select(FeeSummary).where(FeeSummary.id == 74347)
        fee_summary = session.exec(statement).first()

        assert fee_summary is not None, "Test data with ID 74347 should exist"

        # Verify key fields match expected test data
        assert fee_summary.billing_entity_uuid == "JW8H2B9BT6B11R2HHXY3HYQCN6"
        assert fee_summary.fee_code == "MW63DAWPN6JGY.S"
        assert fee_summary.currency == "USD"
        assert float(fee_summary.total_fee_amount) == 9.99

        # Test sanitization - UUID fields should be hashed, other fields unchanged
        sanitized = sanitize(fee_summary)
        assert sanitized.billing_entity_uuid != fee_summary.billing_entity_uuid
        assert sanitized.uuid != fee_summary.uuid
        assert sanitized.fee_code == fee_summary.fee_code  # Non-UUID field unchanged
