"""
NA Production Billing Event environment configuration.

This module provides access to the billing-event database in the
na-prod-us-central1 cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import Enum

from rhizome.environments.database_environment import DatabaseEnvironment
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1


class NorthAmericaBillingEventModel(Enum):
    """Table version mapping for NorthAmericaBillingEvent environment."""
    AppMeteredEvent = AppMeteredEventV1


class NorthAmericaBillingEvent(DatabaseEnvironment):
    """North America production billing event environment using CloudSQL."""

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
        return "clover-prod-databases:us-central1:billing-event"

    def get_database_name(self) -> str:
        """Get database name."""
        return "billing-event-prod"

    def get_username(self) -> str:
        """Get database username."""
        return "billing-event-ro"

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
        return "NorthAmericaBillingEvent"
