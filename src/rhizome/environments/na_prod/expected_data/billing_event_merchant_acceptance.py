"""
Expected data for merchant_acceptance table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_acceptance_v1 import MerchantAcceptanceV1


class MerchantAcceptanceNaProd(Emplacement[MerchantAcceptanceV1]):
    """Expected data for MerchantAcceptance in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantAcceptanceV1:
        """Get expected merchant_acceptance data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
