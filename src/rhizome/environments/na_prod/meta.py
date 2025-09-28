"""
North America Production Meta environment configuration.

This module provides access to the North America production meta database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.table_list import MetaTable

models: dict[MetaTable, tuple[type[RhizomeModel], type[Emplacement[Any]]]] = {
    # This will be populated after running rhizome sync schema and creating models.
}


class NorthAmericaMeta(Environment):
    """North America production meta environment using direct database connection."""

    def tables(self) -> list[StrEnum]:
        return list(MetaTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, MetaTable):
            raise ValueError(f"Expected MetaTable, got {type(table_name)}")
        return models[table_name]

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using pybritive temporary credentials."""
        import asyncio

        meta_pattern = r"""
            Temp\sMySQL\susername:\s*(?P<username>\S+).*
            Temp\spassword:\s*(?P<password>\S+).*
            For\sorders\sin\susprod\sconnect\sto\sserver:\s*(?P<host>[^:]+):(?P<port>\d+)
        """

        return asyncio.run(
            self.get_database_config_from_credentials(
                secret_reference="Resources/COS-RO-USProd/COS-RO-USProd-profile",
                secret_manager=SecretManager.PYBRITIVE,
                database_name="meta",
                pattern=meta_pattern,
            )
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaMeta"

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
