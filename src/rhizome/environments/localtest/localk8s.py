"""
Local Kubernetes environment configuration.

This module provides access to local Kind cluster with MySQL for testing database
functionality. It uses the local test environment described in local_test.md.
"""

from __future__ import annotations

from rhizome.client import Handle, RhizomeClient


def get_handle(client: RhizomeClient | None = None, local_port: int = 3306, delay: float = 2.0) -> Handle:
    """
    Get a handle for a local Kubernetes MySQL database connection.

    This function requests a port forward to the local Kind cluster MySQL instance
    and waits for credentials via Server-Sent Events. The function only returns
    once the port forward is established and credentials are provided.

    Args:
        client: RhizomeClient instance to use (if None, creates a new one)
        local_port: Local port to forward to (default: 3306)
        delay: Delay before server provides credentials (for testing timing)

    Returns:
        Handle: Connection handle with MySQL connection string including credentials
    """
    if client is None:
        client = RhizomeClient(data_in_logs=False)

    # Request port forward to local Kind cluster MySQL with SSE credential waiting
    return client.request_localk8s(
        kube_context="kind-rhizome-test",
        kube_namespace="default",
        kube_deployment="mysql",  # Pod name in the Kind cluster
        local_port=local_port,
        delay=delay,
    )
