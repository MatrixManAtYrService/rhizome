"""
Expected data for server_config table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.server_config_v1 import ServerConfigV1


class ServerConfigDemo(Emplacement[ServerConfigV1]):
    """Expected data for ServerConfig in demo environment."""

    @classmethod
    def get_expected(cls) -> ServerConfigV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_server_config.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ServerConfigV1.model_validate(data)
