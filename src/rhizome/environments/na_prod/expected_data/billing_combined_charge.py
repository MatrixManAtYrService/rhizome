"""
Expected data for combined_charge table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.combined_charge_v1 import CombinedChargeV1


class CombinedChargeNaProd(Emplacement[CombinedChargeV1]):
    """Expected data for CombinedCharge in na_prod environment."""

    @classmethod
    def get_expected(cls) -> CombinedChargeV1:
        """Get expected combined_charge data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_combined_charge.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return CombinedChargeV1.model_validate(data)
