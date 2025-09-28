"""
North America Production Billing environment configuration.

This module provides access to the North America production billing database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.na_prod.expected_data.billing_stage_charge import StageChargeNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing.stage_charge_v1 import StageChargeV1
from rhizome.models.table_list import BillingTable

models: dict[BillingTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    BillingTable.stage_charge: (StageChargeV1, StageChargeNaProd),
    # All other tables are not yet implemented
    BillingTable.app_suppression: (None, None),
    BillingTable.auto_debit_no_auth_config: (None, None),
    BillingTable.bank_routing: (None, None),
    BillingTable.banner_curb: (None, None),
    BillingTable.banner_data: (None, None),
    BillingTable.banner_details: (None, None),
    BillingTable.bi_context: (None, None),
    BillingTable.biie_config: (None, None),
    BillingTable.biie_file_def: (None, None),
    BillingTable.biie_file_instance: (None, None),
    BillingTable.biie_file_instance_request: (None, None),
    BillingTable.biie_file_staging_data: (None, None),
    BillingTable.billing_business_initiative: (None, None),
    BillingTable.billing_request: (None, None),
    BillingTable.billing_request_state: (None, None),
    BillingTable.charge_capture_error: (None, None),
    BillingTable.charge_invoice_number: (None, None),
    BillingTable.charge_metrics: (None, None),
    BillingTable.charge_post_date: (None, None),
    BillingTable.charge_state_attempt: (None, None),
    BillingTable.combined_charge: (None, None),
    BillingTable.combined_charge_tree: (None, None),
    BillingTable.combined_disbursement: (None, None),
    BillingTable.combined_disbursement_tree: (None, None),
    BillingTable.corollary_data: (None, None),
    BillingTable.country_suppression: (None, None),
    BillingTable.device_order_tracking: (None, None),
    BillingTable.disbursement_invoice_number: (None, None),
    BillingTable.email_audit: (None, None),
    BillingTable.email_developer_charge: (None, None),
    BillingTable.explanation: (None, None),
    BillingTable.explanation_data: (None, None),
    BillingTable.export_tracker: (None, None),
    BillingTable.fee: (None, None),
    BillingTable.fee_exception: (None, None),
    BillingTable.flight_check: (None, None),
    BillingTable.flight_check_archive: (None, None),
    BillingTable.flight_check_execution: (None, None),
    BillingTable.heartbeat: (None, None),
    BillingTable.invoice_charge: (None, None),
    BillingTable.job_lock: (None, None),
    BillingTable.merchant_device_info: (None, None),
    BillingTable.merchant_odessa_mapping: (None, None),
    BillingTable.merchant_queue_sensitive: (None, None),
    BillingTable.merchant_subscription_action: (None, None),
    BillingTable.merchant_suppression: (None, None),
    BillingTable.merchant_suppression_by_app: (None, None),
    BillingTable.merchant_terms_acceptance: (None, None),
    BillingTable.merchant_terms_acceptance_events: (None, None),
    BillingTable.merchant_terms_acceptance_failed_event_log: (None, None),
    BillingTable.merchant_terms_missing_acceptance: (None, None),
    BillingTable.offboarding: (None, None),
    BillingTable.plan_authorization_settings: (None, None),
    BillingTable.plan_meta: (None, None),
    BillingTable.plan_meta_history: (None, None),
    BillingTable.producer_failure: (None, None),
    BillingTable.promo: (None, None),
    BillingTable.promo_control: (None, None),
    BillingTable.remit_merchant_details: (None, None),
    BillingTable.reseller_app_rev_share: (None, None),
    BillingTable.reseller_invoice_alliance: (None, None),
    BillingTable.reseller_plan_fee: (None, None),
    BillingTable.reseller_plan_rev_share: (None, None),
    BillingTable.reseller_suppression: (None, None),
    BillingTable.reseller_usage_job_config: (None, None),
    BillingTable.rev_share: (None, None),
    BillingTable.seasonal_merchant_trans_audit: (None, None),
    BillingTable.seasonal_reseller_info: (None, None),
    BillingTable.server_config: (None, None),
    BillingTable.stage_app_metered_event: (None, None),
    BillingTable.stage_charge_capture_error: (None, None),
    BillingTable.stage_charge_history: (None, None),
    BillingTable.stage_charge_state_attempt: (None, None),
    BillingTable.stage_charge_update: (None, None),
    BillingTable.stage_email: (None, None),
    BillingTable.stage_email_merchant_charge: (None, None),
    BillingTable.stage_infolease_charge_attempt: (None, None),
    BillingTable.stage_infolease_disbursement_attempt: (None, None),
    BillingTable.stage_merchant_app_charge: (None, None),
    BillingTable.stage_merchant_plan_charge: (None, None),
    BillingTable.stage_vendor_disbursement_error: (None, None),
    BillingTable.stage_vendor_disbursement_state_attempt: (None, None),
    BillingTable.stop_ach_history: (None, None),
    BillingTable.suppression_metrics: (None, None),
    BillingTable.vat_vendor_disbursement: (None, None),
    BillingTable.vendor_disbursement_error: (None, None),
    BillingTable.vendor_disbursement_state_attempt: (None, None),
}


class NorthAmericaBilling(Environment):
    """North America production billing environment using direct database connection."""

    def tables(self) -> list[StrEnum]:
        return list(BillingTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingTable):
            raise ValueError(f"Expected BillingTable, got {type(table_name)}")
        model_class, emplacement_class = models[table_name]
        if model_class is None:
            raise NotImplementedError(f"Model class for {table_name} not yet implemented")
        return model_class, emplacement_class

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using pybritive temporary credentials."""
        import asyncio

        # This pattern is now the default in the tool, but we pass it for clarity.
        billing_pattern = r"""
            Temp\sMySQL\susername:\s*(?P<username>\S+).*
            Temp\spassword:\s*(?P<password>\S+).*
            For\sbilling\sin\susprod\sconnect\sto\sserver:\s*(?P<host>[^:]+):(?P<port>\d+)
        """

        # Use the new generic credential system
        return asyncio.run(
            self.get_database_config_from_credentials(
                secret_reference="Resources/COS-RO-USProd/COS-RO-USProd-profile",
                secret_manager=SecretManager.PYBRITIVE,
                database_name="billing",
                pattern=billing_pattern,
            )
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBilling"

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
