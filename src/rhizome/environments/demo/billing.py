"""
Demo Billing environment configuration.

This module provides access to the demo billing database
through direct connection using legacy MySQL credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.table_list import BillingTable

# Declare all billing tables with None mappings - models/emplacements to be added later
models: dict[BillingTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    BillingTable.stage_charge: (None, None),
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


class DemoBilling(Environment):
    """Demo billing environment using direct database connection."""

    def tables(self) -> list[StrEnum]:
        return list(BillingTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        if not isinstance(table_name, BillingTable):
            raise ValueError(f"Expected BillingTable, got {type(table_name)}")
        return models.get(table_name, (None, None))

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using legacy MySQL credentials."""
        import asyncio

        demo_pattern = r"""
            MysqlDevLegacy.*
            password:\s*(?P<password>\S+)
        """

        return asyncio.run(
            self.get_database_config_from_credentials(
                secret_reference="op://Shared/MysqlDevLegacy/password",
                secret_manager=SecretManager.ONEPASSWORD,
                database_name="billing",
                pattern=demo_pattern,
                host="demo2-db01.dev.pdx10.clover.network",
                port=3306,
                username="remotereadonly",
            )
        )

    def get_port_forward_config(self) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DemoBilling"

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