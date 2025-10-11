"""
Expected data for merchant_merchant_plan_history table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_merchant_plan_history_v1 import MerchantMerchantPlanHistoryV1


class MerchantMerchantPlanHistoryDev(Emplacement[MerchantMerchantPlanHistoryV1]):
    """Expected data for MerchantMerchantPlanHistoryV1 in dev environment."""

    @classmethod
    def get_expected(cls) -> MerchantMerchantPlanHistoryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_merchant_plan_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantMerchantPlanHistoryV1.model_validate(data)
