"""
Local Test environment configuration.

This module provides access to local testing functionality using the sleeper process.
Used for testing rhizome client-server communication without external dependencies.
"""

from rhizome.client import Handle, client


def get_handle(iterations: int = 5) -> Handle:
    """
    Get a handle for a local sleeper process.

    This function requests a sleeper process from the rhizome server and returns
    a handle. Unlike the database environments, this is purely for testing.

    Args:
        iterations: Number of times the sleeper should count (default: 5)

    Returns:
        Handle: Connection handle with sleeper process info
    """
    return client.request_sleeper(iterations=iterations)