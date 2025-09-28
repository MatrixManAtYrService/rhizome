"""
Expected data for vat_vendor_disbursement table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.vat_vendor_disbursement_v1 import VatVendorDisbursementV1


class VatVendorDisbursementNaProd(Emplacement[VatVendorDisbursementV1]):
    """Expected data for VatVendorDisbursement in na_prod environment."""

    @classmethod
    def get_expected(cls) -> VatVendorDisbursementV1:
        """Get expected vat_vendor_disbursement data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_vat_vendor_disbursement.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return VatVendorDisbursementV1.model_validate(data)
