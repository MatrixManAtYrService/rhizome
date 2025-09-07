"""
North America Production Billing environment configuration.

This module provides access to the North America production billing database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from rhizome.environments.base import DatabaseConfig, PortForwardConfig
from rhizome.environments.database_environment import DatabaseEnvironment
from rhizome.environments.na_prod.expected_data.billing_stage_charge import StageChargeNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing.stage_charge_v1 import StageChargeV1
from rhizome.models.billing.table_list import BillingTable

models: dict[BillingTable, tuple[type[RhizomeModel], type[Emplacement]]] = {
    BillingTable.stage_charge: (StageChargeV1, StageChargeNaProd),
}

if TYPE_CHECKING:
    from rhizome.client import RhizomeClient


class NorthAmericaBilling(DatabaseEnvironment):
    """North America production billing environment using direct database connection."""

    def __init__(self, client) -> None:
        """Initialize North America billing environment with direct connection (no port forwarding)."""
        self.client = client
        
        # Initialize table_situation without port forwarding setup
        self.table_situation = {
            table: (self.situate_table(table)) for table in self.tables()
        }

    def tables(self) -> list[StrEnum]:
        return list(BillingTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement]]:
        if not isinstance(table_name, BillingTable):
            raise ValueError(f"Expected BillingTable, got {type(table_name)}")
        return models[table_name]

    # Since this environment uses direct connection, we need to provide stubs for the abstract methods
    # that DatabaseEnvironment expects, but they won't be called due to our custom __init__
    def get_kube_context(self) -> str:
        raise NotImplementedError("Direct connection environment - no Kubernetes context needed")
    
    def get_kube_namespace(self) -> str:
        raise NotImplementedError("Direct connection environment - no Kubernetes namespace needed")
    
    def get_kube_deployment(self) -> str:
        raise NotImplementedError("Direct connection environment - no Kubernetes deployment needed")
    
    def get_sql_connection(self) -> str:
        raise NotImplementedError("Direct connection environment - no CloudSQL connection needed")
    
    def get_project(self) -> str:
        raise NotImplementedError("Direct connection environment - no GCP project needed")
    
    def get_cluster_name(self) -> str:
        raise NotImplementedError("Direct connection environment - no cluster name needed")
    
    def get_cluster_region(self) -> str:
        raise NotImplementedError("Direct connection environment - no cluster region needed")
    
    def get_cluster_server(self) -> str:
        raise NotImplementedError("Direct connection environment - no cluster server needed")
    
    def get_database_name(self) -> str:
        return "billing"
    
    def get_username(self) -> str:
        raise NotImplementedError("Direct connection environment - username obtained from pybritive")
    
    def get_onepassword_reference(self) -> str:
        raise NotImplementedError("Direct connection environment - credentials from pybritive")

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using pybritive temporary credentials."""
        import asyncio
        
        # Get temporary credentials from pybritive
        britive_info = asyncio.run(
            self.client.tools.pybritive.checkout("Resources/COS-RO-USProd/COS-RO-USProd-profile")
        )
        
        return DatabaseConfig(
            host=britive_info.host,
            port=britive_info.port,
            database="billing",
            username=britive_info.username,
            password=britive_info.password,
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBilling"

    def _get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        import structlog
        from urllib.parse import quote_plus
        
        log = structlog.get_logger()
        db_config = self.get_database_config()
        encoded_password = quote_plus(db_config.password)
        connection_string = f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}?ssl_verify_cert=false"
        
        # Log the MySQL command equivalent for debugging (with redacted password)
        mysql_command = f"mysql --user={db_config.username} --password=[REDACTED] --host={db_config.host} --port={db_config.port} --batch --skip-ssl-verify-server-cert {db_config.database}"
        log.info("MySQL connection details", 
                mysql_command=mysql_command,
                host=db_config.host, 
                port=db_config.port, 
                username=db_config.username, 
                database=db_config.database)
        
        return connection_string

    def select_first(self, query):
        """Execute a query and return the first sanitized result or None."""
        return self.client.select_first(self._get_connection_string(), query)

    def select_all(self, query):
        """Execute a query and return all sanitized results."""
        return self.client.select_all(self._get_connection_string(), query)

    def select_one(self, query):
        """Execute a query and return exactly one sanitized result."""
        return self.client.select_one(self._get_connection_string(), query)

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBilling"