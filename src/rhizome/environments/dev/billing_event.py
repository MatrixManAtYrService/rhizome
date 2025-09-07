"""
Dev Billing Event environment configuration.

This module provides access to the billing-event database in the
dev cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum

from rhizome.environments.database_environment import DatabaseEnvironment
from rhizome.environments.dev.expected_data.billing_event_app_metered_event import AppMeteredEventDev
from rhizome.environments.dev.expected_data.billing_event_app_subscription_event import AppSubscriptionEventDev
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1
from rhizome.models.billing_event.table_list import BillingEventTable

models: dict[BillingEventTable, tuple[type[RhizomeModel], type[Emplacement]]] = {
    BillingEventTable.app_metered_event: (AppMeteredEventV1, AppMeteredEventDev),
    BillingEventTable.app_subscription_event: (None, AppSubscriptionEventDev),  # Model not yet implemented
}


class DevBillingEvent(DatabaseEnvironment):
    """Development billing event environment using CloudSQL."""

    def tables(self) -> list[StrEnum]:
        return list(BillingEventTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement]]:
        if not isinstance(table_name, BillingEventTable):
            raise ValueError(f"Expected BillingEventTable, got {type(table_name)}")
        return models[table_name]

    def get_kube_context(self) -> str:
        """Get Kubernetes context for dev environment."""
        return "gke_clover-dev-kubernetes_us-west1_dev-us-west1-cluster"

    def get_kube_namespace(self) -> str:
        """Get Kubernetes namespace for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_kube_deployment(self) -> str:
        """Get Kubernetes deployment for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_sql_connection(self) -> str:
        """Get CloudSQL connection string."""
        return "clover-dev-managed:us-west1:billing-event"

    def get_database_name(self) -> str:
        """Get database name."""
        return "billing-event-dev"

    def get_username(self) -> str:
        """Get database username."""
        return "billing-event"

    def get_onepassword_reference(self) -> str:
        """Get 1Password reference for credentials."""
        return "op://Shared/EventBillingROCred-dev/password"

    def get_project(self) -> str:
        """Get the Google Cloud project for this environment."""
        return "clover-dev-kubernetes"

    def get_cluster_name(self) -> str:
        """Get the Kubernetes cluster name for this environment."""
        return "dev-us-west1-cluster"

    def get_cluster_region(self) -> str:
        """Get the Kubernetes cluster region for this environment."""
        return "us-west1"

    def get_cluster_server(self) -> str:
        """Get the Kubernetes cluster server for this environment."""
        return "https://dev-us-west1-ingress-nginx.dev.pdx13.clover.network"

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DevBillingEvent"
