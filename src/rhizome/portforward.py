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

import structlog

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


async def _discover_remote_port(
    tools: Tools,
    kube_context: str,
    kube_namespace: str,
    kube_deployment: str,
    log: structlog.BoundLogger,
) -> int:
    """Poll logs to discover the remote port for CloudSQL proxy."""
    log.info("Waiting for Cloud SQL proxy to establish connection...")
    for i in range(20):  # Poll for up to 60 seconds
        await asyncio.sleep(3)
        logs = await tools.kubectl.get_logs(
            context=kube_context,
            namespace=kube_namespace,
            deployment=kube_deployment,
            since="15s",
        )
        log.info("Checking logs for remote port", attempt=i, logs=logs)

        # Parse logs for remote port
        for log_line in logs:
            log.info("Checking log line", line=log_line.content)
            if (
                "Starting proxy for connectionName" in log_line.content
                and "on port" in log_line.content
            ):
                # Extract port from log line like "Starting proxy for ... on port '12345'"
                match = re.search(r"on port '(\d+)'", log_line.content)
                if match:
                    remote_port = int(match.group(1))
                    log.info("Found remote port", port=remote_port)
                    return remote_port
    raise RuntimeError("Failed to discover remote port from logs")


async def _wait_for_port_forward(
    tools: Tools,
    local_port: int,
    log: structlog.BoundLogger,
) -> None:
    """Wait for the port-forward to start listening."""
    log.info("Waiting for port-forward to start listening...")
    for _ in range(10):
        await asyncio.sleep(1)
        port_info = await tools.lsof.check_port(local_port)
        if port_info:
            log.info("Port is listening!", port_info=port_info)
            return
    log.error("Port-forward did not start listening in time.")
    raise RuntimeError("Port-forward did not start listening in time.")


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
    """
    process_name = "cloudsql-portforward"
    tools = tools or Tools()
    log = structlog.get_logger()

    # 1. Check if port is already forwarded
    port_info = await tools.lsof.check_port(local_port)
    if port_info:
        raise RuntimeError(f"Port {local_port} already in use by {port_info[0].process_name}")

    # 2. Start connection script in pod
    connection_command_args = [
        "nohup",
        "sh",
        "-c",
        f"/home/nonroot/createConnection.sh {sql_connection} > /proc/1/fd/1 2>&1 &",
    ]
    result = await tools.kubectl.exec_in_pod(
        context=kube_context,
        namespace=kube_namespace,
        deployment=kube_deployment,
        command=connection_command_args,
    )
    if not result.success:
        log.error(
            "Failed to start connection script",
            stdout=result.stdout,
            stderr=result.stderr,
        )
        raise RuntimeError("Failed to start connection script")

    # 3. Wait and get remote port from logs
    remote_port = await _discover_remote_port(
        tools=tools,
        kube_context=kube_context,
        kube_namespace=kube_namespace,
        kube_deployment=kube_deployment,
        log=log,
    )

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

    # Give the port-forward a moment to start listening
    await _wait_for_port_forward(tools=tools, local_port=local_port, log=log)

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
