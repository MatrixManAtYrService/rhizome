"""Expected data for revenue_share_group table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.revenue_share_group_v1 import RevenueShareGroupV1


class RevenueShareGroupDev(Emplacement[RevenueShareGroupV1]):
    """Expected data for RevenueShareGroup in dev environment."""

    @classmethod
    def get_expected(cls) -> RevenueShareGroupV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_revenue_share_group.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return RevenueShareGroupV1.model_validate(data)
