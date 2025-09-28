"""
Expected data for reseller_plan_trial table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.reseller_plan_trial import ResellerPlanTrial


class ResellerPlanTrialNaProd(Emplacement[ResellerPlanTrial]):
    """Expected data for ResellerPlanTrial in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ResellerPlanTrial:
        """Get expected reseller_plan_trial data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_reseller_plan_trial.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ResellerPlanTrial.model_validate(data)
