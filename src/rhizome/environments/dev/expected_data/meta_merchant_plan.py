"""
Expected data for merchant_plan table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_plan_v1 import MerchantPlanV1


class MerchantPlanDev(Emplacement[MerchantPlanV1]):
    """Expected data for MerchantPlanV1 in dev environment."""

    @classmethod
    def get_expected(cls) -> MerchantPlanV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_plan.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantPlanV1.model_validate(data)
