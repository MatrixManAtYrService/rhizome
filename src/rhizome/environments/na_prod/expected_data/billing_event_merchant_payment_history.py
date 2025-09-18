"""
Expected data for merchant_payment_history table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_payment_history_v1 import MerchantPaymentHistoryV1


class MerchantPaymentHistoryNaProd(Emplacement[MerchantPaymentHistoryV1]):
    """Expected data for MerchantPaymentHistory in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantPaymentHistoryV1:
        """Get expected merchant_payment_history data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
