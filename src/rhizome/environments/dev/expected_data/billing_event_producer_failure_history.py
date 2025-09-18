"""
Expected data for producer_failure_history table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.producer_failure_history_v1 import ProducerFailureHistoryV1


class ProducerFailureHistoryDev(Emplacement[ProducerFailureHistoryV1]):
    """Expected data for ProducerFailureHistory in dev environment."""

    @classmethod
    def get_expected(cls) -> ProducerFailureHistoryV1:
        """Get expected producer_failure_history data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
