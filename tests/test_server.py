import os
import time
from io import StringIO

from fastapi.testclient import TestClient

from rhizome.server import app


def test_multiple_sleeper_processes() -> None:
    """Test starting multiple sleeper processes and tracking them until completion."""
    # Set fast sleep for testing
    os.environ["SLEEP_OVERRIDE"] = "0.1"
    
    try:
        with TestClient(app) as client:
            # Start two sleeper processes
            response1 = client.post("/sleeper")
            assert response1.status_code == 200
            result1 = response1.json()
            assert result1["status"] == "started"
            assert "pid" in result1
            
            response2 = client.post("/sleeper")
            assert response2.status_code == 200
            result2 = response2.json()
            assert result2["status"] == "started"
            assert "pid" in result2
            
            # Ensure we got different PIDs
            assert result1["pid"] != result2["pid"]
            
            # Wait a moment for processes to start
            time.sleep(0.1)
            
            # Check that both processes appear in /ps
            ps_response = client.get("/ps")
            assert ps_response.status_code == 200
            ps_result = ps_response.json()
            assert ps_result["count"] == 2
            
            # Verify both PIDs are in the running list
            running_pids = {p["pid"] for p in ps_result["running"]}
            assert result1["pid"] in running_pids
            assert result2["pid"] in running_pids
            
            # Wait for both processes to complete (5 iterations * 0.1s + buffer)
            # We need to wait long enough for both "subprocess finished" messages
            time.sleep(1.0)
            
            # Check that both processes are no longer in /ps (should be empty)
            ps_response = client.get("/ps")
            ps_result = ps_response.json()
            assert ps_result["count"] == 0
            assert len(ps_result["running"]) == 0
            
    finally:
        # Clean up environment variable
        if "SLEEP_OVERRIDE" in os.environ:
            del os.environ["SLEEP_OVERRIDE"]


def test_single_sleeper_process() -> None:
    """Test that /sleeper endpoint starts subprocess and we can track its lifecycle."""
    # Set fast sleep for testing
    os.environ["SLEEP_OVERRIDE"] = "0.1"
    
    try:
        with TestClient(app) as client:
            # Start the subprocess
            response = client.post("/sleeper")
            assert response.status_code == 200
            result = response.json()
            assert result["status"] == "started"
            assert "pid" in result
            
            # Check that process appears in /ps
            ps_response = client.get("/ps")
            assert ps_response.status_code == 200
            ps_result = ps_response.json()
            assert ps_result["count"] >= 1
            assert any(p["pid"] == result["pid"] for p in ps_result["running"])
            
            # Wait for process to complete (5 iterations * 0.1s + buffer)
            time.sleep(1.0)
            
            # Check that process is no longer in /ps
            ps_response = client.get("/ps")
            ps_result = ps_response.json()
            # Process should be cleaned up automatically
            assert not any(p["pid"] == result["pid"] for p in ps_result["running"])
            
    finally:
        # Clean up environment variable
        if "SLEEP_OVERRIDE" in os.environ:
            del os.environ["SLEEP_OVERRIDE"]


def test_ps_endpoint() -> None:
    """Test that /ps endpoint returns process list."""
    with TestClient(app) as client:
        # Initially should have no processes (or clean up from previous tests)
        ps_response = client.get("/ps")
        assert ps_response.status_code == 200
        ps_result = ps_response.json()
        assert "running" in ps_result
        assert "count" in ps_result
        assert ps_result["count"] == len(ps_result["running"])