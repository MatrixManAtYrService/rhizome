"""
Expected data for billing_entity table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.billing_entity_v1 import BillingEntityV1


class BillingEntityDemo(Emplacement[BillingEntityV1]):
    """Expected data for BillingEntity in demo environment."""

    @classmethod
    def get_expected(cls) -> BillingEntityV1:
        """Get expected billing entity data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )