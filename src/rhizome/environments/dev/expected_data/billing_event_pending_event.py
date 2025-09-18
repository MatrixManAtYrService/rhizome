"""
Expected data for pending_event table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.pending_event_v1 import PendingEventV1


class PendingEventDev(Emplacement[PendingEventV1]):
    """Expected data for PendingEvent in dev environment."""

    @classmethod
    def get_expected(cls) -> PendingEventV1:
        """Get expected pending_event data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
