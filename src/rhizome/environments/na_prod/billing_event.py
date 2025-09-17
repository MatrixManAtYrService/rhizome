"""
NA Production Billing Event environment configuration.

This module provides access to the billing-event database in the
na-prod-us-central1 cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.na_prod.expected_data.billing_event_app_metered_event import AppMeteredEventNaProd
from rhizome.environments.na_prod.expected_data.billing_event_app_subscription_event import AppSubscriptionEventNaProd
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1
from rhizome.models.billing_event.app_subscription_event_v1 import AppSubscriptionEventV1
from rhizome.models.table_list import BillingEventTable

models: dict[BillingEventTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]]]] = {
    BillingEventTable.app_metered_event: (AppMeteredEventV1, AppMeteredEventNaProd),
    BillingEventTable.app_subscription_event: (AppSubscriptionEventV1, AppSubscriptionEventNaProd),
}


class NorthAmericaBillingEvent(Environment):
    """North America production billing event environment using CloudSQL."""

    def tables(self) -> list[StrEnum]:
        return list(BillingEventTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingEventTable):
            raise ValueError(f"Expected BillingEventTable, got {type(table_name)}")
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
            sql_connection="clover-prod-databases:us-central1:billing-event",
            database_name="billing-event-prod",
            username="billing-event-ro",
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
        return "NorthAmericaBillingEvent"
