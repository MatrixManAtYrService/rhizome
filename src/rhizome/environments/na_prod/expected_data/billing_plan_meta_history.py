"""
Expected data for plan_meta_history table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.plan_meta_history_v1 import PlanMetaHistoryV1


class PlanMetaHistoryNaProd(Emplacement[PlanMetaHistoryV1]):
    """Expected data for PlanMetaHistory in na_prod environment."""

    @classmethod
    def get_expected(cls) -> PlanMetaHistoryV1:
        """Get expected plan_meta_history data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_plan_meta_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return PlanMetaHistoryV1.model_validate(data)
