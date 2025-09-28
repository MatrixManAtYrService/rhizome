"""
Expected data for suppression_metrics table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.suppression_metrics_v1 import SuppressionMetricsV1


class SuppressionMetricsNaProd(Emplacement[SuppressionMetricsV1]):
    """Expected data for SuppressionMetrics in na_prod environment."""

    @classmethod
    def get_expected(cls) -> SuppressionMetricsV1:
        """Get expected suppression_metrics data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_suppression_metrics.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return SuppressionMetricsV1.model_validate(data)
