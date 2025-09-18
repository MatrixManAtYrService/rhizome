"""
Expected data for invoice_info table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.invoice_info_v1 import InvoiceInfoV1


class InvoiceInfoDev(Emplacement[InvoiceInfoV1]):
    """Expected data for InvoiceInfo in dev environment."""

    @classmethod
    def get_expected(cls) -> InvoiceInfoV1:
        """Get expected invoice info data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )