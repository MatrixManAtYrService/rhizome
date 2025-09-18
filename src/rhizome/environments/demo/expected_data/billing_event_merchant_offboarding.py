"""
Expected data for merchant_offboarding table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_offboarding_v1 import MerchantOffboardingV1


class MerchantOffboardingDemo(Emplacement[MerchantOffboardingV1]):
    """Expected data for MerchantOffboarding in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantOffboardingV1:
        """Get expected merchant_offboarding data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
