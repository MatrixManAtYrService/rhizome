"""
Expected data for disbursement_invoice_number table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.disbursement_invoice_number_v1 import DisbursementInvoiceNumberV1


class DisbursementInvoiceNumberNaProd(Emplacement[DisbursementInvoiceNumberV1]):
    """Expected data for DisbursementInvoiceNumber in na_prod environment."""

    @classmethod
    def get_expected(cls) -> DisbursementInvoiceNumberV1:
        """Get expected disbursement_invoice_number data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_disbursement_invoice_number.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return DisbursementInvoiceNumberV1.model_validate(data)
