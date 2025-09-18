"""
Expected data for migrated_merchant table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.migrated_merchant_v1 import MigratedMerchantV1


class MigratedMerchantNaProd(Emplacement[MigratedMerchantV1]):
    """Expected data for MigratedMerchant in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MigratedMerchantV1:
        """Get expected migrated_merchant data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
