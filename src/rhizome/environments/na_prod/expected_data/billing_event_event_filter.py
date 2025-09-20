"""
Expected data for event_filter table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.event_filter_v1 import EventFilterV1


class EventFilterNaProd(Emplacement[EventFilterV1]):
    """Expected data for EventFilter in na_prod environment."""

    @classmethod
    def get_expected(cls) -> EventFilterV1:
        """Get expected event filter data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_event_filter.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return EventFilterV1.model_validate(data)