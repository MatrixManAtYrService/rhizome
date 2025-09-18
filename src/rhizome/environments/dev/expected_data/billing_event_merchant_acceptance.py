"""
Expected data for merchant_acceptance table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_acceptance_v1 import MerchantAcceptanceV1


class MerchantAcceptanceDev(Emplacement[MerchantAcceptanceV1]):
    """Expected data for MerchantAcceptance in dev environment."""

    @classmethod
    def get_expected(cls) -> MerchantAcceptanceV1:
        """Get expected merchant_acceptance data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
