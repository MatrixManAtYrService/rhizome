"""
Base class for database environments with CloudSQL port forwarding.

This module provides a reusable base class for database environments that need
CloudSQL proxy port forwarding and credential management.
"""

from __future__ import annotations

import asyncio
import socket
from abc import ABC, abstractmethod
from enum import Enum, StrEnum
from typing import TYPE_CHECKING, TypeVar
from urllib.parse import quote_plus

from rhizome.client import RhizomeClient
from rhizome.cluster import connect_cluster
from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig
from rhizome.models.base import RhizomeModel, Emplacement
from rhizome.portforward import cloudsql_port_forward

if TYPE_CHECKING:
    from sqlmodel.sql._expression_select_cls import SelectOfScalar

    from rhizome.models.base import RhizomeModel

TFirst = TypeVar("TFirst", bound="RhizomeModel")
TAll = TypeVar("TAll", bound="RhizomeModel")
TOne = TypeVar("TOne", bound="RhizomeModel")


class DatabaseEnvironment(Environment, ABC):
    """Base class for database environments."""

    
    table_situation: dict[StrEnum, tuple[type[RhizomeModel], type[Emplacement]]]


    @abstractmethod
    def tables(self) -> list[StrEnum]:
        """
        Returns a list of table names expected to be present in this environment.
        Need not be exhaustive, just include the ones that we need to work with.
        """


    @abstractmethod
    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement]]:
        """
        Indicates which data should be expected from which table.
        Returns tuple of (ModelClass, EmplacementClass).
        """

    def __init__(self, client: RhizomeClient) -> None:
        """Initialize database environment with CloudSQL port forwarding."""
        self.client = client
        self.local_port = self._find_unused_port()

        # Connect to the cluster first
        asyncio.run(
            connect_cluster(
                project=self.get_project(),
                cluster=self.get_cluster_name(),
                region=self.get_cluster_region(),
                server=self.get_cluster_server(),
                tools=client.tools,
            )
        )

        # Start CloudSQL port forward using the environment-specific configuration
        asyncio.run(
            cloudsql_port_forward(
                kube_context=self.get_kube_context(),
                kube_namespace=self.get_kube_namespace(),
                kube_deployment=self.get_kube_deployment(),
                sql_connection=self.get_sql_connection(),
                local_port=self.local_port,
                tools=client.tools,
            )
        )

        # get models and expected data from child class
        self.table_situation = {
            table: (self.situate_table(table)) for table in self.tables()
        }

    def _find_unused_port(self, start_port: int = 30000) -> int:
        """Find an unused local port starting from the given port number."""
        for port in range(start_port, start_port + 1000):  # Try 1000 ports
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('127.0.0.1', port))
                    return port
            except OSError:
                continue  # Port is in use, try the next one
        raise RuntimeError("No unused ports available in range")

    @abstractmethod
    def get_project(self) -> str:
        """Get the Google Cloud project for this environment."""

    @abstractmethod
    def get_cluster_name(self) -> str:
        """Get the Kubernetes cluster name for this environment."""

    @abstractmethod
    def get_cluster_region(self) -> str:
        """Get the Kubernetes cluster region for this environment."""

    @abstractmethod
    def get_cluster_server(self) -> str:
        """Get the Kubernetes cluster server for this environment."""

    @abstractmethod
    def get_kube_context(self) -> str:
        """Get the Kubernetes context for this environment."""

    @abstractmethod
    def get_kube_namespace(self) -> str:
        """Get the Kubernetes namespace for this environment."""

    @abstractmethod
    def get_kube_deployment(self) -> str:
        """Get the Kubernetes deployment for this environment."""

    @abstractmethod
    def get_sql_connection(self) -> str:
        """Get the SQL connection string for CloudSQL."""

    @abstractmethod
    def get_database_name(self) -> str:
        """Get the database name for this environment."""

    @abstractmethod
    def get_username(self) -> str:
        """Get the database username for this environment."""

    @abstractmethod
    def get_onepassword_reference(self) -> str:
        """Get the 1Password reference for credentials."""


    def get_database_config(self) -> DatabaseConfig:
        """Get database config using 1Password for credentials."""
        # Get password from 1Password
        password = asyncio.run(self.client.tools.onepassword.read_secret(self.get_onepassword_reference()))

        return DatabaseConfig(
            host="127.0.0.1",
            port=self.local_port,
            database=self.get_database_name(),
            username=self.get_username(),
            password=password,
        )

    def get_port_forward_config(self) -> PortForwardConfig:
        """Get port forward config for CloudSQL proxy."""
        return PortForwardConfig(
            kube_context=self.get_kube_context(),
            kube_namespace=self.get_kube_namespace(),
            kube_deployment=self.get_kube_deployment(),
            sql_connection=self.get_sql_connection(),
            remote_port=3306,  # Will be discovered from logs
        )

    def _get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        db_config = self.get_database_config()
        encoded_password = quote_plus(db_config.password)
        return f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}"

    def select_first(self, query: SelectOfScalar[TFirst]) -> TFirst | None:
        """Execute a query and return the first sanitized result or None."""
        return self.client.select_first(self._get_connection_string(), query)

    def select_all(self, query: SelectOfScalar[TAll]) -> list[TAll]:
        """Execute a query and return all sanitized results."""
        return self.client.select_all(self._get_connection_string(), query)

    def select_one(self, query: SelectOfScalar[TOne]) -> TOne:
        """Execute a query and return exactly one sanitized result."""
        return self.client.select_one(self._get_connection_string(), query)
