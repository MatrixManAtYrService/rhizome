"""Expected data for prototype_fee_rate table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.prototype_fee_rate_v1 import PrototypeFeeRateV1


class PrototypeFeeRateDev(Emplacement[PrototypeFeeRateV1]):
    """Expected data for PrototypeFeeRate in dev environment."""

    @classmethod
    def get_expected(cls) -> PrototypeFeeRateV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_prototype_fee_rate.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return PrototypeFeeRateV1.model_validate(data)
