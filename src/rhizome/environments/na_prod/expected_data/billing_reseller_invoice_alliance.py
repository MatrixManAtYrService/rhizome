"""
Expected data for reseller_invoice_alliance table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.reseller_invoice_alliance_v1 import ResellerInvoiceAllianceV1


class ResellerInvoiceAllianceNaProd(Emplacement[ResellerInvoiceAllianceV1]):
    """Expected data for ResellerInvoiceAlliance in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ResellerInvoiceAllianceV1:
        """Get expected reseller_invoice_alliance data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_reseller_invoice_alliance.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ResellerInvoiceAllianceV1.model_validate(data)
