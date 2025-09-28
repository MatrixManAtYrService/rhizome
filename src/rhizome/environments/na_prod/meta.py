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
from rhizome.models.meta.account import Account
from rhizome.models.meta.app_app_bundle import AppAppBundle
from rhizome.models.meta.app_bundle import AppBundle
from rhizome.models.meta.app_metered import AppMetered
from rhizome.models.meta.app_metered_country import AppMeteredCountry
from rhizome.models.meta.app_metered_event import AppMeteredEvent
from rhizome.models.meta.app_permission import AppPermission
from rhizome.models.meta.app_subscription import AppSubscription
from rhizome.models.meta.app_subscription_country import AppSubscriptionCountry
from rhizome.models.meta.country import Country
from rhizome.models.meta.developer import Developer
from rhizome.models.meta.developer_app import DeveloperApp
from rhizome.models.meta.device_events import DeviceEvents
from rhizome.models.meta.device_provision import DeviceProvision
from rhizome.models.meta.device_type import DeviceType
from rhizome.models.meta.locale import Locale
from rhizome.models.meta.merchant import Merchant
from rhizome.models.meta.merchant_address import MerchantAddress
from rhizome.models.meta.merchant_app import MerchantApp
from rhizome.models.meta.merchant_app_subscription_history import (
    MerchantAppSubscriptionHistory,
)
from rhizome.models.meta.merchant_boarding import MerchantBoarding
from rhizome.models.meta.merchant_creation_details import MerchantCreationDetails
from rhizome.models.meta.merchant_gateway import MerchantGateway
from rhizome.models.meta.merchant_merchant_plan_history import (
    MerchantMerchantPlanHistory,
)
from rhizome.models.meta.merchant_plan import MerchantPlan
from rhizome.models.meta.merchant_plan_group import MerchantPlanGroup
from rhizome.models.meta.merchant_plan_merchant_plan_group import (
    MerchantPlanMerchantPlanGroup,
)
from rhizome.models.meta.merchant_role import MerchantRole
from rhizome.models.meta.payment_processor import PaymentProcessor
from rhizome.models.meta.processor_key import ProcessorKey
from rhizome.models.meta.reseller import Reseller
from rhizome.models.meta.reseller_plan_trial import ResellerPlanTrial
from rhizome.models.meta.server_feature import ServerFeature
from rhizome.models.meta.terminal_config_merchant_props import (
    TerminalConfigMerchantProps,
)
from rhizome.models.meta.timezones import Timezones
from rhizome.models.table_list import MetaTable

models: dict[MetaTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    MetaTable.account: (Account, None),
    MetaTable.app_app_bundle: (AppAppBundle, None),
    MetaTable.app_bundle: (AppBundle, None),
    MetaTable.app_metered: (AppMetered, None),
    MetaTable.app_metered_country: (AppMeteredCountry, None),
    MetaTable.app_metered_event: (AppMeteredEvent, None),
    MetaTable.app_permission: (AppPermission, None),
    MetaTable.app_subscription: (AppSubscription, None),
    MetaTable.app_subscription_country: (AppSubscriptionCountry, None),
    MetaTable.country: (Country, None),
    MetaTable.developer: (Developer, None),
    MetaTable.developer_app: (DeveloperApp, None),
    MetaTable.device_events: (DeviceEvents, None),
    MetaTable.device_provision: (DeviceProvision, None),
    MetaTable.device_type: (DeviceType, None),
    MetaTable.locale: (Locale, None),
    MetaTable.merchant: (Merchant, None),
    MetaTable.merchant_address: (MerchantAddress, None),
    MetaTable.merchant_app: (MerchantApp, None),
    MetaTable.merchant_app_subscription_history: (MerchantAppSubscriptionHistory, None),
    MetaTable.merchant_boarding: (MerchantBoarding, None),
    MetaTable.merchant_creation_details: (MerchantCreationDetails, None),
    MetaTable.merchant_gateway: (MerchantGateway, None),
    MetaTable.merchant_merchant_plan_history: (MerchantMerchantPlanHistory, None),
    MetaTable.merchant_plan: (MerchantPlan, None),
    MetaTable.merchant_plan_group: (MerchantPlanGroup, None),
    MetaTable.merchant_plan_merchant_plan_group: (MerchantPlanMerchantPlanGroup, None),
    MetaTable.merchant_role: (MerchantRole, None),
    MetaTable.payment_processor: (PaymentProcessor, None),
    MetaTable.processor_key: (ProcessorKey, None),
    MetaTable.reseller: (Reseller, None),
    MetaTable.reseller_plan_trial: (ResellerPlanTrial, None),
    MetaTable.server_feature: (ServerFeature, None),
    MetaTable.terminal_config_merchant_props: (TerminalConfigMerchantProps, None),
    MetaTable.timezones: (Timezones, None),
}


class NorthAmericaMeta(Environment):
    """North America production meta environment using direct database connection."""

    def tables(self) -> list[StrEnum]:
        return list(MetaTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        if not isinstance(table_name, MetaTable):
            raise ValueError(f"Expected MetaTable, got {type(table_name)}")
        return models.get(table_name, (None, None))

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
