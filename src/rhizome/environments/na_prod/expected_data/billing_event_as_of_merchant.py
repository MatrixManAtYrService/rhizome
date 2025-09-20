"""
Expected data for as_of_merchant table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_v1 import AsOfMerchantV1


class AsOfMerchantNaProd(Emplacement[AsOfMerchantV1]):
    """Expected data for AsOfMerchant in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantV1:
        """Get expected as-of-merchant data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_as_of_merchant.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return AsOfMerchantV1.model_validate(data)
