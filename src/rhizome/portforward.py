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

import asyncio
import re

from rhizome.proc import NewProcessResponse, process_manager
from rhizome.tools import Tools


async def port_forward(
    kube_context: str,
    kube_namespace: str,
    kube_deployment: str,
    local_port: int,
    remote_port: int,
    tools: Tools | None = None,
) -> NewProcessResponse:
    """
    Start a simple kubectl port-forward subprocess.

    This is for direct port forwarding to pods/services, like local Kind clusters.

    Args:
        kube_context: Kubernetes context name
        kube_namespace: Kubernetes namespace
        kube_deployment: Kubernetes deployment/pod name
        local_port: Local port to forward from
        remote_port: Remote port to forward to
        tools: Tool dependencies (defaults to external tools)

    Returns:
        NewProcessResponse: Process info for the started port-forward
    """
    process_name = "portforward"
    tools = tools or Tools()

    process = await tools.kubectl.port_forward(
        context=kube_context,
        namespace=kube_namespace,
        resource=f"pod/{kube_deployment}",
        local_port=local_port,
        remote_port=remote_port,
    )

    # Register with process manager for tracking and output streaming
    process_manager.register_process(process, process_name)

    return NewProcessResponse(status="started", pid=process.pid)


async def cloudsql_port_forward(
    kube_context: str,
    kube_namespace: str,
    kube_deployment: str,
    sql_connection: str,
    local_port: int,
    tools: Tools | None = None,
) -> NewProcessResponse:
    """
    Start a Cloud SQL proxy port-forward subprocess.

    This implements the complex production flow:
    1. Check if port is already forwarded
    2. Start connection script in pod
    3. Get the remote port from logs
    4. Set up port forwarding

    Args:
        kube_context: Kubernetes context name
        kube_namespace: Kubernetes namespace
        kube_deployment: Kubernetes deployment name
        sql_connection: SQL connection string (e.g., "clover-prod-databases:us-central1:billing-bookkeeper")
        local_port: Local port to forward to
        tools: Tool dependencies (defaults to external tools)

    Returns:
        NewProcessResponse: Process info for the started port-forward

    Raises:
        RuntimeError: If port is already in use or remote port cannot be discovered
    """
    process_name = "cloudsql-portforward"
    tools = tools or Tools()

    # 1. Check if port is already forwarded
    port_info = await tools.lsof.check_port(local_port)
    if port_info:
        raise RuntimeError(f"Port {local_port} already in use by {port_info[0].process_name}")

    # 2. Start connection script in pod
    connection_command = [
        "nohup",
        "sh",
        "-c",
        f"/home/nonroot/createConnection.sh {sql_connection} > /proc/1/fd/1 2>&1 &",
    ]
    await tools.kubectl.exec_in_pod(
        context=kube_context, namespace=kube_namespace, deployment=kube_deployment, command=connection_command
    )

    # 3. Wait and get remote port from logs
    await asyncio.sleep(5)  # Wait for connection to establish
    logs = await tools.kubectl.get_logs(
        context=kube_context, namespace=kube_namespace, deployment=kube_deployment, since="10s"
    )

    # Parse logs for remote port
    remote_port = None
    for log_line in logs:
        if "Starting proxy" in log_line.content and "on port" in log_line.content:
            # Extract port from log line like "Starting proxy for ... on port '12345'"
            match = re.search(r"on port '(\d+)'", log_line.content)
            if match:
                remote_port = int(match.group(1))
                break

    if remote_port is None:
        raise RuntimeError(f"Failed to discover remote port from logs for connection {sql_connection}")

    # 4. Start port-forward
    process = await tools.kubectl.port_forward(
        context=kube_context,
        namespace=kube_namespace,
        resource=f"deployment/{kube_deployment}",
        local_port=local_port,
        remote_port=remote_port,
    )

    # Register with process manager for tracking and output streaming
    process_manager.register_process(process, process_name)

    return NewProcessResponse(status="started", pid=process.pid)


# Legacy function for backward compatibility
async def start_portforward(
    kube_context: str,
    kube_namespace: str,
    kube_deployment: str,
    sql_connection: str,
    local_port: int = 3306,
    tools: Tools | None = None,
) -> NewProcessResponse:
    """
    Legacy function that routes to the appropriate implementation.

    For localk8s connections, uses simple port_forward.
    For production connections, uses cloudsql_port_forward.
    """
    if sql_connection.startswith("localk8s:"):
        return await port_forward(
            kube_context=kube_context,
            kube_namespace=kube_namespace,
            kube_deployment=kube_deployment,
            local_port=local_port,
            remote_port=3306,  # MySQL default port
            tools=tools,
        )
    else:
        return await cloudsql_port_forward(
            kube_context=kube_context,
            kube_namespace=kube_namespace,
            kube_deployment=kube_deployment,
            sql_connection=sql_connection,
            local_port=local_port,
            tools=tools,
        )


# Legacy function for backward compatibility (no parameters)
async def start_portforward_legacy() -> NewProcessResponse:
    """Legacy start_portforward function for testing compatibility."""
    return await start_portforward(
        kube_context="test-context",
        kube_namespace="test-namespace",
        kube_deployment="test-deployment",
        sql_connection="test:connection",
        local_port=3306,
    )
