"""
Expected data for stage_charge_state_attempt table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_charge_state_attempt_v1 import StageChargeStateAttemptV1


class StageChargeStateAttemptNaProd(Emplacement[StageChargeStateAttemptV1]):
    """Expected data for StageChargeStateAttempt in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageChargeStateAttemptV1:
        """Get expected stage_charge_state_attempt data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_charge_state_attempt.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StageChargeStateAttemptV1.model_validate(data)
