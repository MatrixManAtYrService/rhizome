"""
Expected data for stage_vendor_disbursement_state_attempt table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_vendor_disbursement_state_attempt_v1 import StageVendorDisbursementStateAttemptV1


class StageVendorDisbursementStateAttemptNaProd(Emplacement[StageVendorDisbursementStateAttemptV1]):
    """Expected data for StageVendorDisbursementStateAttempt in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageVendorDisbursementStateAttemptV1:
        """Get expected stage_vendor_disbursement_state_attempt data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_vendor_disbursement_state_attempt.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StageVendorDisbursementStateAttemptV1.model_validate(data)
