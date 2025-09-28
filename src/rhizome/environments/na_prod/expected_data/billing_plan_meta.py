"""
Expected data for plan_meta table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.plan_meta_v1 import PlanMetaV1


class PlanMetaNaProd(Emplacement[PlanMetaV1]):
    """Expected data for PlanMeta in na_prod environment."""

    @classmethod
    def get_expected(cls) -> PlanMetaV1:
        """Get expected plan_meta data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_plan_meta.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return PlanMetaV1.model_validate(data)
