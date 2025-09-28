"""
Expected data for corollary_data table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.corollary_data_v1 import CorollaryDataV1


class CorollaryDataNaProd(Emplacement[CorollaryDataV1]):
    """Expected data for CorollaryData in na_prod environment."""

    @classmethod
    def get_expected(cls) -> CorollaryDataV1:
        """Get expected corollary_data data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_corollary_data.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return CorollaryDataV1.model_validate(data)
