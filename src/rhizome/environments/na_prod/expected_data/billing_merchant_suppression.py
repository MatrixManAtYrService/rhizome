"""
Expected data for merchant_suppression table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_suppression_v1 import MerchantSuppressionV1


class MerchantSuppressionNaProd(Emplacement[MerchantSuppressionV1]):
    """Expected data for MerchantSuppression in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantSuppressionV1:
        """Get expected merchant_suppression data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_suppression.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantSuppressionV1.model_validate(data)
