"""
Expected data for merchant_evolution table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_evolution_v1 import MerchantEvolutionV1


class MerchantEvolutionDemo(Emplacement[MerchantEvolutionV1]):
    """Expected data for MerchantEvolution in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantEvolutionV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_merchant_evolution.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantEvolutionV1.model_validate(data)
