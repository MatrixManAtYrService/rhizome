"""
Expected data for as_of_merchant_plan table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_plan_v1 import AsOfMerchantPlanV1


class AsOfMerchantPlanNaProd(Emplacement[AsOfMerchantPlanV1]):
    """Expected data for AsOfMerchantPlan in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantPlanV1:
        """Get expected as of merchant plan data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_as_of_merchant_plan.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return AsOfMerchantPlanV1.model_validate(data)
