"""Expected data for tiered_pricing table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.tiered_pricing_v1 import TieredPricingV1


class TieredPricingDev(Emplacement[TieredPricingV1]):
    """Expected data for TieredPricing in dev environment."""

    @classmethod
    def get_expected(cls) -> TieredPricingV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_tiered_pricing.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return TieredPricingV1.model_validate(data)
