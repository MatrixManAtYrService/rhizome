"""
Expected data for stage_infolease_charge_attempt table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_infolease_charge_attempt_v1 import StageInfoleaseChargeAttemptV1


class StageInfoleaseChargeAttemptNaProd(Emplacement[StageInfoleaseChargeAttemptV1]):
    """Expected data for StageInfoleaseChargeAttempt in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageInfoleaseChargeAttemptV1:
        """Get expected stage_infolease_charge_attempt data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_infolease_charge_attempt.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StageInfoleaseChargeAttemptV1.model_validate(data)
