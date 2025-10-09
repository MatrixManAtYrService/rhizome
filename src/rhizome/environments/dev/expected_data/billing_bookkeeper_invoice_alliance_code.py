"""Expected data for invoice_alliance_code table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.invoice_alliance_code_v1 import InvoiceAllianceCodeV1


class InvoiceAllianceCodeDev(Emplacement[InvoiceAllianceCodeV1]):
    """Expected data for InvoiceAllianceCode in dev environment."""

    @classmethod
    def get_expected(cls) -> InvoiceAllianceCodeV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_invoice_alliance_code.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return InvoiceAllianceCodeV1.model_validate(data)
