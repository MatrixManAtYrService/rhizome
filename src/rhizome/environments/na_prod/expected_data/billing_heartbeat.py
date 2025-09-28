"""
Expected data for heartbeat table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.heartbeat_v1 import HeartbeatV1


class HeartbeatNaProd(Emplacement[HeartbeatV1]):
    """Expected data for Heartbeat in na_prod environment."""

    @classmethod
    def get_expected(cls) -> HeartbeatV1:
        """Get expected heartbeat data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_heartbeat.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return HeartbeatV1.model_validate(data)