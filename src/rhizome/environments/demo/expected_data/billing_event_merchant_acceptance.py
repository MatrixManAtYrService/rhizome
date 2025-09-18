"""
Expected data for merchant_acceptance table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_acceptance_v1 import MerchantAcceptanceV1


class MerchantAcceptanceDemo(Emplacement[MerchantAcceptanceV1]):
    """Expected data for MerchantAcceptance in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantAcceptanceV1:
        """Get expected merchant_acceptance data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
