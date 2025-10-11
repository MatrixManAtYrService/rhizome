"""
Development Meta environment configuration.

This module provides access to the development meta database
through direct connection using legacy MySQL credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import (
    DatabaseConfig,
    DatabaseConfigWithRW,
    Environment,
    PortForwardConfig,
    SecretManager,
)
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
from .expected_data.meta_account import AccountDev
from .expected_data.meta_app_app_bundle import AppAppBundleDev
from .expected_data.meta_app_bundle import AppBundleDev
from .expected_data.meta_app_metered import AppMeteredDev
from .expected_data.meta_app_metered_country import AppMeteredCountryDev
from .expected_data.meta_app_metered_event import AppMeteredEventDev
from .expected_data.meta_app_permission import AppPermissionDev
from .expected_data.meta_app_subscription import AppSubscriptionDev
from .expected_data.meta_app_subscription_country import AppSubscriptionCountryDev
from .expected_data.meta_country import CountryDev
from .expected_data.meta_developer import DeveloperDev
from .expected_data.meta_developer_app import DeveloperAppDev
from .expected_data.meta_device_events import DeviceEventsDev
from .expected_data.meta_device_provision import DeviceProvisionDev
from .expected_data.meta_device_type import DeviceTypeDev
from .expected_data.meta_locale import LocaleDev
from .expected_data.meta_merchant import MerchantDev
from .expected_data.meta_merchant_address import MerchantAddressDev
from .expected_data.meta_merchant_app import MerchantAppDev
from .expected_data.meta_merchant_app_subscription_history import MerchantAppSubscriptionHistoryDev
from .expected_data.meta_merchant_boarding import MerchantBoardingDev
from .expected_data.meta_merchant_creation_details import MerchantCreationDetailsDev
from .expected_data.meta_merchant_gateway import MerchantGatewayDev
from .expected_data.meta_merchant_merchant_plan_history import MerchantMerchantPlanHistoryDev
from .expected_data.meta_merchant_plan import MerchantPlanDev
from .expected_data.meta_merchant_plan_group import MerchantPlanGroupDev
from .expected_data.meta_merchant_plan_merchant_plan_group import MerchantPlanMerchantPlanGroupDev
from .expected_data.meta_merchant_role import MerchantRoleDev
from .expected_data.meta_payment_processor import PaymentProcessorDev
from .expected_data.meta_processor_key import ProcessorKeyDev
from .expected_data.meta_reseller import ResellerDev
from .expected_data.meta_reseller_permissions import ResellerPermissionsDev
from .expected_data.meta_reseller_plan_trial import ResellerPlanTrialDev
from .expected_data.meta_reseller_role import ResellerRoleDev
from .expected_data.meta_server_feature import ServerFeatureDev
from .expected_data.meta_terminal_config_merchant_props import TerminalConfigMerchantPropsDev
from .expected_data.meta_timezones import TimezonesDev

# Register all meta table models with their emplacements (JSON data to be generated via 'rhizome sync data')
models: dict[MetaTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    MetaTable.account: (Account, AccountDev),
    MetaTable.country: (Country, CountryDev),
    MetaTable.device_type: (DeviceTypeV1, DeviceTypeDev),
    MetaTable.server_feature: (ServerFeatureV1, ServerFeatureDev),
    MetaTable.merchant: (Merchant, MerchantDev),
    MetaTable.terminal_config_merchant_props: (TerminalConfigMerchantPropsV1, TerminalConfigMerchantPropsDev),
    MetaTable.reseller: (Reseller, ResellerDev),
    MetaTable.reseller_permissions: (ResellerPermissionsV1, ResellerPermissionsDev),
    MetaTable.reseller_role: (ResellerRoleV1, ResellerRoleDev),
    MetaTable.merchant_address: (MerchantAddressV1, MerchantAddressDev),
    MetaTable.merchant_gateway: (MerchantGatewayV1, MerchantGatewayDev),
    MetaTable.payment_processor: (PaymentProcessorV1, PaymentProcessorDev),
    MetaTable.processor_key: (ProcessorKeyV1, ProcessorKeyDev),
    MetaTable.merchant_plan: (MerchantPlanV1, MerchantPlanDev),
    MetaTable.merchant_plan_group: (MerchantPlanGroupV1, MerchantPlanGroupDev),
    MetaTable.merchant_plan_merchant_plan_group: (MerchantPlanMerchantPlanGroupV1, MerchantPlanMerchantPlanGroupDev),
    MetaTable.merchant_role: (MerchantRoleV1, MerchantRoleDev),
    MetaTable.developer: (Developer, DeveloperDev),
    MetaTable.locale: (Locale, LocaleDev),
    MetaTable.timezones: (Timezones, TimezonesDev),
    MetaTable.app_app_bundle: (AppAppBundleV1, AppAppBundleDev),
    MetaTable.app_bundle: (AppBundleV1, AppBundleDev),
    MetaTable.app_metered: (AppMeteredV1, AppMeteredDev),
    MetaTable.app_metered_country: (AppMeteredCountryV1, AppMeteredCountryDev),
    MetaTable.app_metered_event: (AppMeteredEventV1, AppMeteredEventDev),
    MetaTable.app_permission: (AppPermissionV1, AppPermissionDev),
    MetaTable.app_subscription: (AppSubscriptionV1, AppSubscriptionDev),
    MetaTable.app_subscription_country: (AppSubscriptionCountryV1, AppSubscriptionCountryDev),
    MetaTable.developer_app: (DeveloperAppV1, DeveloperAppDev),
    MetaTable.device_events: (DeviceEventsV1, DeviceEventsDev),
    MetaTable.device_provision: (DeviceProvisionV1, DeviceProvisionDev),
    MetaTable.merchant_app: (MerchantAppV1, MerchantAppDev),
    MetaTable.merchant_app_subscription_history: (MerchantAppSubscriptionHistoryV1, MerchantAppSubscriptionHistoryDev),
    MetaTable.merchant_boarding: (MerchantBoardingV1, MerchantBoardingDev),
    MetaTable.merchant_creation_details: (MerchantCreationDetailsV1, MerchantCreationDetailsDev),
    MetaTable.merchant_merchant_plan_history: (MerchantMerchantPlanHistoryV1, MerchantMerchantPlanHistoryDev),
    MetaTable.reseller_plan_trial: (ResellerPlanTrialV1, ResellerPlanTrialDev),
}


class DevMeta(Environment):
    """Development meta environment using direct database connection."""

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

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using legacy MySQL credentials (read-only)."""
        import asyncio

        password = asyncio.run(self._get_secret("op://Shared/MysqlDevLegacy/password", SecretManager.ONEPASSWORD))

        return DatabaseConfig(
            host="dev1-db01.dev.pdx10.clover.network",
            port=3306,
            database="meta",
            username="remotereadonly",
            password=password,
        )

    def get_database_config_rw(self) -> DatabaseConfigWithRW | None:
        """Get database configuration with both RO and RW credentials."""
        import asyncio

        ro_password = asyncio.run(self._get_secret("op://Shared/MysqlDevLegacy/password", SecretManager.ONEPASSWORD))
        rw_password = asyncio.run(self._get_secret("op://Shared/DevMetaRW/password", SecretManager.ONEPASSWORD))

        return DatabaseConfigWithRW(
            host="dev1-db01.dev.pdx10.clover.network",
            port=3306,
            database="meta",
            ro_username="remotereadonly",
            ro_password=ro_password,
            rw_username="superuser",
            rw_password=rw_password,
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DevMeta"

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
