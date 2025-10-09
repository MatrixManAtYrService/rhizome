"""Base classes for rhizome environments."""

from __future__ import annotations

import asyncio
import socket
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import TYPE_CHECKING, Any, TypeVar
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from sqlmodel.sql._expression_select_cls import SelectOfScalar

    from rhizome.client import RhizomeClient
    from rhizome.models.base import Emplacement, RhizomeModel

TFirst = TypeVar("TFirst", bound="RhizomeModel")
TAll = TypeVar("TAll", bound="RhizomeModel")
TOne = TypeVar("TOne", bound="RhizomeModel")


class SecretManager(StrEnum):
    """Enum for credential management systems."""

    ONEPASSWORD = auto()
    PYBRITIVE = auto()


@dataclass
class DatabaseConfig:
    """Database connection configuration."""

    host: str
    port: int
    database: str
    username: str
    password: str


@dataclass
class PortForwardConfig:
    """Port forwarding configuration for Kubernetes environments."""

    # Kubernetes cluster information
    project: str
    cluster: str
    region: str
    server: str

    # Kubernetes connection details
    kube_context: str
    kube_namespace: str
    kube_deployment: str
    sql_connection: str

    # Database connection details
    database_name: str
    username: str
    secret_reference: str
    secret_manager: SecretManager = SecretManager.ONEPASSWORD

    # Port configuration
    remote_port: int = 3306  # Port on the remote pod/service


class Environment(ABC):
    """Abstract base class for rhizome environments."""

    table_situation: dict[StrEnum, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]]

    @abstractmethod
    def tables(self) -> list[StrEnum]:
        """
        Returns a list of table names expected to be present in this environment.
        Need not be exhaustive, just include the ones that we need to work with.
        """

    @abstractmethod
    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        """
        Indicates which data should be expected from which table.
        Returns tuple of (ModelClass, EmplacementClass).
        """

    @abstractmethod
    def get_database_config(self) -> DatabaseConfig:
        """Get the database configuration for this environment."""

    @abstractmethod
    def get_port_forward_config(self) -> PortForwardConfig | None:
        """Get port forwarding config, or None if direct connection."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""

    def __init__(self, client: RhizomeClient) -> None:
        """Initialize environment with optional port forwarding."""
        self.client = client

        # Set up port forwarding if needed
        port_forward_config = self.get_port_forward_config()
        if port_forward_config is not None:
            self.setup_port_forwarding(port_forward_config)

        # Initialize table situation
        self.table_situation = {table: self.situate_table(table) for table in self.tables()}

    def get_model(self, table_name: StrEnum) -> type[RhizomeModel]:
        """
        Get the appropriate model class for a given table in this environment.

        This method returns the correct versioned model (V1, V2, etc.) based on
        what this specific environment is configured to use, eliminating the need
        for users to know which version to import.

        Args:
            table_name: The table enum value (e.g., BillingBookkeeperTable.fee_summary)

        Returns:
            The model class appropriate for this environment (e.g., FeeSummaryV1 or FeeSummaryV2)

        Raises:
            KeyError: If the table is not configured for this environment
            ValueError: If the table's model class is None (not yet implemented)

        Example:
            >>> db = DevBillingBookkeeper(client)
            >>> FeeSummary = db.get_model(BillingBookkeeperTable.fee_summary)
            >>> # FeeSummary is now the correct version for DevBillingBookkeeper
        """
        if table_name not in self.table_situation:
            raise KeyError(
                f"Table {table_name} is not configured for environment {self.name}. "
                f"Available tables: {', '.join(str(t) for t in self.table_situation)}"
            )

        model_class, _ = self.table_situation[table_name]

        if model_class is None:
            raise ValueError(
                f"Model for table {table_name} is not yet implemented in environment {self.name}. "
                f"Please check if the model class has been created and registered."
            )

        return model_class

    def setup_port_forwarding(self, config: PortForwardConfig) -> None:
        """Set up port forwarding using the provided configuration."""
        from rhizome.cluster import connect_cluster
        from rhizome.portforward import cloudsql_port_forward

        self.local_port = self._find_unused_port()

        # Connect to the cluster first
        asyncio.run(
            connect_cluster(
                project=config.project,
                cluster=config.cluster,
                region=config.region,
                server=config.server,
                tools=self.client.tools,
            )
        )

        # Start CloudSQL port forward
        asyncio.run(
            cloudsql_port_forward(
                kube_context=config.kube_context,
                kube_namespace=config.kube_namespace,
                kube_deployment=config.kube_deployment,
                sql_connection=config.sql_connection,
                local_port=self.local_port,
                tools=self.client.tools,
            )
        )

    def get_database_config_from_port_forward(self, port_forward_config: PortForwardConfig) -> DatabaseConfig:
        """Helper method to get database config for port forwarding environments."""
        password = asyncio.run(
            self._get_secret(port_forward_config.secret_reference, port_forward_config.secret_manager)
        )
        return DatabaseConfig(
            host="127.0.0.1",
            port=self.local_port,
            database=port_forward_config.database_name,
            username=port_forward_config.username,
            password=password,
        )

    async def _get_secret(self, secret_reference: str, secret_manager: SecretManager) -> str:
        """Get secret from the appropriate credential manager."""
        if secret_manager == SecretManager.ONEPASSWORD:
            return await self.client.tools.onepassword.read_secret(secret_reference)
        elif secret_manager == SecretManager.PYBRITIVE:
            # For pybritive, the secret_reference is the resource path
            britive_info = await self.client.tools.pybritive.checkout(secret_reference)
            return britive_info.password
        else:
            raise ValueError(f"Unsupported secret manager: {secret_manager}")

    async def get_database_config_from_credentials(
        self,
        secret_reference: str,
        secret_manager: SecretManager,
        database_name: str,
        pattern: str | None = None,
    ) -> DatabaseConfig:
        """Helper method to get database config for direct credential access (pybritive)."""
        if secret_manager == SecretManager.PYBRITIVE:
            # For pybritive, we get all connection details from the checkout
            britive_info = await self.client.tools.pybritive.checkout(
                resource_path=secret_reference, pattern=pattern, database_name=database_name
            )
            return DatabaseConfig(
                host=britive_info.host,
                port=britive_info.port,
                database=database_name,
                username=britive_info.username,
                password=britive_info.password,
            )
        elif secret_manager == SecretManager.ONEPASSWORD:
            # OnePassword only provides passwords, not full connection details
            raise ValueError("OnePassword requires port forwarding configuration for connection details")
        else:
            raise ValueError(f"Unsupported secret manager: {secret_manager}")

    def _find_unused_port(self, start_port: int = 30000) -> int:
        """Find an unused local port starting from the given port number."""
        for port in range(start_port, start_port + 1000):  # Try 1000 ports
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(("127.0.0.1", port))
                    return port
            except OSError:
                continue  # Port is in use, try the next one
        raise RuntimeError("No unused ports available in range")

    def get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        db_config = self.get_database_config()
        encoded_password = quote_plus(db_config.password)
        return f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}"

    def select_first(self, query: SelectOfScalar[TFirst]) -> TFirst | None:
        """Execute a query and return the first sanitized result or None."""
        return self.client.select_first(self.get_connection_string(), query)

    def select_all(self, query: SelectOfScalar[TAll]) -> list[TAll]:
        """Execute a query and return all sanitized results."""
        return self.client.select_all(self.get_connection_string(), query)

    def select_one(self, query: SelectOfScalar[TOne]) -> TOne:
        """Execute a query and return exactly one sanitized result."""
        return self.client.select_one(self.get_connection_string(), query)
