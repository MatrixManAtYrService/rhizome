"""
Expected data for billing_entity table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.billing_entity_v1 import BillingEntityV1


class BillingEntityNaProd(Emplacement[BillingEntityV1]):
    """Expected data for BillingEntity in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BillingEntityV1:
        """Get expected billing entity data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )