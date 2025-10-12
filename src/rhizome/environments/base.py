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
TModel = TypeVar("TModel", bound="RhizomeModel")


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
class DatabaseConfigWithRW:
    """Database connection configuration with separate read-only and read-write credentials."""

    host: str
    port: int
    database: str

    # Read-only credentials (used by default)
    ro_username: str
    ro_password: str

    # Read-write credentials (requires user approval for each write operation)
    rw_username: str
    rw_password: str


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

    # Class-level set to track logged connections (shared across all environments)
    _logged_connections: set[tuple[str, int, str, str]] = set()

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

    def get_database_config_rw(self) -> DatabaseConfigWithRW | None:
        """
        Get the database configuration with RW credentials if available.

        Returns None by default. Environments that support write operations
        should override this method to provide RW credentials.

        Returns:
            DatabaseConfigWithRW if write access is supported, None otherwise
        """
        return None

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

    def get_versioned(self, model_class: type[TModel]) -> type[TModel]:
        """
        Get the appropriate versioned model class for this environment.

        This method takes a base model class and returns the correct versioned model (V1, V2, etc.) based on what
        `rhizome sync schema` has found for this specific environment. This allows writing version-agnostic code
        that works across environments with different schema versions.

        Args:
            model_class: The base model class (e.g., BillingEntityModel, MerchantEvolutionModel)

        Returns:
            The versioned model class appropriate for this environment.

            At runtime, this will be a specific version (e.g., BillingEntityV1, MerchantEvolutionV2). The type system
            treats it as the base class though, so attempts to reference version-specific columns will fail type
            checking. If version-specific usage is required, see the examples below.

        Raises:
            TypeError: If no matching model is found for the given base class

        Usage Pattern 1 - Totally version-agnostic (recommended for portable code):
            Use get_versioned() with base classes. Only access fields guaranteed to exist in all versions.

            >>> from rhizome.models.billing_bookkeeper.billing_entity import BillingEntity as BillingEntityModel
            >>> from sqlmodel import select
            >>>
            >>> db = DevBillingBookkeeper(client)
            >>> BillingEntity = db.get_versioned(BillingEntityModel)
            >>>
            >>> # Write code using only fields from the base class - works in any environment
            >>> entities = db.select_all(
            ...     select(BillingEntity).where(BillingEntity.entity_type == "RESELLER")
            ... )
            >>> for entity in entities:
            ...     print(entity.uuid, entity.name)  # Base fields work everywhere

        Usage Pattern 2 - Version-agnostic with runtime edge cases:
            Use get_versioned() with base classes, but handle specific versions when needed via match/case.

            >>> from rhizome.models.billing_event.merchant_evolution import MerchantEvolution as MerchantEvolutionModel
            >>> from rhizome.models.billing_event.merchant_evolution_v1 import MerchantEvolutionV1
            >>> from rhizome.models.billing_event.merchant_evolution_v2 import MerchantEvolutionV2
            >>>
            >>> db = DevBillingEvent(client)
            >>> MerchantEvolution = db.get_versioned(MerchantEvolutionModel)
            >>>
            >>> merchant = db.select_first(select(MerchantEvolution).where(...))
            >>> match merchant:
            ...     case MerchantEvolutionV2():
            ...         # Type checker knows this is V2 with billable_merchant_type field
            ...         print(f"Billable type: {merchant.billable_merchant_type}")
            ...     case MerchantEvolutionV1():
            ...         # Type checker knows this is V1 without that field
            ...         print("V1 merchant - no billable type field")
            ...     case _:
            ...         raise TypeError(f"Unknown merchant evolution version: {type(merchant)}")

        Usage Pattern 3 - Totally version-explicit (not portable):
            Import and use versioned classes directly. Ties code to specific schema version.

            >>> from rhizome.models.billing_event.merchant_evolution_v2 import MerchantEvolutionV2
            >>> from sqlmodel import select
            >>>
            >>> db = DevBillingEvent(client)
            >>> merchants = db.select_all(select(MerchantEvolutionV2).where(...))
            >>> for merchant in merchants:
            ...     print(merchant.billable_merchant_type)  # V2-specific field

            This approach fails in environments using different versions (e.g., production uses V1).
            Only use when you know the target environment and need version-specific fields throughout.

        Usage Pattern 4 - Environment-specific aliases:
            Use type aliases on environment classes for environment-specific but version-agnostic code.
            This provides compile-time type safety for the specific version an environment uses.

            >>> from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
            >>> from sqlmodel import select
            >>>
            >>> # DevBillingBookkeeper.BillingEntity is a type alias to BillingEntityV1
            >>> db = DevBillingBookkeeper(client)
            >>> entities = db.select_all(
            ...     select(DevBillingBookkeeper.BillingEntity)
            ...     .where(DevBillingBookkeeper.BillingEntity.entity_type == "RESELLER")
            ... )
            >>> for entity in entities:
            ...     print(entity.uuid, entity.name)  # Type checker knows V1 fields

            This pattern is ideal for environment-specific code (scripts, tests) that needs
            type-checked access to version-specific fields while remaining portable within
            that environment.
        """
        # Search through table_situation for a model that is a subclass of the requested base class
        for env_model_class, _ in self.table_situation.values():
            if env_model_class is not None and issubclass(env_model_class, model_class):
                return env_model_class

        raise TypeError(
            f"No model found for {model_class.__name__} in environment {self.name}. "
            f"Available models: {', '.join(m.__name__ for m, _ in self.table_situation.values() if m is not None)}"
        )

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
            self.get_secret(port_forward_config.secret_reference, port_forward_config.secret_manager)
        )
        return DatabaseConfig(
            host="127.0.0.1",
            port=self.local_port,
            database=port_forward_config.database_name,
            username=port_forward_config.username,
            password=password,
        )

    async def get_secret(self, secret_reference: str, secret_manager: SecretManager) -> str:
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

    def _log_connection_if_new(self, db_config: DatabaseConfig, mysql_command: str) -> None:
        """
        Log database connection details to rhizome server if not already logged.

        Args:
            db_config: Database configuration to log
            mysql_command: MySQL command string for debugging (should have password redacted)
        """
        from contextlib import suppress

        import httpx

        connection_key = (db_config.host, db_config.port, db_config.username, db_config.database)
        if connection_key not in Environment._logged_connections:
            # Send connection details to rhizome server (fire-and-forget)
            with suppress(Exception):
                httpx.post(
                    f"{self.client.base_url}/log_connection",
                    json={
                        "host": db_config.host,
                        "port": db_config.port,
                        "username": db_config.username,
                        "database": db_config.database,
                        "mysql_command": mysql_command,
                    },
                    timeout=1.0,
                )

            Environment._logged_connections.add(connection_key)

    def get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        db_config = self.get_database_config()
        encoded_password = quote_plus(db_config.password)
        connection_string = f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}"

        # Log connection details
        mysql_command = (
            f"mysql --user={db_config.username} --password=[REDACTED] --host={db_config.host} "
            f"--port={db_config.port} --batch {db_config.database}"
        )
        self._log_connection_if_new(db_config, mysql_command)

        return connection_string

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
