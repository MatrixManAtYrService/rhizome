"""
Demo Meta environment configuration.

This module provides access to the demo meta database
through direct connection using legacy MySQL credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager, Tools
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
from rhizome.models.meta.merchant_app_subscription_history_v1 import MerchantAppSubscriptionHistoryV1
from rhizome.models.meta.merchant_app_v1 import MerchantAppV1
from rhizome.models.meta.merchant_boarding_v1 import MerchantBoardingV1
from rhizome.models.meta.merchant_creation_details_v1 import MerchantCreationDetailsV1
from rhizome.models.meta.merchant_gateway_v1 import MerchantGatewayV1
from rhizome.models.meta.merchant_merchant_plan_history_v1 import MerchantMerchantPlanHistoryV1
from rhizome.models.meta.merchant_plan_group_v1 import MerchantPlanGroupV1
from rhizome.models.meta.merchant_plan_merchant_plan_group_v1 import MerchantPlanMerchantPlanGroupV1
from rhizome.models.meta.merchant_plan_v1 import MerchantPlanV1
from rhizome.models.meta.merchant_role_v1 import MerchantRoleV1
from rhizome.models.meta.payment_processor_v1 import PaymentProcessorV1
from rhizome.models.meta.processor_key_v1 import ProcessorKeyV1
from rhizome.models.meta.reseller import Reseller
from rhizome.models.meta.reseller_permissions_v1 import ResellerPermissionsV1
from rhizome.models.meta.reseller_plan_trial_v1 import ResellerPlanTrialV1
from rhizome.models.meta.reseller_role_v1 import ResellerRoleV1
from rhizome.models.meta.server_feature_v1 import ServerFeatureV1
from rhizome.models.meta.terminal_config_merchant_props_v1 import TerminalConfigMerchantPropsV1
from rhizome.models.meta.timezones import Timezones
from rhizome.models.table_list import MetaTable

# Import emplacements
from .expected_data.meta_account import AccountDemo
from .expected_data.meta_app_app_bundle import AppAppBundleDemo
from .expected_data.meta_app_bundle import AppBundleDemo
from .expected_data.meta_app_metered import AppMeteredDemo
from .expected_data.meta_app_metered_country import AppMeteredCountryDemo
from .expected_data.meta_app_metered_event import AppMeteredEventDemo
from .expected_data.meta_app_permission import AppPermissionDemo
from .expected_data.meta_app_subscription import AppSubscriptionDemo
from .expected_data.meta_app_subscription_country import AppSubscriptionCountryDemo
from .expected_data.meta_country import CountryDemo
from .expected_data.meta_developer import DeveloperDemo
from .expected_data.meta_developer_app import DeveloperAppDemo
from .expected_data.meta_device_events import DeviceEventsDemo
from .expected_data.meta_device_provision import DeviceProvisionDemo
from .expected_data.meta_device_type import DeviceTypeDemo
from .expected_data.meta_locale import LocaleDemo
from .expected_data.meta_merchant import MerchantDemo
from .expected_data.meta_merchant_address import MerchantAddressDemo
from .expected_data.meta_merchant_app import MerchantAppDemo
from .expected_data.meta_merchant_app_subscription_history import MerchantAppSubscriptionHistoryDemo
from .expected_data.meta_merchant_boarding import MerchantBoardingDemo
from .expected_data.meta_merchant_creation_details import MerchantCreationDetailsDemo
from .expected_data.meta_merchant_gateway import MerchantGatewayDemo
from .expected_data.meta_merchant_merchant_plan_history import MerchantMerchantPlanHistoryDemo
from .expected_data.meta_merchant_plan import MerchantPlanDemo
from .expected_data.meta_merchant_plan_group import MerchantPlanGroupDemo
from .expected_data.meta_merchant_plan_merchant_plan_group import MerchantPlanMerchantPlanGroupDemo
from .expected_data.meta_merchant_role import MerchantRoleDemo
from .expected_data.meta_payment_processor import PaymentProcessorDemo
from .expected_data.meta_processor_key import ProcessorKeyDemo
from .expected_data.meta_reseller import ResellerDemo
from .expected_data.meta_reseller_permissions import ResellerPermissionsDemo
from .expected_data.meta_reseller_plan_trial import ResellerPlanTrialDemo
from .expected_data.meta_reseller_role import ResellerRoleDemo
from .expected_data.meta_server_feature import ServerFeatureDemo
from .expected_data.meta_terminal_config_merchant_props import TerminalConfigMerchantPropsDemo
from .expected_data.meta_timezones import TimezonesDemo

# Register all meta table models with their emplacements (JSON data files to be generated via 'rhizome sync data')
models: dict[MetaTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    MetaTable.account: (Account, AccountDemo),
    MetaTable.country: (Country, CountryDemo),
    MetaTable.device_type: (DeviceTypeV1, DeviceTypeDemo),
    MetaTable.server_feature: (ServerFeatureV1, ServerFeatureDemo),
    MetaTable.merchant: (Merchant, MerchantDemo),
    MetaTable.terminal_config_merchant_props: (TerminalConfigMerchantPropsV1, TerminalConfigMerchantPropsDemo),
    MetaTable.reseller: (Reseller, ResellerDemo),
    MetaTable.reseller_permissions: (ResellerPermissionsV1, ResellerPermissionsDemo),
    MetaTable.reseller_role: (ResellerRoleV1, ResellerRoleDemo),
    MetaTable.merchant_address: (MerchantAddressV1, MerchantAddressDemo),
    MetaTable.merchant_gateway: (MerchantGatewayV1, MerchantGatewayDemo),
    MetaTable.payment_processor: (PaymentProcessorV1, PaymentProcessorDemo),
    MetaTable.processor_key: (ProcessorKeyV1, ProcessorKeyDemo),
    MetaTable.merchant_plan: (MerchantPlanV1, MerchantPlanDemo),
    MetaTable.merchant_plan_group: (MerchantPlanGroupV1, MerchantPlanGroupDemo),
    MetaTable.merchant_plan_merchant_plan_group: (MerchantPlanMerchantPlanGroupV1, MerchantPlanMerchantPlanGroupDemo),
    MetaTable.merchant_role: (MerchantRoleV1, MerchantRoleDemo),
    MetaTable.developer: (Developer, DeveloperDemo),
    MetaTable.locale: (Locale, LocaleDemo),
    MetaTable.timezones: (Timezones, TimezonesDemo),
    MetaTable.app_app_bundle: (AppAppBundleV1, AppAppBundleDemo),
    MetaTable.app_bundle: (AppBundleV1, AppBundleDemo),
    MetaTable.app_metered: (AppMeteredV1, AppMeteredDemo),
    MetaTable.app_metered_country: (AppMeteredCountryV1, AppMeteredCountryDemo),
    MetaTable.app_metered_event: (AppMeteredEventV1, AppMeteredEventDemo),
    MetaTable.app_permission: (AppPermissionV1, AppPermissionDemo),
    MetaTable.app_subscription: (AppSubscriptionV1, AppSubscriptionDemo),
    MetaTable.app_subscription_country: (AppSubscriptionCountryV1, AppSubscriptionCountryDemo),
    MetaTable.developer_app: (DeveloperAppV1, DeveloperAppDemo),
    MetaTable.device_events: (DeviceEventsV1, DeviceEventsDemo),
    MetaTable.device_provision: (DeviceProvisionV1, DeviceProvisionDemo),
    MetaTable.merchant_app: (MerchantAppV1, MerchantAppDemo),
    MetaTable.merchant_app_subscription_history: (MerchantAppSubscriptionHistoryV1, MerchantAppSubscriptionHistoryDemo),
    MetaTable.merchant_boarding: (MerchantBoardingV1, MerchantBoardingDemo),
    MetaTable.merchant_creation_details: (MerchantCreationDetailsV1, MerchantCreationDetailsDemo),
    MetaTable.merchant_merchant_plan_history: (MerchantMerchantPlanHistoryV1, MerchantMerchantPlanHistoryDemo),
    MetaTable.reseller_plan_trial: (ResellerPlanTrialV1, ResellerPlanTrialDemo),
}


class DemoMeta(Environment):
    """Demo meta environment using direct database connection."""

    # Type aliases for environment-specific model versions
    DeviceType: type[DeviceTypeV1] = DeviceTypeV1
    ServerFeature: type[ServerFeatureV1] = ServerFeatureV1
    ResellerPermissions: type[ResellerPermissionsV1] = ResellerPermissionsV1
    ResellerRole: type[ResellerRoleV1] = ResellerRoleV1
    TerminalConfigMerchantProps: type[TerminalConfigMerchantPropsV1] = TerminalConfigMerchantPropsV1
    MerchantAddress: type[MerchantAddressV1] = MerchantAddressV1
    MerchantGateway: type[MerchantGatewayV1] = MerchantGatewayV1
    PaymentProcessor: type[PaymentProcessorV1] = PaymentProcessorV1
    ProcessorKey: type[ProcessorKeyV1] = ProcessorKeyV1
    MerchantPlan: type[MerchantPlanV1] = MerchantPlanV1
    MerchantPlanGroup: type[MerchantPlanGroupV1] = MerchantPlanGroupV1
    MerchantPlanMerchantPlanGroup: type[MerchantPlanMerchantPlanGroupV1] = MerchantPlanMerchantPlanGroupV1
    MerchantRole: type[MerchantRoleV1] = MerchantRoleV1
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
    MerchantApp: type[MerchantAppV1] = MerchantAppV1
    MerchantAppSubscriptionHistory: type[MerchantAppSubscriptionHistoryV1] = MerchantAppSubscriptionHistoryV1
    MerchantBoarding: type[MerchantBoardingV1] = MerchantBoardingV1
    MerchantCreationDetails: type[MerchantCreationDetailsV1] = MerchantCreationDetailsV1
    MerchantMerchantPlanHistory: type[MerchantMerchantPlanHistoryV1] = MerchantMerchantPlanHistoryV1
    ResellerPlanTrial: type[ResellerPlanTrialV1] = ResellerPlanTrialV1

    def tables(self) -> list[StrEnum]:
        return list(MetaTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        if not isinstance(table_name, MetaTable):
            raise ValueError(f"Expected MetaTable, got {type(table_name)}")
        return models.get(table_name, (None, None))

    @classmethod
    def get_database_config(cls, tools: Tools) -> DatabaseConfig:
        """Get database configuration using legacy MySQL credentials."""
        import asyncio

        password = asyncio.run(
            Environment.get_secret(tools, "op://Shared/MysqlDevLegacy/password", SecretManager.ONEPASSWORD)
        )

        return DatabaseConfig(
            host="demo2-db01.dev.pdx10.clover.network",
            port=3306,
            database="meta",
            username="remotereadonly",
            password=password,
        )

    @classmethod
    def get_port_forward_config(cls) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DemoMeta"

    @classmethod
    def database_id(cls) -> str:
        """Database identifier for server-side query execution."""
        return "demo_meta"

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
