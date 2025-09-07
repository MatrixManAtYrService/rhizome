"""
Expected data for stage_charge table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_charge_v1 import StageChargeV1


class StageChargeNaProd(Emplacement[StageChargeV1]):
    """Expected data for StageCharge in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageChargeV1:
        """Get expected stage charge data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_charge.json"
        with open(file_path) as f:
            data = json.load(f)
        return StageChargeV1.model_validate(data)
