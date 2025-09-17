"""
NA Production Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
na-prod-us-central1 cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_fee_summary import FeeSummaryNaProd
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_settlement import SettlementNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1
from rhizome.models.billing_bookkeeper.settlement_v1 import SettlementV1
from rhizome.models.table_list import BillingBookkeeperTable

models: dict[BillingBookkeeperTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]]]] = {
    BillingBookkeeperTable.fee_summary: (FeeSummaryV1, FeeSummaryNaProd),
    BillingBookkeeperTable.settlement: (SettlementV1, SettlementNaProd),
}


class NorthAmericaBillingBookkeeper(Environment):
    """North America production billing bookkeeper environment using CloudSQL."""

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

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using port forwarding."""
        port_forward_config = self.get_port_forward_config()
        return self.get_database_config_from_port_forward(port_forward_config)

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBillingBookkeeper"
