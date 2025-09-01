"""
Demo Billing Event environment configuration.

This module provides access to the billing-event database in the
demo cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from rhizome.environments.database_environment import DatabaseEnvironment


class DemoBillingEvent(DatabaseEnvironment):
    """Demo billing event environment using CloudSQL."""

    def get_kube_context(self) -> str:
        """Get Kubernetes context for demo environment."""
        return "gke_clover-dev-kubernetes_us-west1_dev-us-west1-cluster"

    def get_kube_namespace(self) -> str:
        """Get Kubernetes namespace for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_kube_deployment(self) -> str:
        """Get Kubernetes deployment for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_sql_connection(self) -> str:
        """Get CloudSQL connection string."""
        return "clover-dev-managed:us-west1:billing-event-demo"

    def get_database_name(self) -> str:
        """Get database name."""
        return "billing-event-demo"

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
        return "DemoBillingEvent"
