"""
Expected data for stop_ach_history table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.stop_ach_history_v1 import StopAchHistoryV1


class StopAchHistoryNaProd(Emplacement[StopAchHistoryV1]):
    """Expected data for StopAchHistory in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StopAchHistoryV1:
        """Get expected stop_ach_history data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_stop_ach_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return StopAchHistoryV1.model_validate(data)
