"""Expected data for model_fee_summary table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.model_fee_summary_v1 import ModelFeeSummaryV1


class ModelFeeSummaryDev(Emplacement[ModelFeeSummaryV1]):
    """Expected data for ModelFeeSummary in dev environment."""

    @classmethod
    def get_expected(cls) -> ModelFeeSummaryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_model_fee_summary.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ModelFeeSummaryV1.model_validate(data)
