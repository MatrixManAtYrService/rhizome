"""Base classes for rhizome environments."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


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

    kube_context: str
    kube_namespace: str
    kube_deployment: str
    sql_connection: str
    remote_port: int  # Port on the remote pod/service


class Environment(ABC):
    """Abstract base class for rhizome environments."""

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
