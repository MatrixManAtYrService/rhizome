"""
Expected data for settlement table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
# TODO: Create SettlementV1 model class
# from rhizome.models.billing_bookkeeper.settlement_v1 import SettlementV1


class SettlementDemo(Emplacement):
    """Expected data for Settlement in demo environment."""

    @classmethod
    def get_expected(cls):
        """Get expected settlement data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please create SettlementV1 model and add test data based on real data from this environment."
        )