"""
Expected data for device_events table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.device_events_v1 import DeviceEventsV1


class DeviceEventsNaProd(Emplacement[DeviceEventsV1]):
    """Expected data for DeviceEvents in na_prod environment."""

    @classmethod
    def get_expected(cls) -> DeviceEventsV1:
        """Get expected device_events data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_device_events.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return DeviceEventsV1.model_validate(data)
