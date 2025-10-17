"""
North America Production Meta environment configuration.

This module provides access to the North America production meta database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager, Tools
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
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.meta.account import Account
from rhizome.models.meta.app_app_bundle_v1 import AppAppBundleV1
from rhizome.models.meta.app_bundle_v1 import AppBundleV1
from rhizome.models.meta.app_metered_country_v1 import AppMeteredCountryV1
from rhizome.models.meta.app_metered_event_v1 import AppMeteredEventV1
from rhizome.models.meta.app_metered_v1 import AppMeteredV1
from rhizome.models.meta.app_permission_v1 import AppPermissionV1
from rhizome.models.meta.app_subscription_country_v1 import AppSubscriptionCountryV1
from rhizome.models.meta.app_subscription_v1 import AppSubscriptionV1
from rhizome.models.meta.country import Country
from rhizome.models.meta.developer import Developer
from rhizome.models.meta.developer_app_v1 import DeveloperAppV1
from rhizome.models.meta.device_events_v1 import DeviceEventsV1
from rhizome.models.meta.device_provision_v1 import DeviceProvisionV1
from rhizome.models.meta.device_type_v1 import DeviceTypeV1
from rhizome.models.meta.locale import Locale
from rhizome.models.meta.merchant import Merchant
from rhizome.models.meta.merchant_address_v1 import MerchantAddressV1
from rhizome.models.meta.merchant_app_subscription_history_v1 import (
    MerchantAppSubscriptionHistoryV1,
)
from rhizome.models.meta.merchant_app_v1 import MerchantAppV1
from rhizome.models.meta.merchant_boarding_v1 import MerchantBoardingV1
from rhizome.models.meta.merchant_creation_details_v1 import MerchantCreationDetailsV1
from rhizome.models.meta.merchant_gateway_v1 import MerchantGatewayV1
from rhizome.models.meta.merchant_merchant_plan_history_v1 import (
    MerchantMerchantPlanHistoryV1,
)
from rhizome.models.meta.merchant_plan_group_v1 import MerchantPlanGroupV1
from rhizome.models.meta.merchant_plan_merchant_plan_group_v1 import (
    MerchantPlanMerchantPlanGroupV1,
)
from rhizome.models.meta.merchant_plan_v1 import MerchantPlanV1
from rhizome.models.meta.merchant_role_v1 import MerchantRoleV1
from rhizome.models.meta.payment_processor_v1 import PaymentProcessorV1
from rhizome.models.meta.processor_key_v1 import ProcessorKeyV1
from rhizome.models.meta.reseller import Reseller
from rhizome.models.meta.reseller_plan_trial_v1 import ResellerPlanTrialV1
from rhizome.models.meta.server_feature_v1 import ServerFeatureV1
from rhizome.models.meta.terminal_config_merchant_props_v1 import (
    TerminalConfigMerchantPropsV1,
)
from rhizome.models.meta.timezones import Timezones
from rhizome.models.table_list import MetaTable

models: dict[MetaTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    MetaTable.account: (Account, AccountNaProd),
    MetaTable.app_app_bundle: (AppAppBundleV1, AppAppBundleNaProd),
    MetaTable.app_bundle: (AppBundleV1, AppBundleNaProd),
    MetaTable.app_metered: (AppMeteredV1, AppMeteredNaProd),
    MetaTable.app_metered_country: (AppMeteredCountryV1, AppMeteredCountryNaProd),
    MetaTable.app_metered_event: (AppMeteredEventV1, AppMeteredEventNaProd),
    MetaTable.app_permission: (AppPermissionV1, AppPermissionNaProd),
    MetaTable.app_subscription: (AppSubscriptionV1, AppSubscriptionNaProd),
    MetaTable.app_subscription_country: (AppSubscriptionCountryV1, AppSubscriptionCountryNaProd),
    MetaTable.country: (Country, CountryNaProd),
    MetaTable.developer: (Developer, DeveloperNaProd),
    MetaTable.developer_app: (DeveloperAppV1, DeveloperAppNaProd),
    MetaTable.device_events: (DeviceEventsV1, DeviceEventsNaProd),
    MetaTable.device_provision: (DeviceProvisionV1, DeviceProvisionNaProd),
    MetaTable.device_type: (DeviceTypeV1, DeviceTypeNaProd),
    MetaTable.locale: (Locale, LocaleNaProd),
    MetaTable.merchant: (Merchant, MerchantNaProd),
    MetaTable.merchant_address: (MerchantAddressV1, MerchantAddressNaProd),
    MetaTable.merchant_app: (MerchantAppV1, MerchantAppNaProd),
    MetaTable.merchant_app_subscription_history: (
        MerchantAppSubscriptionHistoryV1,
        MerchantAppSubscriptionHistoryNaProd,
    ),
    MetaTable.merchant_boarding: (MerchantBoardingV1, MerchantBoardingNaProd),
    MetaTable.merchant_creation_details: (MerchantCreationDetailsV1, MerchantCreationDetailsNaProd),
    MetaTable.merchant_gateway: (MerchantGatewayV1, MerchantGatewayNaProd),
    MetaTable.merchant_merchant_plan_history: (MerchantMerchantPlanHistoryV1, MerchantMerchantPlanHistoryNaProd),
    MetaTable.merchant_plan: (MerchantPlanV1, MerchantPlanNaProd),
    MetaTable.merchant_plan_group: (MerchantPlanGroupV1, MerchantPlanGroupNaProd),
    MetaTable.merchant_plan_merchant_plan_group: (MerchantPlanMerchantPlanGroupV1, MerchantPlanMerchantPlanGroupNaProd),
    MetaTable.merchant_role: (MerchantRoleV1, MerchantRoleNaProd),
    MetaTable.payment_processor: (PaymentProcessorV1, PaymentProcessorNaProd),
    MetaTable.processor_key: (ProcessorKeyV1, ProcessorKeyNaProd),
    MetaTable.reseller: (Reseller, ResellerNaProd),
    MetaTable.reseller_plan_trial: (ResellerPlanTrialV1, ResellerPlanTrialNaProd),
    MetaTable.server_feature: (ServerFeatureV1, ServerFeatureNaProd),
    MetaTable.terminal_config_merchant_props: (TerminalConfigMerchantPropsV1, TerminalConfigMerchantPropsNaProd),
    MetaTable.timezones: (Timezones, TimezonesNaProd),
}


class NorthAmericaMeta(Environment):
    """North America production meta environment using direct database connection."""

    # Type aliases for environment-specific model versions
    AppAppBundle: type[AppAppBundleV1] = AppAppBundleV1
    AppBundle: type[AppBundleV1] = AppBundleV1
    AppMetered: type[AppMeteredV1] = AppMeteredV1
    AppMeteredCountry: type[AppMeteredCountryV1] = AppMeteredCountryV1
    AppMeteredEvent: type[AppMeteredEventV1] = AppMeteredEventV1
    AppPermission: type[AppPermissionV1] = AppPermissionV1
    AppSubscription: type[AppSubscriptionV1] = AppSubscriptionV1
    AppSubscriptionCountry: type[AppSubscriptionCountryV1] = AppSubscriptionCountryV1
    DeveloperApp: type[DeveloperAppV1] = DeveloperAppV1
    DeviceEvents: type[DeviceEventsV1] = DeviceEventsV1
    DeviceProvision: type[DeviceProvisionV1] = DeviceProvisionV1
    DeviceType: type[DeviceTypeV1] = DeviceTypeV1
    MerchantAddress: type[MerchantAddressV1] = MerchantAddressV1
    MerchantApp: type[MerchantAppV1] = MerchantAppV1
    MerchantBoarding: type[MerchantBoardingV1] = MerchantBoardingV1
    MerchantCreationDetails: type[MerchantCreationDetailsV1] = MerchantCreationDetailsV1
    MerchantGateway: type[MerchantGatewayV1] = MerchantGatewayV1
    MerchantMerchantPlanHistory: type[MerchantMerchantPlanHistoryV1] = MerchantMerchantPlanHistoryV1
    MerchantPlan: type[MerchantPlanV1] = MerchantPlanV1
    MerchantPlanGroup: type[MerchantPlanGroupV1] = MerchantPlanGroupV1
    MerchantPlanMerchantPlanGroup: type[MerchantPlanMerchantPlanGroupV1] = MerchantPlanMerchantPlanGroupV1
    MerchantRole: type[MerchantRoleV1] = MerchantRoleV1
    PaymentProcessor: type[PaymentProcessorV1] = PaymentProcessorV1
    ProcessorKey: type[ProcessorKeyV1] = ProcessorKeyV1
    ResellerPlanTrial: type[ResellerPlanTrialV1] = ResellerPlanTrialV1
    ServerFeature: type[ServerFeatureV1] = ServerFeatureV1
    TerminalConfigMerchantProps: type[TerminalConfigMerchantPropsV1] = TerminalConfigMerchantPropsV1

    def tables(self) -> list[StrEnum]:
        return list(MetaTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        if not isinstance(table_name, MetaTable):
            raise ValueError(f"Expected MetaTable, got {type(table_name)}")
        return models.get(table_name, (None, None))

    @classmethod
    def get_database_config(cls, tools: Tools) -> DatabaseConfig:
        """Get database configuration using pybritive temporary credentials."""
        import asyncio

        # Use the default pattern which handles billing/log/orders variants
        return asyncio.run(
            Environment.get_database_config_from_credentials(
                tools=tools,
                secret_reference="Resources/COS-RO-USProd/COS-RO-USProd-profile",
                secret_manager=SecretManager.PYBRITIVE,
                database_name="meta",
            )
        )

    @classmethod
    def get_port_forward_config(cls) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaMeta"

    @classmethod
    def database_id(cls) -> str:
        """Database identifier for server-side query execution."""
        return "na_prod_meta"

    def get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        from urllib.parse import quote_plus

        db_config = self.get_database_config(self.client.tools)
        encoded_password = quote_plus(db_config.password)
        connection_string = f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}?ssl_verify_cert=false"

        # Log connection details
        mysql_command = (
            f"mysql --user={db_config.username} --password=[REDACTED] --host={db_config.host} "
            f"--port={db_config.port} --batch --skip-ssl-verify-server-cert {db_config.database}"
        )
        self._log_connection_if_new(db_config, mysql_command)

        return connection_string
