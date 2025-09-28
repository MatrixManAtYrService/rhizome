"""
Expected data for bi_context table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.bi_context_v1 import BiContextV1


class BiContextNaProd(Emplacement[BiContextV1]):
    """Expected data for BiContext in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BiContextV1:
        """Get expected bi_context data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bi_context.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BiContextV1.model_validate(data)
