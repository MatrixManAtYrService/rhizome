"""
North America Production Billing environment configuration.

This module provides access to the North America production billing database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.na_prod.expected_data.billing_stage_charge import StageChargeNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing.stage_charge_v1 import StageChargeV1
from rhizome.models.table_list import BillingTable

models: dict[BillingTable, tuple[type[RhizomeModel], type[Emplacement]]] = {
    BillingTable.stage_charge: (StageChargeV1, StageChargeNaProd),
}

if TYPE_CHECKING:
    from rhizome.client import RhizomeClient


class NorthAmericaBilling(Environment):
    """North America production billing environment using direct database connection."""


    def tables(self) -> list[StrEnum]:
        return list(BillingTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement]]:
        if not isinstance(table_name, BillingTable):
            raise ValueError(f"Expected BillingTable, got {type(table_name)}")
        return models[table_name]


    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using pybritive temporary credentials."""
        import asyncio
        
        # Use the new generic credential system
        return asyncio.run(
            self.get_database_config_from_credentials(
                secret_reference="Resources/COS-RO-USProd/COS-RO-USProd-profile",
                secret_manager=SecretManager.PYBRITIVE,
                database_name="billing"
            )
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