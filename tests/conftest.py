"""Pytest fixtures for rhizome tests."""

import os
import tempfile
import threading
import time
from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path

import pytest
import uvicorn

from rhizome.config import Home
from rhizome.server import app, setup_logging
from tests.utils import get_open_port


@dataclass
class RunningServer:
    """Represents a running rhizome server instance for testing."""
    port: int
    home: Home


@pytest.fixture(scope="session")
def local_cluster() -> None:
    """Ensure Kind cluster 'rhizome-test' is available and set KUBECONFIG.

    Raises:
        Exception: If the cluster is not available.
    """
    # Set KUBECONFIG to local test config to avoid touching remote infrastructure
    kubeconfig_path = Path("local_test/kubeconfig").absolute()
    if not kubeconfig_path.exists():
        raise Exception(
            f"Local kubeconfig not found at {kubeconfig_path}. "
            "Run 'make up' to create the Kind cluster."
        )

    os.environ["KUBECONFIG"] = str(kubeconfig_path)

    # Check if Kind cluster is available
    import subprocess
    try:
        result = subprocess.run(
            ["kubectl", "cluster-info", "--context", "kind-rhizome-test"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            raise Exception(
                f"Kind cluster 'rhizome-test' not available. "
                f"Run 'make up' first. Error: {result.stderr}"
            )
    except subprocess.TimeoutExpired as e:
        raise Exception("Timeout checking Kind cluster availability.") from e
    except FileNotFoundError as e:
        raise Exception("kubectl not found. Please install kubectl.") from e


@pytest.fixture(scope="session")
def local_mysql(local_cluster: None) -> None:
    """Ensure MySQL pod is ready in the Kind cluster.

    Args:
        local_cluster: Consumes the local_cluster fixture.

    Raises:
        Exception: If the MySQL pod is not ready.
    """
    import subprocess

    try:
        # Check if MySQL pod is ready
        result = subprocess.run([
            "kubectl", "get", "pod", "mysql",
            "-o", "jsonpath={.status.phase}"
        ], capture_output=True, text=True, timeout=10)

        if result.returncode != 0 or result.stdout.strip() != "Running":
            raise Exception(
                "MySQL pod not ready. Run 'tilt up' to deploy MySQL. "
                f"Current status: {result.stdout.strip()}"
            )

        # Check if MySQL is actually ready (not just running)
        result = subprocess.run([
            "kubectl", "get", "pod", "mysql",
            "-o", "jsonpath={.status.conditions[?(@.type==\"Ready\")].status}"
        ], capture_output=True, text=True, timeout=10)

        if result.stdout.strip() != "True":
            raise Exception(
                "MySQL pod is running but not ready. "
                "Wait for the readiness probe to pass."
            )

    except subprocess.TimeoutExpired as e:
        raise Exception("Timeout checking MySQL pod status.") from e
    except FileNotFoundError as e:
        raise Exception("kubectl not found. Please install kubectl.") from e


@pytest.fixture(scope="module")
def rhizome_server(local_mysql: None) -> Generator[RunningServer, None, None]:
    """Start a rhizome server for testing.

    Args:
        local_mysql: Consumes the local_mysql fixture.

    Returns:
        RunningServer: Server instance with port and home attributes.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sandboxed home
        home = Home.sandbox(Path(temp_dir))
        test_port = get_open_port()
        home.set_port(test_port)

        # Setup logging
        setup_logging()

        # Start server in background thread
        def run_server() -> None:
            uvicorn.run(app, host="0.0.0.0", port=test_port, log_config=None)

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        time.sleep(0.5)  # Give server time to start

        yield RunningServer(port=test_port, home=home)
