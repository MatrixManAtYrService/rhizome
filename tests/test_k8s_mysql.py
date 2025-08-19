"""
Test local Kubernetes MySQL integration.

Verifies rhizome can connect to local Kind cluster MySQL and query expected data.
"""

import os
import subprocess
import tempfile
import threading
import time
from pathlib import Path

import uvicorn
from sqlmodel import Session, create_engine, select

import rhizome.environments.localtest.localk8s as localk8s
from rhizome.config import Home
from rhizome.models.bookkeeper.fee_summary import FeeSummary, sanitize
from rhizome.server import app, setup_logging
from tests.utils import get_open_port


def is_kind_cluster_available() -> bool:
    """Check if the rhizome-test Kind cluster is available."""
    try:
        result = subprocess.run(
            ["kind", "get", "clusters"],
            capture_output=True,
            text=True,
            check=False
        )
        return "rhizome-test" in result.stdout
    except FileNotFoundError:
        return False


def is_mysql_pod_ready() -> bool:
    """Check if the MySQL pod is ready in the Kind cluster."""
    kubeconfig_path = Path("local_test/kubeconfig")
    if not kubeconfig_path.exists():
        return False

    try:
        result = subprocess.run([
            "kubectl", f"--kubeconfig={kubeconfig_path.absolute()}",
            "get", "pod", "mysql", "-o", "jsonpath={.status.phase}"
        ], capture_output=True, text=True, check=False)
        return result.stdout.strip() == "Running"
    except FileNotFoundError:
        return False


def test_mysql_connection_and_sanitization() -> None:
    """Test MySQL connection, data query, and sanitization functionality."""
    # Fail if prerequisites aren't met
    assert is_kind_cluster_available(), "Kind cluster 'rhizome-test' not available. Run 'make up' first."
    assert is_mysql_pod_ready(), "MySQL pod not ready. Run 'tilt up' to deploy MySQL."

    # Disable simulation mode for this test
    original_simulate = os.environ.get("RHIZOME_SIMULATE")
    os.environ["RHIZOME_SIMULATE"] = "false"

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sandboxed home and client
            home = Home.sandbox(Path(temp_dir))
            test_port = 54324
            home.set_port(test_port)

            # Set up logging and start server
            setup_logging()
            server_thread = threading.Thread(
                target=lambda: uvicorn.run(app, host="0.0.0.0", port=test_port, log_config=None),
                daemon=True
            )
            server_thread.start()
            time.sleep(0.5)

            # Set KUBECONFIG and configure client
            kubeconfig_path = Path("local_test/kubeconfig").absolute()
            os.environ["KUBECONFIG"] = str(kubeconfig_path)
            localk8s.client.home = home

            # Connect to MySQL via rhizome port forwarding
            mysql_port = get_open_port()
            print(f"Using MySQL port: {mysql_port}")
            handle = localk8s.get_handle(local_port=mysql_port, delay=1.5)
            engine = create_engine(handle.connection_string)

            with Session(engine) as session:
                # Query for expected test data
                statement = select(FeeSummary).where(FeeSummary.id == 74347)
                fee_summary = session.exec(statement).first()

                assert fee_summary is not None, "Test data with ID 74347 should exist"

                # Verify key fields match expected test data
                assert fee_summary.billing_entity_uuid == "JW8H2B9BT6B11R2HHXY3HYQCN6"
                assert fee_summary.fee_code == "MW63DAWPN6JGY.S"
                assert fee_summary.currency == "USD"
                assert float(fee_summary.total_fee_amount) == 9.99

                # Test sanitization - UUID fields should be hashed, other fields unchanged
                sanitized = sanitize(fee_summary)
                assert sanitized.billing_entity_uuid != fee_summary.billing_entity_uuid
                assert sanitized.uuid != fee_summary.uuid
                assert sanitized.fee_code == fee_summary.fee_code  # Non-UUID field unchanged

    finally:
        # Clean up environment variables
        if original_simulate is not None:
            os.environ["RHIZOME_SIMULATE"] = original_simulate
        elif "RHIZOME_SIMULATE" in os.environ:
            del os.environ["RHIZOME_SIMULATE"]

        if "KUBECONFIG" in os.environ:
            del os.environ["KUBECONFIG"]
