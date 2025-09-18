"""
Expected data for billing_event_history table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.billing_event_history_v1 import BillingEventHistoryV1


class BillingEventHistoryDemo(Emplacement[BillingEventHistoryV1]):
    """Expected data for BillingEventHistory in demo environment."""

    @classmethod
    def get_expected(cls) -> BillingEventHistoryV1:
        """Get expected billing event history data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )