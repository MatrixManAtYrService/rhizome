"""
Expected data for fee_summary table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1


class FeeSummaryNaProd(Emplacement[FeeSummaryV1]):
    """Expected data for FeeSummary in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FeeSummaryV1:
        """Get expected fee summary data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_fee_summary.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FeeSummaryV1.model_validate(data)
