"""
Test North America production fee summary data accessibility.

This module contains two tests for the same functionality:
1. Mocked test - uses mock tools to simulate CloudSQL proxy, 1Password, and database
2. Real test - connects to actual external infrastructure (requires --external-infra)

Both tests verify that fee summary record 74347 exists and sanitization works correctly.
"""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.config import Home
from rhizome.environments.na_prod.bookeeper import NorthAmericaBookkeeper
from rhizome.models.bookkeeper.fee_summary import FeeSummary
from rhizome.tools import Tools
from tests.mocked_subprocesses import MockLsofTool, MockNAProductionKubectlTool, MockOnePasswordTool
from tests.mocked_table_data import TEST_DATA_SPECS


def test_na_production_connection_and_sanitization_with_mocks(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test North America production flow using mocked tools (no external dependencies)."""

    # Create mocked tools
    mock_tools = Tools(kubectl=MockNAProductionKubectlTool(), onepassword=MockOnePasswordTool(), lsof=MockLsofTool())

    # Get test specification for FeeSummary in North America environment
    test_spec = TEST_DATA_SPECS[FeeSummary][NorthAmericaBookkeeper]
    
    # Mock SQLModel database session to return test data
    mock_session = MagicMock()
    test_fee_summary = test_spec.get_mock_data()

    mock_exec_result = MagicMock()
    mock_exec_result.first.return_value = test_fee_summary
    mock_session.exec.return_value = mock_exec_result

    # Patch SQLModel components to use mocks that return actual data
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
    client = RhizomeClient(home=temp_home, tools=mock_tools, data_in_logs=False)

    # Create North America production environment which handles CloudSQL port forwarding
    na_prod = NorthAmericaBookkeeper(client)

    # Execute query with automatic sanitization (same pattern as test_k8s_mysql.py)
    fee_summary = na_prod.select_first(select(FeeSummary).where(FeeSummary.id == test_spec.use_id))

    # Use centralized assertion function
    expected = test_spec.get_mock_data()
    test_spec.check_assertions(fee_summary, expected)


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
        client = RhizomeClient(home=home, data_in_logs=True)
        
        # Create North America production environment which handles real CloudSQL port forwarding
        na_prod = NorthAmericaBookkeeper(client)
        
        # Get test specification for FeeSummary in North America environment
        test_spec = TEST_DATA_SPECS[FeeSummary][NorthAmericaBookkeeper]
        
        # Execute query with automatic sanitization
        # This will use real kubectl, 1Password, and database connections
        fee_summary = na_prod.select_first(select(FeeSummary).where(FeeSummary.id == test_spec.use_id))
        
        # Use centralized assertion function  
        expected = test_spec.get_expected_data()
        test_spec.check_assertions(fee_summary, expected)
