"""
Test all environment and database combinations using mocked infrastructure.

This module contains parameterized tests that verify mocked data access across
all supported environment/database combinations:
- Environments: na, dev, demo  
- Databases: billing-bookkeeper, billing-event

Tests use mocked tools to simulate CloudSQL proxy, 1Password, and database
connections without requiring external infrastructure.
"""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.config import Home
from rhizome.environments.demo.billing_event import DemoBillingEvent
from rhizome.environments.demo.bookeeper import DemoBookkeeper
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.environments.dev.bookeeper import DevBookkeeper
from rhizome.environments.na_prod.billing_event import NorthAmericaBillingEvent
from rhizome.environments.na_prod.bookeeper import NorthAmericaBookkeeper
from rhizome.models.billing_event.app_metered_event import AppMeteredEvent
from rhizome.models.bookkeeper.fee_summary import FeeSummary
from rhizome.tools import Tools
from tests.mocked_subprocesses import MockKubectlTool, MockLsofTool, MockOnePasswordTool
from tests.mocked_table_data import TEST_DATA_SPECS

ENVIRONMENT_DATABASE_COMBINATIONS = [
    (NorthAmericaBookkeeper, FeeSummary),      
    (DevBookkeeper, FeeSummary),               
    (DemoBookkeeper, FeeSummary),              
    (NorthAmericaBillingEvent, AppMeteredEvent), 
    (DevBillingEvent, AppMeteredEvent),        
    (DemoBillingEvent, AppMeteredEvent),       
]


@pytest.mark.parametrize("environment_class,model_class", ENVIRONMENT_DATABASE_COMBINATIONS)
def test_mocked_environment_database_access(
    monkeypatch: pytest.MonkeyPatch, 
    environment_class: type, 
    model_class: type
) -> None:
    """Test database access across all environment/database combinations using mocks (no external dependencies)."""
    
    # Get test specification for this model class and environment
    test_spec = TEST_DATA_SPECS[model_class][environment_class]
    
    # Create mocked tools
    mock_tools = Tools(
        kubectl=MockKubectlTool(), 
        onepassword=MockOnePasswordTool(), 
        lsof=MockLsofTool()
    )

    # Mock SQLModel database session to return appropriate test data
    mock_session = MagicMock()
    test_data = test_spec.get_mock_data()
    mock_exec_result = MagicMock()
    mock_exec_result.first.return_value = test_data
    mock_session.exec.return_value = mock_exec_result

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

    # Create client instance with mocked tools
    temp_home = Home(state=Path(tempfile.mkdtemp()))
    client = RhizomeClient(home=temp_home, tools=mock_tools, data_in_logs=False)
    
    # Query the table using the model class and test specification
    env_instance = environment_class(client)
    result = env_instance.select_first(select(model_class).where(model_class.id == test_spec.use_id))
    
    # Is the mocked data present? For mocked tests, we compare against the same mock data
    expected = test_spec.get_mock_data()
    test_spec.check_assertions(result, expected)


@pytest.mark.external_infra
@pytest.mark.parametrize("environment_class,model_class", ENVIRONMENT_DATABASE_COMBINATIONS)
def test_real_environment_database_access(
    environment_class: type, 
    model_class: type
) -> None:
    """Test database access across all environment/database combinations using real external infrastructure."""
    
    test_spec = TEST_DATA_SPECS[model_class][environment_class]
    with tempfile.TemporaryDirectory() as temp_dir:

        # Create client instance with real tools (using default RhizomeClient "tools" kwarg)
        home = Home.sandbox(Path(temp_dir))
        client = RhizomeClient(home=home, data_in_logs=True)

        # Query the table using the model class and test specification
        env_instance = environment_class(client)
        result = env_instance.select_first(select(model_class).where(model_class.id == test_spec.use_id))

        # Is the expected data present? For real tests, we compare against environment-specific expected data
        expected = test_spec.get_expected_data()
        test_spec.check_assertions(result, expected)
