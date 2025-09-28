"""
Expected data for invoice_charge table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.invoice_charge_v1 import InvoiceChargeV1


class InvoiceChargeNaProd(Emplacement[InvoiceChargeV1]):
    """Expected data for InvoiceCharge in na_prod environment."""

    @classmethod
    def get_expected(cls) -> InvoiceChargeV1:
        """Get expected invoice_charge data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_invoice_charge.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return InvoiceChargeV1.model_validate(data)
