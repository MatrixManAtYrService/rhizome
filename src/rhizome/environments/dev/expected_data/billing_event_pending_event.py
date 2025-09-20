"""
Expected data for pending_event table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.pending_event_v1 import PendingEventV1


class PendingEventDev(Emplacement[PendingEventV1]):
    """Expected data for PendingEvent in dev environment."""

    @classmethod
    def get_expected(cls) -> PendingEventV1:
        """Get expected pending_event data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_pending_event.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return PendingEventV1.model_validate(data)
