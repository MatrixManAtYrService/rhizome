"""
Expected data for merchant_odessa_mapping table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_odessa_mapping_v1 import MerchantOdessaMappingV1


class MerchantOdessaMappingNaProd(Emplacement[MerchantOdessaMappingV1]):
    """Expected data for MerchantOdessaMapping in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantOdessaMappingV1:
        """Get expected merchant_odessa_mapping data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_odessa_mapping.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantOdessaMappingV1.model_validate(data)
