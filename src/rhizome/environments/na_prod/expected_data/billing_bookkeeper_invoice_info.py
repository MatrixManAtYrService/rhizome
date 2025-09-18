"""
Expected data for invoice_info table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.invoice_info_v1 import InvoiceInfoV1


class InvoiceInfoNaProd(Emplacement[InvoiceInfoV1]):
    """Expected data for InvoiceInfo in na_prod environment."""

    @classmethod
    def get_expected(cls) -> InvoiceInfoV1:
        """Get expected invoice info data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )