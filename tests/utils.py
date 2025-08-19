"""
Test utilities shared across multiple test modules.
"""

import socket


def get_open_port() -> int:
    """Get an available port for testing."""
    sock = socket.socket()
    sock.bind(('', 0))
    test_port = sock.getsockname()[1]
    sock.close()
    return test_port
