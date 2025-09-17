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
from rhizome.config import Home
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.demo.billing_event import DemoBillingEvent
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.environments.na_prod.billing import NorthAmericaBilling
from rhizome.environments.na_prod.billing_bookkeeper import NorthAmericaBillingBookkeeper
from rhizome.environments.na_prod.billing_event import NorthAmericaBillingEvent
from rhizome.tools import Tools
from tests.mocked_subprocesses import (
    MockGcloudTool,
    MockKubectlTool,
    MockLsofTool,
    MockOnePasswordTool,
    MockPybritiveTool,
)


@dataclass
class EnvironmentMocks:
    """Container for mocks associated with an environment class."""

    environment_class: type
    mock_tools: Tools
    client: RhizomeClient
    env_instance: Any
    table_mocks: dict[Any, tuple[Any, Callable[[object], object], Callable[[str], MagicMock]]]


def create_environment_mocks(environment_class: type) -> EnvironmentMocks:
    """Create all mocks needed for testing an environment class."""
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

    # Create mocks for each table
    table_mocks: dict[Any, tuple[Any, Callable[[object], object], Callable[[str], MagicMock]]] = {}
    for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
        # Skip tables where model_class is None (not yet implemented)
        if model_class is None:
            continue

        # Get expected data from the emplacement class
        try:
            expected_data = emplacement_class.get_expected()
        except NotImplementedError:
            # Skip tables where expected data is not yet implemented
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
]

# Pre-create all mocks for each environment class
ENVIRONMENT_MOCKS = {cls: create_environment_mocks(cls) for cls in ENVIRONMENT_CLASSES}


@pytest.mark.parametrize("environment_class,mocks", ENVIRONMENT_MOCKS.items())
def test_mocked_environment_database_access(
    monkeypatch: pytest.MonkeyPatch,
    environment_class: type,
    mocks: EnvironmentMocks,
) -> None:
    """Test database access across all environment/database combinations using mocks (no external dependencies)."""

    # Test each table with pre-created mocks
    for table_name, (model_class, _) in mocks.env_instance.table_situation.items():
        # Skip tables where model_class is None (not yet implemented)
        if model_class is None:
            continue

        # Skip if no mocks were created for this table
        if table_name not in mocks.table_mocks:
            continue

        expected_data, mock_session_context, mock_create_engine = mocks.table_mocks[table_name]

        monkeypatch.setattr("rhizome.client.create_engine", mock_create_engine)
        monkeypatch.setattr("rhizome.client.Session", mock_session_context)

        # Query the table using the model class
        result = mocks.env_instance.select_first(select(model_class).where(model_class.id == expected_data.id))

        # Verify the mocked data is returned and matches expected structure
        assert result is not None, f"Query should return data for {table_name} in {mocks.env_instance.name}"
        assert result.id == expected_data.id, f"ID should match for {table_name} in {mocks.env_instance.name}"


@pytest.mark.external_infra
@pytest.mark.parametrize("environment_class", ENVIRONMENT_CLASSES)
def test_real_environment_database_access(
    environment_class: type,
) -> None:
    """Test database access across all environment/database combinations using real external infrastructure."""

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create client instance with real tools (using default RhizomeClient "tools" kwarg)
        home = Home.sandbox(Path(temp_dir))
        client = RhizomeClient(home=home, data_in_logs=True)

        # Create environment instance to get table_situation
        env_instance = environment_class(client)

        # Test each table in the environment's table_situation
        for table_name, (model_class, emplacement_class) in env_instance.table_situation.items():
            # Skip tables where model_class is None (not yet implemented)
            if model_class is None:
                continue

            # Get expected data from the emplacement class
            try:
                expected_data = emplacement_class.get_expected()
            except NotImplementedError:
                # Skip tables where expected data is not yet implemented
                continue

            # Query the table using the model class and expected ID
            result = env_instance.select_first(select(model_class).where(model_class.id == expected_data.id))

            # Verify the real data matches the expected structure
            assert result is not None, f"Real data should exist for {table_name} in {env_instance.name}"

            # Use the emplacement class's assert_match method if available, otherwise basic assertions
            if hasattr(emplacement_class, "assert_match"):
                emplacement_class().assert_match(result, expected_data)
            else:
                assert result.id == expected_data.id, f"ID should match for {table_name} in {env_instance.name}"
