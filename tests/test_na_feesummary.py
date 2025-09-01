"""
Test North America production fee summary data accessibility.

This module contains two tests for the same functionality:
1. Mocked test - uses mock tools to simulate CloudSQL proxy, 1Password, and database
2. Real test - connects to actual external infrastructure (requires --external-infra)

Both tests verify that fee summary record 74347 exists and sanitization works correctly.
"""

import asyncio
import datetime
import tempfile
from decimal import Decimal
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.config import Home
from rhizome.environments.na_prod.bookeeper import NorthAmericaBookkeeper
from rhizome.models.bookkeeper.fee_summary import FeeSummary
from rhizome.tools import CommandResult, KubectlTool, LogLine, LsofTool, OnePasswordTool, PortInfo, Tools


class MockKubectlTool(KubectlTool):
    """Mock kubectl tool that simulates CloudSQL proxy behavior."""

    async def exec_in_pod(self, context: str, namespace: str, deployment: str, command: list[str]) -> CommandResult:
        """Simulate starting CloudSQL connection script."""
        return CommandResult(returncode=0, stdout="Connection script started", stderr="")

    async def get_logs(self, context: str, namespace: str, deployment: str, since: str = "10s") -> list[LogLine]:
        """Return logs with CloudSQL proxy port information."""
        return [
            LogLine(
                content=(
                    "Starting proxy for connectionName "
                    "'clover-prod-databases:us-central1:billing-bookkeeper' on port '62956'"
                )
            ),
            LogLine(content="Ready for new connections"),
        ]

    async def port_forward(
        self, context: str, namespace: str, resource: str, local_port: int, remote_port: int
    ) -> asyncio.subprocess.Process:
        """Return a mock subprocess for port forwarding."""
        mock_process = AsyncMock()
        mock_process.pid = 12345
        mock_process.stdout = AsyncMock()
        mock_process.stderr = AsyncMock()
        mock_process.stdout.readline = AsyncMock(return_value=b"Forwarding from 127.0.0.1:31001 -> 62956\n")
        mock_process.stderr.readline = AsyncMock(return_value=b"")
        return mock_process

    async def cluster_info(self, context: str) -> CommandResult:
        """Mock cluster info."""
        return CommandResult(returncode=0, stdout="Cluster info", stderr="")

    async def get_pod_status(self, pod_name: str, context: str | None = None) -> CommandResult:
        """Mock pod status."""
        return CommandResult(returncode=0, stdout="Running", stderr="")


class MockOnePasswordTool(OnePasswordTool):
    """Mock 1Password tool that returns test credentials."""

    async def read_secret(self, reference: str) -> str:
        """Return mock password for production database."""
        return "test_production_password_123"


class MockLsofTool(LsofTool):
    """Mock lsof tool that reports ports as available."""

    async def check_port(self, port: int) -> list[PortInfo]:
        """Return empty list indicating port is available."""
        return []


def test_na_production_connection_and_sanitization_with_mocks(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test North America production flow using mocked tools (no external dependencies)."""

    # Create mocked tools
    mock_tools = Tools(kubectl=MockKubectlTool(), onepassword=MockOnePasswordTool(), lsof=MockLsofTool())

    # Mock SQLModel database session to return test data
    mock_session = MagicMock()
    test_fee_summary = FeeSummary(
        id=74347,
        uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_entity_uuid="MERCHANT_UUID_EXAMPLE_123456",
        billing_date=datetime.date(2025, 1, 15),
        fee_category="Processing",
        fee_code="MW63DAWPN6JGY.S",
        currency="USD",
        total_period_units=Decimal("1.0000"),
        abs_period_units=Decimal("1.0000"),
        total_basis_amount=Decimal("9.990"),
        abs_basis_amount=Decimal("9.990"),
        total_fee_amount=Decimal("9.990"),
        fee_rate_uuid="FEE_RATE_UUID_EXAMPLE_789",
        request_uuid="REQUEST_UUID_EXAMPLE_456",
        invoice_info_uuid=None,
        fee_code_ledger_account_uuid=None,
        credit_ledger_account_uuid=None,
        debit_ledger_account_uuid=None,
        exclude_from_invoice=0,
        created_timestamp=datetime.datetime(2025, 1, 15, 10, 30, 0),
        modified_timestamp=datetime.datetime(2025, 1, 15, 10, 30, 0),
    )

    mock_exec_result = MagicMock()
    mock_exec_result.first.return_value = test_fee_summary
    mock_session.exec.return_value = mock_exec_result

    # Patch SQLModel components to use mocks that return actual data
    if TYPE_CHECKING:
        pass

    def mock_session_context(engine: object) -> object:
        class MockSessionContext:
            def __enter__(self) -> object:
                return mock_session

            def __exit__(self, *args: object) -> None:
                pass

        return MockSessionContext()

    def mock_create_engine(cs: str) -> MagicMock:
        return MagicMock()

    monkeypatch.setattr("rhizome.client.create_engine", mock_create_engine)
    monkeypatch.setattr("rhizome.client.Session", mock_session_context)

    # Create client instance with mocked tools (no server needed)
    temp_home = Home(state=Path(tempfile.mkdtemp()))
    client = RhizomeClient(home=temp_home, tools=mock_tools)

    # Create North America production environment which handles CloudSQL port forwarding
    na_prod = NorthAmericaBookkeeper(client)

    # Execute query with automatic sanitization (same pattern as test_k8s_mysql.py)
    fee_summary = na_prod.select_first(select(FeeSummary).where(FeeSummary.id == 74347))

    assert fee_summary is not None, "Test data with ID 74347 should exist"

    # Since the result is sanitized, UUID fields should be hashed
    assert fee_summary.billing_entity_uuid.startswith("Hash"), "billing_entity_uuid should be sanitized"
    assert fee_summary.uuid.startswith("Hash"), "uuid should be sanitized"
    assert fee_summary.fee_code == "MW63DAWPN6JGY.S"  # Non-UUID field unchanged
    assert fee_summary.currency == "USD"
    assert float(fee_summary.total_fee_amount) == 9.99


@pytest.mark.external_infra
def test_na_production_connection_and_sanitization_real() -> None:
    """Test North America production CloudSQL connection with real external infrastructure.
    
    This test performs the complete production workflow without mocks:
    1. Connects to real CloudSQL via kubectl port-forwarding
    2. Retrieves actual credentials from 1Password
    3. Queries real production database for fee summary record 74347
    4. Verifies data sanitization works correctly
    
    Prerequisites:
    - VPN connection to production network
    - kubectl configured with production context
    - 1Password CLI authenticated
    - Production database read access
    """
    import tempfile
    from pathlib import Path
    from rhizome.config import Home
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create client with real tools (no mocks)
        home = Home.sandbox(Path(temp_dir))
        client = RhizomeClient(home=home)
        
        # Create North America production environment which handles real CloudSQL port forwarding
        na_prod = NorthAmericaBookkeeper(client)
        
        # Execute query with automatic sanitization
        # This will use real kubectl, 1Password, and database connections
        fee_summary = na_prod.select_first(select(FeeSummary).where(FeeSummary.id == 74347))
        
        assert fee_summary is not None, "Test data with ID 74347 should exist in production database"
        
        # Since the result is sanitized, UUID fields should be hashed
        assert fee_summary.billing_entity_uuid.startswith("Hash"), "billing_entity_uuid should be sanitized"
        assert fee_summary.uuid.startswith("Hash"), "uuid should be sanitized"
        assert fee_summary.fee_code == "MW63DAWPN6JGY.S"  # Non-UUID field unchanged
        assert fee_summary.currency == "USD"
        assert float(fee_summary.total_fee_amount) == 9.99
