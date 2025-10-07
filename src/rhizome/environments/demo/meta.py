"""
Demo Meta environment configuration.

This module provides access to the demo meta database
through direct connection using legacy MySQL credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.table_list import MetaTable

# Declare all meta tables with None mappings - models/emplacements to be added later
models: dict[MetaTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    MetaTable.account: (None, None),
    MetaTable.country: (None, None),
    MetaTable.device_type: (None, None),
    MetaTable.server_feature: (None, None),
    MetaTable.merchant: (None, None),
    MetaTable.terminal_config_merchant_props: (None, None),
    MetaTable.reseller: (None, None),
    MetaTable.merchant_address: (None, None),
    MetaTable.merchant_gateway: (None, None),
    MetaTable.payment_processor: (None, None),
    MetaTable.processor_key: (None, None),
    MetaTable.merchant_plan: (None, None),
    MetaTable.merchant_plan_group: (None, None),
    MetaTable.merchant_plan_merchant_plan_group: (None, None),
    MetaTable.merchant_role: (None, None),
    MetaTable.developer: (None, None),
    MetaTable.locale: (None, None),
    MetaTable.timezones: (None, None),
    MetaTable.app_app_bundle: (None, None),
    MetaTable.app_bundle: (None, None),
    MetaTable.app_metered: (None, None),
    MetaTable.app_metered_country: (None, None),
    MetaTable.app_metered_event: (None, None),
    MetaTable.app_permission: (None, None),
    MetaTable.app_subscription: (None, None),
    MetaTable.app_subscription_country: (None, None),
    MetaTable.developer_app: (None, None),
    MetaTable.device_events: (None, None),
    MetaTable.device_provision: (None, None),
    MetaTable.merchant_app: (None, None),
    MetaTable.merchant_app_subscription_history: (None, None),
    MetaTable.merchant_boarding: (None, None),
    MetaTable.merchant_creation_details: (None, None),
    MetaTable.merchant_merchant_plan_history: (None, None),
    MetaTable.reseller_plan_trial: (None, None),
}


class DemoMeta(Environment):
    """Demo meta environment using direct database connection."""

    def tables(self) -> list[StrEnum]:
        return list(MetaTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        if not isinstance(table_name, MetaTable):
            raise ValueError(f"Expected MetaTable, got {type(table_name)}")
        return models.get(table_name, (None, None))

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using legacy MySQL credentials."""
        import asyncio

        password = asyncio.run(
            self._get_secret("op://Shared/MysqlDevLegacy/password", SecretManager.ONEPASSWORD)
        )

        return DatabaseConfig(
            host="demo2-db01.dev.pdx10.clover.network",
            port=3306,
            database="meta",
            username="remotereadonly",
            password=password,
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DemoMeta"

    def get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        from urllib.parse import quote_plus

        import structlog

        log = structlog.get_logger()
        db_config = self.get_database_config()
        encoded_password = quote_plus(db_config.password)
        connection_string = f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}?ssl_verify_cert=false"

        # Log the MySQL command equivalent for debugging (with redacted password)
        mysql_command = (
            f"mysql --user={db_config.username} --password=[REDACTED] --host={db_config.host} "
            f"--port={db_config.port} --batch --skip-ssl-verify-server-cert {db_config.database}"
        )
        log.info(
            "MySQL connection details",
            mysql_command=mysql_command,
            host=db_config.host,
            port=db_config.port,
            username=db_config.username,
            database=db_config.database,
        )

        return connection_string
