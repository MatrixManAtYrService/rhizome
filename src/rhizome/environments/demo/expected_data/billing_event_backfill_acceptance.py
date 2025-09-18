"""
Expected data for backfill_acceptance table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.backfill_acceptance_v1 import BackfillAcceptanceV1


class BackfillAcceptanceDemo(Emplacement[BackfillAcceptanceV1]):
    """Expected data for BackfillAcceptance in demo environment."""

    @classmethod
    def get_expected(cls) -> BackfillAcceptanceV1:
        """Get expected backfill acceptance data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )