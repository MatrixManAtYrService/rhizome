"""Expected data for fee_ytd table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_ytd_v1 import FeeYtdV1


class FeeYtdDev(Emplacement[FeeYtdV1]):
    """Expected data for FeeYtd in dev environment."""

    @classmethod
    def get_expected(cls) -> FeeYtdV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_fee_ytd.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FeeYtdV1.model_validate(data)
