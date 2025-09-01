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
        # Note: This would need to be updated with actual demo cluster context
        return "gke_clover-demo-kubernetes_us-central1_demo-cluster"

    def get_kube_namespace(self) -> str:
        """Get Kubernetes namespace for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_kube_deployment(self) -> str:
        """Get Kubernetes deployment for CloudSQL access."""
        return "gke-cloudsql-access"

    def get_sql_connection(self) -> str:
        """Get CloudSQL connection string."""
        # Note: This would need to be updated with actual demo connection
        return "clover-demo-databases:us-central1:billing-event"

    def get_database_name(self) -> str:
        """Get database name."""
        return "billing-event-demo"

    def get_username(self) -> str:
        """Get database username."""
        return "billing-event"

    def get_onepassword_reference(self) -> str:
        """Get 1Password reference for credentials."""
        # Note: This would need to be updated with actual demo credentials
        return "op://Shared/EventBillingROCred-demo/password"

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DemoBillingEvent"