"""
North America Production Billing environment configuration.

This module provides access to the North America production billing database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig
from rhizome.models.na_billing.stage_charge_v1 import StageChargeV1


class NorthAmericaBillingModel(Enum):
    """Table version mapping for NorthAmericaBilling environment."""
    StageCharge = StageChargeV1

if TYPE_CHECKING:
    from rhizome.client import RhizomeClient


class NorthAmericaBilling(Environment):
    """North America production billing environment using direct database connection."""

    def __init__(self, client: RhizomeClient) -> None:
        """Initialize North America billing environment with pybritive credentials."""
        self.client = client

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