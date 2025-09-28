"""
Expected data for merchant_suppression_by_app table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_suppression_by_app_v1 import MerchantSuppressionByAppV1


class MerchantSuppressionByAppNaProd(Emplacement[MerchantSuppressionByAppV1]):
    """Expected data for MerchantSuppressionByApp in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantSuppressionByAppV1:
        """Get expected merchant_suppression_by_app data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_suppression_by_app.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantSuppressionByAppV1.model_validate(data)
