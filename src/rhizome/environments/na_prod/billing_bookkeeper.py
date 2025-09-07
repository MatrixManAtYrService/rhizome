"""
NA Production Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
na-prod-us-central1 cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum

from rhizome.environments.database_environment import DatabaseEnvironment
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_fee_summary import FeeSummaryNaProd
from rhizome.environments.na_prod.expected_data.billing_bookkeeper_settlement import SettlementNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1
from rhizome.models.billing_bookkeeper.table_list import BillingBookkeeperTable

models: dict[BillingBookkeeperTable, tuple[type[RhizomeModel], type[Emplacement]]] = {
    BillingBookkeeperTable.fee_summary: (FeeSummaryV1, FeeSummaryNaProd),
    BillingBookkeeperTable.settlement: (None, SettlementNaProd),  # Model not yet implemented
}


class NorthAmericaBillingBookkeeper(DatabaseEnvironment):
    """North America production billing bookkeeper environment using CloudSQL."""

    def tables(self) -> list[StrEnum]:
        return list(BillingBookkeeperTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement]]:
        if not isinstance(table_name, BillingBookkeeperTable):
            raise ValueError(f"Expected BillingBookkeeperTable, got {type(table_name)}")
        return models[table_name]

    def get_kube_context(self) -> str:
        """Get Kubernetes context for NA production."""
        return "gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster"

    def get_kube_namespace(self) -> str:
        """Get Kubernetes namespace for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_kube_deployment(self) -> str:
        """Get Kubernetes deployment for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_sql_connection(self) -> str:
        """Get CloudSQL connection string."""
        return "clover-prod-databases:us-central1:billing-bookkeeper"

    def get_database_name(self) -> str:
        """Get database name."""
        return "billing-bookkeeper-prod"

    def get_username(self) -> str:
        """Get database username."""
        return "billing-bookkeeper-ro"

    def get_onepassword_reference(self) -> str:
        """Get 1Password reference for credentials."""
        return "op://Shared/EventBillingROCred/password"

    def get_project(self) -> str:
        """Get the Google Cloud project for this environment."""
        return "clover-prod-kubernetes"

    def get_cluster_name(self) -> str:
        """Get the Kubernetes cluster name for this environment."""
        return "na-prod-us-central1-cluster"

    def get_cluster_region(self) -> str:
        """Get the Kubernetes cluster region for this environment."""
        return "us-central1"

    def get_cluster_server(self) -> str:
        """Get the Kubernetes cluster server for this environment."""
        return "https://na-prod-ingress-nginx.prod.dsm06.clover.network"

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBillingBookkeeper"
