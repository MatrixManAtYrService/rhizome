"""Expected data for fee_ctd table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_ctd_v1 import FeeCtdV1


class FeeCtdDev(Emplacement[FeeCtdV1]):
    """Expected data for FeeCtd in dev environment."""

    @classmethod
    def get_expected(cls) -> FeeCtdV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_fee_ctd.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FeeCtdV1.model_validate(data)
