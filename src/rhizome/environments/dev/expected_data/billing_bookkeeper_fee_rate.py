"""
Expected data for fee_rate table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_rate_v1 import FeeRateV1


class FeeRateDev(Emplacement[FeeRateV1]):
    """Expected data for FeeRate in dev environment."""

    @classmethod
    def get_expected(cls) -> FeeRateV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_fee_rate.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FeeRateV1.model_validate(data)
