"""
Expected data for fee_rate table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_rate_v1 import FeeRateV1


class FeeRateDemo(Emplacement[FeeRateV1]):
    """Expected data for FeeRate in demo environment."""

    @classmethod
    def get_expected(cls) -> FeeRateV1:
        """Get expected fee rate data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )