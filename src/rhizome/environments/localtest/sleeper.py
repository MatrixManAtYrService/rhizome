"""
Local Test Sleeper environment configuration.

This module provides access to local sleeper process testing functionality.
Used for testing rhizome client-server communication without external dependencies.
"""

from __future__ import annotations

from rhizome.client import Handle, RhizomeClient


def get_handle(client: RhizomeClient | None = None, iterations: int = 5) -> Handle:
    """
    Get a handle for a local sleeper process.

    This function requests a sleeper process from the rhizome server and returns
    a handle. Unlike the database environments, this is purely for testing.

    Args:
        client: RhizomeClient instance to use (if None, creates a new one)
        iterations: Number of times the sleeper should count (default: 5)

    Returns:
        Handle: Connection handle with sleeper process info
    """
    if client is None:
        client = RhizomeClient()

    return client.request_sleeper(iterations=iterations)
