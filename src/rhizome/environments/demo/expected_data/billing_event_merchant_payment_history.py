"""
Expected data for merchant_payment_history table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_payment_history_v1 import MerchantPaymentHistoryV1


class MerchantPaymentHistoryDemo(Emplacement[MerchantPaymentHistoryV1]):
    """Expected data for MerchantPaymentHistory in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantPaymentHistoryV1:
        """Get expected merchant_payment_history data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
