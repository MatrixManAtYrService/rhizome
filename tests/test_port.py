import tempfile
from pathlib import Path

from fastapi.testclient import TestClient

from trifolium.config import Home
from rhizome.server import app
from tests.utils import get_open_port


def test_port_storage_in_sandbox() -> None:
    """Test that port number gets set and retrieved correctly using a sandbox directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a sandboxed Home instance
        home = Home.sandbox(Path(temp_dir))

        test_port = get_open_port()

        home.set_port(test_port)

        # Verify port was stored correctly
        assert home.get_port() == test_port

        # Verify the port file was created in the correct location
        port_file = home.state / "rhizome_port"
        assert port_file.exists()
        assert port_file.read_text().strip() == str(test_port)


def test_port_not_found() -> None:
    """Test that get_port returns None when no port file exists."""
    with tempfile.TemporaryDirectory() as temp_dir:
        home = Home.sandbox(Path(temp_dir))

        # Should return None when no port file exists
        assert home.get_port() is None


def test_port_cleanup_on_server_shutdown() -> None:
    """Test that port file is cleaned up when the server shuts down."""
    with tempfile.TemporaryDirectory() as temp_dir:
        home = Home.sandbox(Path(temp_dir))
        test_port = get_open_port()

        # Set up port file
        home.set_port(test_port)
        port_file = home.state / "rhizome_port"
        assert port_file.exists()

        # Set the global _home variable to our sandbox home
        import rhizome.server

        rhizome.server._home = home  # type: ignore

        # Create test client and trigger shutdown event
        with TestClient(app) as client:
            # Make a request to ensure the app is running
            response = client.get("/ps")
            assert response.status_code == 200

        # After the context manager exits, the shutdown event should have been triggered
        # and the port file should be cleaned up
        assert not port_file.exists()
