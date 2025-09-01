"""
NA Production Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
na-prod-us-central1 cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, TypeVar

from rhizome.client import RhizomeClient
from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig
from rhizome.portforward import cloudsql_port_forward

if TYPE_CHECKING:
    from sqlmodel.sql._expression_select_cls import SelectOfScalar

    from rhizome.models.base import SanitizableModel

TFirst = TypeVar("TFirst", bound="SanitizableModel")
TAll = TypeVar("TAll", bound="SanitizableModel")
TOne = TypeVar("TOne", bound="SanitizableModel")


class NorthAmericaBookkeeper(Environment):
    """North America production bookkeeper environment using CloudSQL."""

    def __init__(self, client: RhizomeClient) -> None:
        """Initialize NA production environment, setting up CloudSQL port forwarding."""
        self.client = client
        self.local_port = 31001  # From local-ports.nu bb_prod_port

        # Start CloudSQL port forward using the production flow
        # This will handle credential retrieval, proxy setup, and port discovery
        asyncio.run(
            cloudsql_port_forward(
                kube_context="gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster",
                kube_namespace="gke-cloudsql-access",
                kube_deployment="gke-cloudsql-access",
                sql_connection="clover-prod-databases:us-central1:billing-bookkeeper",
                local_port=self.local_port,
                tools=client.tools,
            )
        )

    def get_database_config(self) -> DatabaseConfig:
        """Get database config for NA production bookkeeper."""
        # Get password from 1Password
        password = asyncio.run(self.client.tools.onepassword.read_secret("op://Shared/EventBillingROCred/password"))

        return DatabaseConfig(
            host="127.0.0.1",
            port=self.local_port,
            database="billing-bookkeeper-prod",
            username="billing-bookkeeper-ro",
            password=password,
        )

    def get_port_forward_config(self) -> PortForwardConfig:
        """Get port forward config for CloudSQL proxy."""
        return PortForwardConfig(
            kube_context="gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster",
            kube_namespace="gke-cloudsql-access",
            kube_deployment="gke-cloudsql-access",
            sql_connection="clover-prod-databases:us-central1:billing-bookkeeper",
            remote_port=3306,  # Will be discovered from logs
        )

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBookkeeper"

    def _get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        db_config = self.get_database_config()
        return f"mysql+pymysql://{db_config.username}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}"

    def select_first(self, query: SelectOfScalar[TFirst]) -> TFirst | None:
        """Execute a query and return the first sanitized result or None."""
        return self.client.select_first(self._get_connection_string(), query)

    def select_all(self, query: SelectOfScalar[TAll]) -> list[TAll]:
        """Execute a query and return all sanitized results."""
        return self.client.select_all(self._get_connection_string(), query)

    def select_one(self, query: SelectOfScalar[TOne]) -> TOne:
        """Execute a query and return exactly one sanitized result."""
        return self.client.select_one(self._get_connection_string(), query)
