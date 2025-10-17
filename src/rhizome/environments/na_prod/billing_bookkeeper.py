"""
NA Production Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
na-prod-us-central1 cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager, Tools
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_billing_entity import BillingEntityNaProd
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_fee_rate import FeeRateNaProd
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_fee_summary import FeeSummaryNaProd
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_invoice_info import InvoiceInfoNaProd
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_settlement import SettlementNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_bookkeeper.billing_entity_v1 import BillingEntityV1
from rhizome.models.billing_bookkeeper.fee_rate_v1 import FeeRateV1
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1
from rhizome.models.billing_bookkeeper.invoice_info_v1 import InvoiceInfoV1
from rhizome.models.billing_bookkeeper.settlement_v1 import SettlementV1
from rhizome.models.table_list import BillingBookkeeperTable

models: dict[BillingBookkeeperTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]]]] = {
    BillingBookkeeperTable.billing_entity: (BillingEntityV1, BillingEntityNaProd),
    BillingBookkeeperTable.fee_rate: (FeeRateV1, FeeRateNaProd),
    BillingBookkeeperTable.fee_summary: (FeeSummaryV1, FeeSummaryNaProd),
    BillingBookkeeperTable.invoice_info: (InvoiceInfoV1, InvoiceInfoNaProd),
    BillingBookkeeperTable.settlement: (SettlementV1, SettlementNaProd),
}


class NorthAmericaBillingBookkeeper(Environment):
    """North America production billing bookkeeper environment using CloudSQL."""

    # Type aliases for environment-specific model versions
    BillingEntity: type[BillingEntityV1] = BillingEntityV1
    FeeRate: type[FeeRateV1] = FeeRateV1
    FeeSummary: type[FeeSummaryV1] = FeeSummaryV1
    InvoiceInfo: type[InvoiceInfoV1] = InvoiceInfoV1
    Settlement: type[SettlementV1] = SettlementV1

    def tables(self) -> list[StrEnum]:
        return list(BillingBookkeeperTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingBookkeeperTable):
            raise ValueError(f"Expected BillingBookkeeperTable, got {type(table_name)}")
        model_class, emplacement_class = models[table_name]
        if model_class is None:
            raise NotImplementedError(f"Model class for {table_name} not yet implemented")
        return model_class, emplacement_class

    @classmethod
    def get_port_forward_config(cls) -> PortForwardConfig:
        """Get port forwarding configuration for NA production environment."""
        return PortForwardConfig(
            project="clover-prod-kubernetes",
            cluster="na-prod-us-central1-cluster",
            region="us-central1",
            server="https://na-prod-ingress-nginx.prod.dsm06.clover.network",
            kube_context="gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster",
            kube_namespace="gke-cloudsql-access",
            kube_deployment="gke-cloudsql-access",
            sql_connection="clover-prod-databases:us-central1:billing-bookkeeper",
            database_name="billing-bookkeeper-prod",
            username="billing-bookkeeper-ro",
            secret_reference="op://Shared/EventBillingROCred/password",
            secret_manager=SecretManager.ONEPASSWORD,
        )

    @classmethod
    def get_database_config(cls, tools: Tools) -> DatabaseConfig:
        """Get database configuration using port forwarding credentials."""
        import asyncio

        # Get the port forward config to access secret reference
        pf_config = cls.get_port_forward_config()

        # Retrieve password directly without needing port forwarding setup
        password = asyncio.run(Environment.get_secret(tools, pf_config.secret_reference, pf_config.secret_manager))

        # Return config with placeholder port (actual port assigned during __init__)
        return DatabaseConfig(
            host="127.0.0.1",  # Port forwarding always uses localhost
            port=0,  # Placeholder - actual port set during instance initialization
            database=pf_config.database_name,
            username=pf_config.username,
            password=password,
        )

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBillingBookkeeper"

    @classmethod
    def database_id(cls) -> str:
        """Database identifier for server-side query execution."""
        return "na_prod_billing_bookkeeper"

    def get_connection_string(self) -> str:
        """Build the connection string for this port-forwarded environment."""
        from urllib.parse import quote_plus

        # Get the config with credentials
        db_config = self.get_database_config(self.client.tools)

        # Use the actual local port that was set up during __init__
        encoded_password = quote_plus(db_config.password)
        connection_string = f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{self.local_port}/{db_config.database}"

        # Log connection details
        mysql_command = (
            f"mysql --user={db_config.username} --password=[REDACTED] --host={db_config.host} "
            f"--port={self.local_port} --batch {db_config.database}"
        )
        self._log_connection_if_new(
            DatabaseConfig(
                host=db_config.host,
                port=self.local_port,
                database=db_config.database,
                username=db_config.username,
                password=db_config.password,
            ),
            mysql_command,
        )

        return connection_string
