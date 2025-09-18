"""
Expected data for server_config table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.server_config_v1 import ServerConfigV1


class ServerConfigDemo(Emplacement[ServerConfigV1]):
    """Expected data for ServerConfig in demo environment."""

    @classmethod
    def get_expected(cls) -> ServerConfigV1:
        """Get expected server_config data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
