"""
Expected data for stage_infolease_disbursement_attempt table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_infolease_disbursement_attempt_v1 import StageInfoleaseDisbursementAttemptV1


class StageInfoleaseDisbursementAttemptNaProd(Emplacement[StageInfoleaseDisbursementAttemptV1]):
    """Expected data for StageInfoleaseDisbursementAttempt in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageInfoleaseDisbursementAttemptV1:
        """Get expected stage_infolease_disbursement_attempt data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_infolease_disbursement_attempt.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StageInfoleaseDisbursementAttemptV1.model_validate(data)
