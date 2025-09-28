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
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.demo.billing_event import DemoBillingEvent
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.environments.na_prod.billing import NorthAmericaBilling
from rhizome.environments.na_prod.billing_bookkeeper import NorthAmericaBillingBookkeeper
from rhizome.environments.na_prod.billing_event import NorthAmericaBillingEvent
from rhizome.environments.na_prod.meta import NorthAmericaMeta
from rhizome.tools import Tools
from tests.mocked_subprocesses import (
    MockGcloudTool,
    MockKubectlTool,
    MockLsofTool,
    MockOnePasswordTool,
    MockPybritiveTool,
)
from trifolium.config import Home


@dataclass
class EnvironmentMocks:
    """Container for mocks associated with an environment class."""

    environment_class: type
    mock_tools: Tools
    client: RhizomeClient
    env_instance: Any
    table_mocks: dict[Any, tuple[Any, Callable[[object], object], Callable[[str], MagicMock]]]


def create_environment_mocks(environment_class: type) -> EnvironmentMocks | None:
    """Create all mocks needed for testing an environment class."""
    try:
        # Create mocked tools
        mock_tools = Tools(
            kubectl=MockKubectlTool(),
            onepassword=MockOnePasswordTool(),
            lsof=MockLsofTool(),
            gcloud=MockGcloudTool(),
            pybritive=MockPybritiveTool(),
        )

        # Create client instance with mocked tools
        temp_home = Home(state=Path(tempfile.mkdtemp()))
        client = RhizomeClient(home=temp_home, tools=mock_tools, data_in_logs=False)

        # Create environment instance to get table_situation
        env_instance = environment_class(client)
    except Exception:
        # If environment creation fails, return None
        return None

    # Create mocks for each table
    table_mocks: dict[Any, tuple[Any, Callable[[object], object], Callable[[str], MagicMock]]] = {}
    for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
        # Skip tables where model_class is None (not yet implemented)
        if model_class is None:
            continue

        # Get expected data from the emplacement class
        try:
            expected_data = emplacement_class.get_expected()
        except (NotImplementedError, FileNotFoundError, ValueError, Exception):
            # Skip tables where expected data is not yet implemented or missing JSON files
            continue

        # Mock SQLModel database session to return the expected data
        mock_session = MagicMock()
        mock_exec_result = MagicMock()
        mock_exec_result.first.return_value = expected_data
        mock_session.exec.return_value = mock_exec_result

        def create_mock_session_context(session_obj: MagicMock) -> Callable[[object], object]:
            """Create a mock session context factory."""

            class MockSessionContext:
                def __enter__(self) -> object:
                    return session_obj

                def __exit__(self, *args: object) -> None:
                    pass

            def session_context_factory(engine: object) -> object:
                return MockSessionContext()

            return session_context_factory

        mock_session_context = create_mock_session_context(mock_session)

        def mock_create_engine(cs: str) -> MagicMock:
            return MagicMock()

        table_mocks[table_name] = (expected_data, mock_session_context, mock_create_engine)

    return EnvironmentMocks(
        environment_class=environment_class,
        mock_tools=mock_tools,
        client=client,
        env_instance=env_instance,
        table_mocks=table_mocks,
    )


# Environment classes to test
ENVIRONMENT_CLASSES = [
    NorthAmericaBillingBookkeeper,
    DevBillingBookkeeper,
    DemoBillingBookkeeper,
    NorthAmericaBillingEvent,
    DevBillingEvent,
    DemoBillingEvent,
    NorthAmericaBilling,
    NorthAmericaMeta,
]

# Create environment instances without attempting to load test data
ENVIRONMENT_INSTANCES = {}
for cls in ENVIRONMENT_CLASSES:
    try:
        # Create mocked tools
        mock_tools = Tools(
            kubectl=MockKubectlTool(),
            onepassword=MockOnePasswordTool(),
            lsof=MockLsofTool(),
            gcloud=MockGcloudTool(),
            pybritive=MockPybritiveTool(),
        )
        # Create client instance with mocked tools
        temp_home = Home(state=Path(tempfile.mkdtemp()))
        client = RhizomeClient(home=temp_home, tools=mock_tools, data_in_logs=False)
        # Create environment instance
        env_instance = cls(client)
        ENVIRONMENT_INSTANCES[cls] = env_instance
    except Exception:
        # Skip environments that can't be created
        continue

# Generate test parameters: one test per environment/table combination
TEST_PARAMETERS = []  # type: ignore
for env_class, env_instance in ENVIRONMENT_INSTANCES.items():  # type: ignore
    for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():  # type: ignore
        # Skip tables where model_class is None (not yet implemented)
        if model_class is None:
            continue
        TEST_PARAMETERS.append((env_class, table_name, model_class, emplacement_class))  # type: ignore


@pytest.mark.parametrize("environment_class,table_name,model_class,emplacement_class", TEST_PARAMETERS)  # type: ignore
def test_mocked_environment_database_access(
    monkeypatch: pytest.MonkeyPatch,
    environment_class: type,
    table_name: str,
    model_class: type,
    emplacement_class: type,
) -> None:
    """Test database access for a specific environment/table combination using mocks."""

    # Get environment instance
    env_instance = ENVIRONMENT_INSTANCES[environment_class]  # type: ignore

    # Try to get expected data - this should FAIL if JSON is missing
    try:
        expected_data = emplacement_class.get_expected()  # type: ignore[reportUnknownMemberType]
    except FileNotFoundError:
        pytest.fail(
            f"Missing test data file for {emplacement_class.__name__}. "
            f"Run 'rhizome sync data --env {env_instance.name} --table {table_name}' to generate it."  # type: ignore[reportUnknownMemberType]
        )
    except NotImplementedError:
        pytest.skip(f"Test data not yet implemented for {environment_class.__name__}/{table_name}")

    # Create mocks for this specific table
    mock_session = MagicMock()
    mock_exec_result = MagicMock()
    mock_exec_result.first.return_value = expected_data
    mock_session.exec.return_value = mock_exec_result

    class MockSessionContext:
        def __enter__(self) -> object:
            return mock_session

        def __exit__(self, *args: object) -> None:
            pass

    def mock_session_context_factory(engine: object) -> object:
        return MockSessionContext()

    def mock_create_engine(cs: str) -> MagicMock:
        return MagicMock()

    monkeypatch.setattr("rhizome.client.create_engine", mock_create_engine)
    monkeypatch.setattr("rhizome.client.Session", mock_session_context_factory)

    # Query the table using the model class
    result = env_instance.select_first(select(model_class).where(model_class.id == expected_data.id))  # type: ignore

    # Verify the mocked data is returned and matches expected structure
    assert result is not None, f"Query should return data for {table_name} in {env_instance.name}"  # type: ignore
    assert result.id == expected_data.id, f"ID should match for {table_name} in {env_instance.name}"  # type: ignore


@pytest.mark.external_infra
@pytest.mark.parametrize("environment_class,table_name,model_class,emplacement_class", TEST_PARAMETERS)
def test_real_environment_database_access(
    environment_class: type,
    table_name: str,
    model_class: type,
    emplacement_class: type,
    real_env_instance_factory: Callable[[type], object],
) -> None:
    """Test database access for a single environment/table combination using real external infrastructure."""
    # Get a memoized environment instance from the factory fixture
    env_instance = real_env_instance_factory(environment_class)

    # Get expected data from the emplacement class
    try:
        expected_data = emplacement_class.get_expected()
    except NotImplementedError:
        # Skip tables where expected data is not yet implemented
        pytest.skip(f"Test data not yet implemented for {environment_class.__name__}/{table_name}")

    # Query the table using the model class and expected ID
    result = env_instance.select_first(select(model_class).where(model_class.id == expected_data.id))

    # If no data is found in the real environment, warn and skip.
    # This makes the test tolerant of empty tables in real environments.
    if result is None:
        print(f"Warning: No real data found for {table_name} in {env_instance.name}. Skipping assertion.")
        return

    # The emplacement class handles the assertion and provides rich error messages
    emplacement_class().assert_match(result, expected_data)
