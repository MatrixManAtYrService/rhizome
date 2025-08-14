"""
NA Production Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the 
na-prod-us-central1 cluster through kubectl port-forward.
"""

from rhizome.client import Handle, client


def get_handle() -> Handle:
    """
    Get a database connection handle for the NA Prod Bookkeeper database.
    
    This function requests a port forward from the rhizome server and returns
    a handle that can be used to create database connections.
    
    Returns:
        Handle: Connection handle with connection string and port info
    """
    return client.request_portforward(
        kube_context="gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster",
        kube_namespace="gke-cloudsql-access", 
        kube_deployment="gke-cloudsql-access",
        sql_connection="clover-prod-databases:us-central1:billing-bookkeeper",
        local_port=3306
    )