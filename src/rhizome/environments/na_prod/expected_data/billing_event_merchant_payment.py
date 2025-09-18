"""
Expected data for merchant_payment table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_payment_v1 import MerchantPaymentV1


class MerchantPaymentNaProd(Emplacement[MerchantPaymentV1]):
    """Expected data for MerchantPayment in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantPaymentV1:
        """Get expected merchant_payment data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
