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

from rhizome.environments.na_prod.expected_data.meta_locale import LocaleNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant import MerchantNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_address import MerchantAddressNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_app import MerchantAppNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_app_subscription_history import (
    MerchantAppSubscriptionHistoryNaProd,
)
from rhizome.environments.na_prod.expected_data.meta_merchant_boarding import MerchantBoardingNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_creation_details import (
    MerchantCreationDetailsNaProd,
)
from rhizome.environments.na_prod.expected_data.meta_merchant_gateway import MerchantGatewayNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_merchant_plan_history import (
    MerchantMerchantPlanHistoryNaProd,
)
from rhizome.environments.na_prod.expected_data.meta_merchant_plan import MerchantPlanNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_plan_group import MerchantPlanGroupNaProd
from rhizome.environments.na_prod.expected_data.meta_merchant_plan_merchant_plan_group import (
    MerchantPlanMerchantPlanGroupNaProd,
)
from rhizome.environments.na_prod.expected_data.meta_merchant_role import MerchantRoleNaProd
from rhizome.environments.na_prod.expected_data.meta_payment_processor import PaymentProcessorNaProd
from rhizome.environments.na_prod.expected_data.meta_processor_key import ProcessorKeyNaProd
from rhizome.environments.na_prod.expected_data.meta_reseller import ResellerNaProd
from rhizome.environments.na_prod.expected_data.meta_reseller_plan_trial import ResellerPlanTrialNaProd
from rhizome.environments.na_prod.expected_data.meta_server_feature import ServerFeatureNaProd
from rhizome.environments.na_prod.expected_data.meta_terminal_config_merchant_props import (
    TerminalConfigMerchantPropsNaProd,
)
from rhizome.environments.na_prod.expected_data.meta_timezones import TimezonesNaProd
from rhizome.environments.na_prod.expected_data.meta_account import AccountNaProd
from rhizome.environments.na_prod.expected_data.meta_app_app_bundle import AppAppBundleNaProd
from rhizome.environments.na_prod.expected_data.meta_app_bundle import AppBundleNaProd
from rhizome.environments.na_prod.expected_data.meta_app_metered import AppMeteredNaProd
from rhizome.environments.na_prod.expected_data.meta_app_metered_country import AppMeteredCountryNaProd
from rhizome.environments.na_prod.expected_data.meta_app_metered_event import AppMeteredEventNaProd
from rhizome.environments.na_prod.expected_data.meta_app_permission import AppPermissionNaProd
from rhizome.environments.na_prod.expected_data.meta_app_subscription import AppSubscriptionNaProd
from rhizome.environments.na_prod.expected_data.meta_app_subscription_country import AppSubscriptionCountryNaProd
from rhizome.environments.na_prod.expected_data.meta_country import CountryNaProd
from rhizome.environments.na_prod.expected_data.meta_developer import DeveloperNaProd
from rhizome.environments.na_prod.expected_data.meta_developer_app import DeveloperAppNaProd
from rhizome.environments.na_prod.expected_data.meta_device_events import DeviceEventsNaProd
from rhizome.environments.na_prod.expected_data.meta_device_provision import DeviceProvisionNaProd
from rhizome.environments.na_prod.expected_data.meta_device_type import DeviceTypeNaProd

models: dict[MetaTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    MetaTable.account: (Account, AccountNaProd),
    MetaTable.app_app_bundle: (AppAppBundle, AppAppBundleNaProd),
    MetaTable.app_bundle: (AppBundle, AppBundleNaProd),
    MetaTable.app_metered: (AppMetered, AppMeteredNaProd),
    MetaTable.app_metered_country: (AppMeteredCountry, AppMeteredCountryNaProd),
    MetaTable.app_metered_event: (AppMeteredEvent, AppMeteredEventNaProd),
    MetaTable.app_permission: (AppPermission, AppPermissionNaProd),
    MetaTable.app_subscription: (AppSubscription, AppSubscriptionNaProd),
    MetaTable.app_subscription_country: (AppSubscriptionCountry, AppSubscriptionCountryNaProd),
    MetaTable.country: (Country, CountryNaProd),
    MetaTable.developer: (Developer, DeveloperNaProd),
    MetaTable.developer_app: (DeveloperApp, DeveloperAppNaProd),
    MetaTable.device_events: (DeviceEvents, DeviceEventsNaProd),
    MetaTable.device_provision: (DeviceProvision, DeviceProvisionNaProd),
    MetaTable.device_type: (DeviceType, DeviceTypeNaProd),
    MetaTable.locale: (Locale, LocaleNaProd),
    MetaTable.merchant: (Merchant, MerchantNaProd),
    MetaTable.merchant_address: (MerchantAddress, MerchantAddressNaProd),
    MetaTable.merchant_app: (MerchantApp, MerchantAppNaProd),
    MetaTable.merchant_app_subscription_history: (MerchantAppSubscriptionHistory, MerchantAppSubscriptionHistoryNaProd),
    MetaTable.merchant_boarding: (MerchantBoarding, MerchantBoardingNaProd),
    MetaTable.merchant_creation_details: (MerchantCreationDetails, MerchantCreationDetailsNaProd),
    MetaTable.merchant_gateway: (MerchantGateway, MerchantGatewayNaProd),
    MetaTable.merchant_merchant_plan_history: (MerchantMerchantPlanHistory, MerchantMerchantPlanHistoryNaProd),
    MetaTable.merchant_plan: (MerchantPlan, MerchantPlanNaProd),
    MetaTable.merchant_plan_group: (MerchantPlanGroup, MerchantPlanGroupNaProd),
    MetaTable.merchant_plan_merchant_plan_group: (MerchantPlanMerchantPlanGroup, MerchantPlanMerchantPlanGroupNaProd),
    MetaTable.merchant_role: (MerchantRole, MerchantRoleNaProd),
    MetaTable.payment_processor: (PaymentProcessor, PaymentProcessorNaProd),
    MetaTable.processor_key: (ProcessorKey, ProcessorKeyNaProd),
    MetaTable.reseller: (Reseller, ResellerNaProd),
    MetaTable.reseller_plan_trial: (ResellerPlanTrial, ResellerPlanTrialNaProd),
    MetaTable.server_feature: (ServerFeature, ServerFeatureNaProd),
    MetaTable.terminal_config_merchant_props: (TerminalConfigMerchantProps, TerminalConfigMerchantPropsNaProd),
    MetaTable.timezones: (Timezones, TimezonesNaProd),
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
