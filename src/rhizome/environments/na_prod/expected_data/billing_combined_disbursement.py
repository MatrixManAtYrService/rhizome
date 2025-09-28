"""
Expected data for combined_disbursement table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.combined_disbursement_v1 import CombinedDisbursementV1


class CombinedDisbursementNaProd(Emplacement[CombinedDisbursementV1]):
    """Expected data for CombinedDisbursement in na_prod environment."""

    @classmethod
    def get_expected(cls) -> CombinedDisbursementV1:
        """Get expected combined_disbursement data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_combined_disbursement.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return CombinedDisbursementV1.model_validate(data)
