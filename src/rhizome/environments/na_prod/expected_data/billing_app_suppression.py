"""
Expected data for app_suppression table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.app_suppression_v1 import AppSuppressionV1


class AppSuppressionNaProd(Emplacement[AppSuppressionV1]):
    """Expected data for AppSuppression in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppSuppressionV1:
        """Get expected app_suppression data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_app_suppression.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return AppSuppressionV1.model_validate(data)