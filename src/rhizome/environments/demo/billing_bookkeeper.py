"""
Demo Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
demo cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_entity import BillingEntityDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_rate import FeeRateDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_summary import FeeSummaryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_info import InvoiceInfoDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_settlement import SettlementDemo
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_bookkeeper.billing_entity_v1 import BillingEntityV1
from rhizome.models.billing_bookkeeper.fee_rate_v1 import FeeRateV1
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1
from rhizome.models.billing_bookkeeper.invoice_info_v1 import InvoiceInfoV1
from rhizome.models.billing_bookkeeper.settlement_v1 import SettlementV1
from rhizome.models.table_list import BillingBookkeeperTable

models: dict[BillingBookkeeperTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]]]] = {
    BillingBookkeeperTable.billing_entity: (BillingEntityV1, BillingEntityDemo),
    BillingBookkeeperTable.fee_rate: (FeeRateV1, FeeRateDemo),
    BillingBookkeeperTable.fee_summary: (FeeSummaryV1, FeeSummaryDemo),
    BillingBookkeeperTable.invoice_info: (InvoiceInfoV1, InvoiceInfoDemo),
    BillingBookkeeperTable.settlement: (SettlementV1, SettlementDemo),
}


class DemoBillingBookkeeper(Environment):
    """Demo bookkeeper environment using CloudSQL."""

    def tables(self) -> list[StrEnum]:
        return list(BillingBookkeeperTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingBookkeeperTable):
            raise ValueError(f"Expected BillingBookkeeperTable, got {type(table_name)}")
        model_class, emplacement_class = models[table_name]
        if model_class is None:
            raise NotImplementedError(f"Model class for {table_name} not yet implemented")
        return model_class, emplacement_class

    def get_port_forward_config(self) -> PortForwardConfig:
        """Get port forwarding configuration for demo environment."""
        return PortForwardConfig(
            project="clover-dev-kubernetes",
            cluster="dev-us-west1-cluster",
            region="us-west1",
            server="https://dev-us-west1-ingress-nginx.dev.pdx13.clover.network",
            kube_context="gke_clover-dev-kubernetes_us-west1_dev-us-west1-cluster",
            kube_namespace="gke-cloudsql-access",
            kube_deployment="gke-cloudsql-access",
            sql_connection="clover-dev-managed:us-west1:billing-bookkeeper-demo2",
            database_name="billing-bookkeeper-dev",
            username="billing-bookkeeper",
            secret_reference="op://Shared/EventBillingROCred-dev/password",
            secret_manager=SecretManager.ONEPASSWORD,
        )

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using port forwarding."""
        port_forward_config = self.get_port_forward_config()
        return self.get_database_config_from_port_forward(port_forward_config)

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DemoBillingBookkeeper"
