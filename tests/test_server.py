import os
import tempfile
import threading
import time
from pathlib import Path

import uvicorn

from rhizome.client import RhizomeClient
from rhizome.server import app, setup_logging
from trifolium.config import Home


def test_multiple_sleeper_processes() -> None:
    """Test starting multiple sleeper processes using real server and client."""
    # Set fast sleep for testing
    os.environ["SLEEP_OVERRIDE"] = "0.1"

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sandboxed home and client
            home = Home.sandbox(Path(temp_dir))
            test_port = 54321
            home.set_port(test_port)

            # Set up logging for the server
            setup_logging()

            # Start server in background thread
            server_thread = threading.Thread(
                target=lambda: uvicorn.run(app, host="0.0.0.0", port=test_port, log_config=None), daemon=True
            )
            server_thread.start()

            # Wait for server to start
            time.sleep(0.5)

            # Create client with sandboxed home
            rhizome_client = RhizomeClient(home=home, data_in_logs=False)

            # Use the client to start two sleeper processes
            handle1 = rhizome_client.request_sleeper(iterations=5)
            assert handle1.connection_string == "sleeper://localhost/test"
            assert handle1.sql_connection == "sleeper-5-iterations"

            handle2 = rhizome_client.request_sleeper(iterations=5)
            assert handle2.connection_string == "sleeper://localhost/test"
            assert handle2.sql_connection == "sleeper-5-iterations"

            # Wait a moment for processes to start
            time.sleep(0.2)

            # Check that both processes appear by making direct request to /ps
            import httpx

            with httpx.Client() as client:
                ps_response = client.get(f"http://0.0.0.0:{test_port}/ps")
                assert ps_response.status_code == 200
                ps_result = ps_response.json()
                assert ps_result["count"] == 2

                # Wait for both processes to complete (5 iterations * 0.1s + buffer)
                time.sleep(1.0)

                # Check that both processes are no longer in /ps (should be empty)
                ps_response = client.get(f"http://0.0.0.0:{test_port}/ps")
                ps_result = ps_response.json()
                assert ps_result["count"] == 0

    finally:
        # Clean up environment variable
        if "SLEEP_OVERRIDE" in os.environ:
            del os.environ["SLEEP_OVERRIDE"]


def test_single_sleeper_process() -> None:
    """Test single sleeper process using real server and client."""
    # Set fast sleep for testing
    os.environ["SLEEP_OVERRIDE"] = "0.1"

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sandboxed home and client
            home = Home.sandbox(Path(temp_dir))
            test_port = 54322
            home.set_port(test_port)

            # Set up logging for the server
            setup_logging()

            # Start server in background thread
            server_thread = threading.Thread(
                target=lambda: uvicorn.run(app, host="0.0.0.0", port=test_port, log_config=None), daemon=True
            )
            server_thread.start()

            # Wait for server to start
            time.sleep(0.5)

            # Create client with sandboxed home
            rhizome_client = RhizomeClient(home=home, data_in_logs=False)

            # Use the client to start a sleeper process
            handle = rhizome_client.request_sleeper(iterations=3)
            assert handle.connection_string == "sleeper://localhost/test"
            assert handle.sql_connection == "sleeper-3-iterations"

            # Wait a moment for process to start
            time.sleep(0.2)

            # Check that process appears in /ps
            import httpx

            with httpx.Client() as client:
                ps_response = client.get(f"http://0.0.0.0:{test_port}/ps")
                assert ps_response.status_code == 200
                ps_result = ps_response.json()
                assert ps_result["count"] >= 1

                # Wait for process to complete (3 iterations * 0.1s + buffer)
                time.sleep(0.8)

                # Check that process is no longer in /ps
                ps_response = client.get(f"http://0.0.0.0:{test_port}/ps")
                ps_result = ps_response.json()
                # Process should be cleaned up automatically
                assert ps_result["count"] == 0

    finally:
        # Clean up environment variable
        if "SLEEP_OVERRIDE" in os.environ:
            del os.environ["SLEEP_OVERRIDE"]


def test_ps_endpoint() -> None:
    """Test that /ps endpoint returns process list using real server."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sandboxed home
        home = Home.sandbox(Path(temp_dir))
        test_port = 54323
        home.set_port(test_port)

        # Set up logging for the server
        setup_logging()

        # Start server in background thread
        server_thread = threading.Thread(
            target=lambda: uvicorn.run(app, host="0.0.0.0", port=test_port, log_config=None), daemon=True
        )
        server_thread.start()

        # Wait for server to start
        time.sleep(0.5)

        # Test /ps endpoint
        import httpx

        with httpx.Client() as client:
            ps_response = client.get(f"http://0.0.0.0:{test_port}/ps")
            assert ps_response.status_code == 200
            ps_result = ps_response.json()
            assert "running" in ps_result
            assert "count" in ps_result
            assert ps_result["count"] == len(ps_result["running"])
