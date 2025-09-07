"""
Cluster connection management.

This module handles connecting to Kubernetes clusters.
"""

import structlog

from rhizome.tools import Tools


async def connect_cluster(
    project: str,
    cluster: str,
    region: str,
    server: str,
    tools: Tools,
) -> None:
    """
    Connect to a Kubernetes cluster.

    This function replicates the logic from the nushell `connect-cluster` function.
    """
    log = structlog.get_logger()
    source = "mock" if tools.is_mocked() else "subprocess"

    log.info("Getting cluster credentials...", source=source)
    result = await tools.gcloud.get_cluster_credentials(
        project=project, cluster=cluster, region=region
    )
    if not result.success:
        log.error(
            "Failed to get cluster credentials",
            stdout=result.stdout,
            stderr=result.stderr,
        )
        raise RuntimeError("Failed to get cluster credentials")

    fqcn = f"gke_{project}_{region}_{cluster}"
    log.info("Setting cluster server...", fqcn=fqcn, server=server, source=source)
    result = await tools.gcloud.set_cluster_server(cluster_name=fqcn, server_url=server)
    if not result.success:
        log.error(
            "Failed to set cluster server",
            stdout=result.stdout,
            stderr=result.stderr,
        )
        raise RuntimeError("Failed to set cluster server")

    log.info("Unsetting certificate authority data...", source=source)
    # There is no specific tool for this, so we use the internal _run_command
    # from the kubectl tool. This is a bit of a hack, but it's the cleanest way
    # to do it without adding a new method to the KubectlTool interface.
    result = await tools.kubectl.unset_cluster_ca(cluster_name=fqcn)
    if not result.success:
        log.error(
            "Failed to unset certificate authority data",
            stdout=result.stdout,
            stderr=result.stderr,
        )
        # This is not a fatal error, so we just log it and continue.
        log.warning("Could not unset certificate authority data. This may or may not be a problem.")
