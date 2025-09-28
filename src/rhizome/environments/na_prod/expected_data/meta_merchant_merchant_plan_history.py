"""
Expected data for merchant_merchant_plan_history table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_merchant_plan_history import MerchantMerchantPlanHistory


class MerchantMerchantPlanHistoryNaProd(Emplacement[MerchantMerchantPlanHistory]):
    """Expected data for MerchantMerchantPlanHistory in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantMerchantPlanHistory:
        """Get expected merchant_merchant_plan_history data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_merchant_plan_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantMerchantPlanHistory.model_validate(data)
