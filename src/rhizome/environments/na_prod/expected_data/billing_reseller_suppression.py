"""
Expected data for reseller_suppression table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.reseller_suppression_v1 import ResellerSuppressionV1


class ResellerSuppressionNaProd(Emplacement[ResellerSuppressionV1]):
    """Expected data for ResellerSuppression in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ResellerSuppressionV1:
        """Get expected reseller_suppression data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_reseller_suppression.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ResellerSuppressionV1.model_validate(data)
