"""
Dev Billing Event environment configuration.

This module provides access to the billing-event database in the
dev cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from rhizome.environments.database_environment import DatabaseEnvironment


class DevBillingEvent(DatabaseEnvironment):
    """Development billing event environment using CloudSQL."""

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

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DevBillingEvent"