"""
Expected data for as_of_merchant table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_v1 import AsOfMerchantV1


class AsOfMerchantNaProd(Emplacement[AsOfMerchantV1]):
    """Expected data for AsOfMerchant in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantV1:
        """Get expected as-of-merchant data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )