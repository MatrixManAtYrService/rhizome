"""
Expected data for reseller_plan_trial table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.reseller_plan_trial_v1 import ResellerPlanTrialV1


class ResellerPlanTrialDev(Emplacement[ResellerPlanTrialV1]):
    """Expected data for ResellerPlanTrialV1 in dev environment."""

    @classmethod
    def get_expected(cls) -> ResellerPlanTrialV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_reseller_plan_trial.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ResellerPlanTrialV1.model_validate(data)
