"""
Expected data for invoice_info table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.invoice_info_v1 import InvoiceInfoV1


class InvoiceInfoNaProd(Emplacement[InvoiceInfoV1]):
    """Expected data for InvoiceInfo in na_prod environment."""

    @classmethod
    def get_expected(cls) -> InvoiceInfoV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_invoice_info.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return InvoiceInfoV1.model_validate(data)
