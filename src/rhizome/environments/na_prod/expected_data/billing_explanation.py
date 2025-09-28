"""
Expected data for explanation table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.explanation_v1 import ExplanationV1


class ExplanationNaProd(Emplacement[ExplanationV1]):
    """Expected data for Explanation in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ExplanationV1:
        """Get expected explanation data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_explanation.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ExplanationV1.model_validate(data)
