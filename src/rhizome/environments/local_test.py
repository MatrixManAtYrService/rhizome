"""Local test environment for rhizome."""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, Any, TypeVar

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig
from rhizome.models.base import Emplacement
from rhizome.utils import get_open_port

if TYPE_CHECKING:
    from sqlmodel.sql._expression_select_cls import SelectOfScalar

    from rhizome.client import RhizomeClient
    from rhizome.models.base import RhizomeModel

TFirst = TypeVar("TFirst", bound="RhizomeModel")
TAll = TypeVar("TAll", bound="RhizomeModel")
TOne = TypeVar("TOne", bound="RhizomeModel")


class LocalTest(Environment):
    """Local test environment using Kind cluster with MySQL."""

    def __init__(self, client: RhizomeClient) -> None:
        """Initialize LocalTest environment, setting up port forwarding."""
        self.client = client

        # Get an available port and request port forward
        available_port = get_open_port()
        handle = client.request_localk8s(
            kube_context="kind-rhizome-test",
            kube_namespace="default",
            kube_deployment="mysql",
            local_port=available_port,
        )
        self.local_port = handle.local_port

    def get_database_config(self) -> DatabaseConfig:
        """Get database config for local test MySQL."""
        return DatabaseConfig(
            host="127.0.0.1",
            port=self.local_port,  # Use the actual forwarded port
            database="test",
            username="user",
            password="pass",
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """LocalTest handles port forwarding in __init__, so return None here."""
        return None

    @property
    def name(self) -> str:
        """Environment name."""
        return "LocalTest"

    def tables(self) -> list[StrEnum]:
        """Return empty list for local test environment."""
        return []

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        """Not implemented for local test environment."""
        raise NotImplementedError("LocalTest environment does not support table situation mapping")

    def get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        db_config = self.get_database_config()
        return f"mysql+pymysql://{db_config.username}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}"

    def select_first(self, query: SelectOfScalar[TFirst], sanitize: bool = True) -> TFirst | None:
        """Execute a query and return the first result or None.

        Args:
            query: SQLModel query to execute
            sanitize: If True, return sanitized result. If False, return raw result. Default: True

        Returns:
            First model instance (sanitized or raw) or None
        """
        return self.client.select_first(self.get_connection_string(), query, sanitize=sanitize)

    def select_all(self, query: SelectOfScalar[TAll], sanitize: bool = True) -> list[TAll]:
        """Execute a query and return all results.

        Args:
            query: SQLModel query to execute
            sanitize: If True, return sanitized results. If False, return raw results. Default: True

        Returns:
            List of model instances (sanitized or raw)
        """
        return self.client.select_all(self.get_connection_string(), query, sanitize=sanitize)

    def select_one(self, query: SelectOfScalar[TOne], sanitize: bool = True) -> TOne:
        """Execute a query and return exactly one result.

        Args:
            query: SQLModel query to execute
            sanitize: If True, return sanitized result. If False, return raw result. Default: True

        Returns:
            Single model instance (sanitized or raw)
        """
        return self.client.select_one(self.get_connection_string(), query, sanitize=sanitize)
