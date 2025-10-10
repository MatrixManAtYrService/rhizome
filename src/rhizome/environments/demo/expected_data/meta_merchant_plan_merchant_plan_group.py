"""
Expected data for merchant_plan_merchant_plan_group table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_plan_merchant_plan_group_v1 import MerchantPlanMerchantPlanGroupV1


class MerchantPlanMerchantPlanGroupDemo(Emplacement[MerchantPlanMerchantPlanGroupV1]):
    """Expected data for MerchantPlanMerchantPlanGroup in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantPlanMerchantPlanGroupV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_plan_merchant_plan_group.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantPlanMerchantPlanGroupV1.model_validate(data)
