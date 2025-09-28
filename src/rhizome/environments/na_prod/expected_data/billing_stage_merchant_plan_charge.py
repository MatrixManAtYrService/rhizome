"""
Expected data for stage_merchant_plan_charge table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_merchant_plan_charge_v1 import StageMerchantPlanChargeV1


class StageMerchantPlanChargeNaProd(Emplacement[StageMerchantPlanChargeV1]):
    """Expected data for StageMerchantPlanCharge in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageMerchantPlanChargeV1:
        """Get expected stage_merchant_plan_charge data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_merchant_plan_charge.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StageMerchantPlanChargeV1.model_validate(data)
