"""
Expected data for merchant_plan table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_plan import MerchantPlan


class MerchantPlanNaProd(Emplacement[MerchantPlan]):
    """Expected data for MerchantPlan in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantPlan:
        """Get expected merchant_plan data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_plan.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantPlan.model_validate(data)
