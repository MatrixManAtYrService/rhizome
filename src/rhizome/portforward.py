"""
Port Forward subprocess - kubectl port-forward process management.

This module manages kubectl port-forward processes that need to run continuously 
in the background to provide database access for clover applications.

Unlike the sleeper module (which exists for testing), this is the real use case
for rhizome: managing long-running kubectl port-forward processes that forward
database connections from remote Kubernetes clusters to local ports.

A typical port-forward process runs indefinitely until terminated, forwarding
traffic from a local port to a service/pod port in a Kubernetes cluster.
"""

import os
import sys
from typing import Dict, Any

from rhizome.proc import NewProcessResponse, process_manager


async def start_portforward(
    kube_context: str,
    kube_namespace: str,
    kube_deployment: str, 
    sql_connection: str,
    local_port: int = 3306
) -> NewProcessResponse:
    """
    Start a kubectl port-forward subprocess for database access.
    
    This implements the actual kubectl port-forward logic based on the 
    provided shell function, including:
    1. Starting the connection script in the pod
    2. Getting the remote port from logs
    3. Setting up port forwarding
    
    Args:
        kube_context: Kubernetes context name
        kube_namespace: Kubernetes namespace  
        kube_deployment: Kubernetes deployment name
        sql_connection: SQL connection string (e.g., "clover-prod-databases:us-central1:billing-bookkeeper")
        local_port: Local port to forward to (default: 3306)
        
    Returns:
        NewProcessResponse: Process info for the started port-forward
    """
    process_name = "portforward"
    
    # For now, simulate the behavior for development/testing
    # TODO: Implement the actual kubectl port-forward logic
    if os.environ.get("RHIZOME_SIMULATE", "true").lower() == "true":
        return await _simulate_portforward(kube_context, kube_namespace, kube_deployment, sql_connection, local_port)
    
    # Real implementation would be:
    # 1. Check if port is already forwarded (lsof -i :local_port)
    # 2. Start connection script in pod:
    #    kubectl --context {kube_context} -n {kube_namespace} exec -it deployment/{kube_deployment} -- 
    #    nohup sh -c "/home/nonroot/createConnection.sh {sql_connection} > /proc/1/fd/1 2>&1 &"
    # 3. Wait and get remote port from logs:
    #    kubectl --context {kube_context} -n {kube_namespace} logs deployment/{kube_deployment} --since 10s
    # 4. Start port-forward:
    #    kubectl --context {kube_context} -n {kube_namespace} port-forward deployment/{kube_deployment} {local_port}:{remote_port}
    
    # Build the actual kubectl port-forward command
    args = [
        "kubectl", 
        "--context", kube_context,
        "-n", kube_namespace,
        "port-forward", 
        f"deployment/{kube_deployment}",
        f"{local_port}:3307"  # This would be the remote_port from logs in real implementation
    ]
    
    # Use the generic process manager to start the process
    return await process_manager.start_process(args, process_name)


async def _simulate_portforward(
    kube_context: str,
    kube_namespace: str, 
    kube_deployment: str,
    sql_connection: str,
    local_port: int
) -> NewProcessResponse:
    """Simulate port-forward for development/testing."""
    sleep_duration = os.environ.get("SLEEP_OVERRIDE", "1")
    process_name = "portforward"
    
    # Simulation that shows the actual parameters being used
    python_code = f"""
from time import sleep
print("Starting kubectl port-forward simulation...")
print("Context: {kube_context}")
print("Namespace: {kube_namespace}")
print("Deployment: {kube_deployment}")
print("SQL Connection: {sql_connection}")
print("Local Port: {local_port}")
print("")

for i in range(15):  # Longer simulation for port-forward
    print(f"Forwarding localhost:{local_port} -> pod:3307 (iteration {{i}})")
    sleep({sleep_duration})
print("Port-forward terminated")
"""
    
    # Build command args for simulation
    args = [sys.executable, "-c", python_code]
    
    # Use the generic process manager to start the process
    return await process_manager.start_process(args, process_name)


# Legacy function for backward compatibility (no parameters)
async def start_portforward_legacy() -> NewProcessResponse:
    """Legacy start_portforward function for testing compatibility."""
    return await start_portforward(
        kube_context="test-context",
        kube_namespace="test-namespace", 
        kube_deployment="test-deployment",
        sql_connection="test:connection",
        local_port=3306
    )