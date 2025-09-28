"""
Expected data for reseller_plan_rev_share table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.reseller_plan_rev_share_v1 import ResellerPlanRevShareV1


class ResellerPlanRevShareNaProd(Emplacement[ResellerPlanRevShareV1]):
    """Expected data for ResellerPlanRevShare in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ResellerPlanRevShareV1:
        """Get expected reseller_plan_rev_share data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_reseller_plan_rev_share.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ResellerPlanRevShareV1.model_validate(data)
