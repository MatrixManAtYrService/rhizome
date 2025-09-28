"""
Expected data for remit_merchant_details table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.remit_merchant_details_v1 import RemitMerchantDetailsV1


class RemitMerchantDetailsNaProd(Emplacement[RemitMerchantDetailsV1]):
    """Expected data for RemitMerchantDetails in na_prod environment."""

    @classmethod
    def get_expected(cls) -> RemitMerchantDetailsV1:
        """Get expected remit_merchant_details data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_remit_merchant_details.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return RemitMerchantDetailsV1.model_validate(data)
