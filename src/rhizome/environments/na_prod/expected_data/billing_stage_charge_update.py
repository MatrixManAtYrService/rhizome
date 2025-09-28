"""
Expected data for stage_charge_update table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_charge_update_v1 import StageChargeUpdateV1


class StageChargeUpdateNaProd(Emplacement[StageChargeUpdateV1]):
    """Expected data for StageChargeUpdate in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageChargeUpdateV1:
        """Get expected stage_charge_update data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stage_charge_update.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StageChargeUpdateV1.model_validate(data)
