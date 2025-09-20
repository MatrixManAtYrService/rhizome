"""
Expected data for event_ignored table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.event_ignored_v1 import EventIgnoredV1


class EventIgnoredDev(Emplacement[EventIgnoredV1]):
    """Expected data for EventIgnored in dev environment."""

    @classmethod
    def get_expected(cls) -> EventIgnoredV1:
        """Get expected event ignored data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_event_ignored.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return EventIgnoredV1.model_validate(data)
