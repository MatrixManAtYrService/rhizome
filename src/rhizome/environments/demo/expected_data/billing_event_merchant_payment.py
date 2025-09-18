"""
Expected data for merchant_payment table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_payment_v1 import MerchantPaymentV1


class MerchantPaymentDemo(Emplacement[MerchantPaymentV1]):
    """Expected data for MerchantPayment in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantPaymentV1:
        """Get expected merchant_payment data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
