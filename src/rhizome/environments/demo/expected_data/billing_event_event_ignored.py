"""
Expected data for event_ignored table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.event_ignored_v1 import EventIgnoredV1


class EventIgnoredDemo(Emplacement[EventIgnoredV1]):
    """Expected data for EventIgnored in demo environment."""

    @classmethod
    def get_expected(cls) -> EventIgnoredV1:
        """Get expected event ignored data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_event_ignored.json"
        with open(file_path) as f:
            data = json.load(f)
        return EventIgnoredV1.model_validate(data)