"""
Expected data for settlement table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.settlement_v1 import SettlementV1


class SettlementDev(Emplacement[SettlementV1]):
    """Expected data for Settlement in dev environment."""

    @classmethod
    def get_expected(cls) -> SettlementV1:
        """Get expected settlement data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please create SettlementV1 model and add test data based on real data from this environment."
        )
