"""
Expected data for biie_file_staging_data table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.biie_file_staging_data_v1 import BiieFileStagingDataV1


class BiieFileStagingDataNaProd(Emplacement[BiieFileStagingDataV1]):
    """Expected data for BiieFileStagingData in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BiieFileStagingDataV1:
        """Get expected biie_file_staging_data data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_biie_file_staging_data.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BiieFileStagingDataV1.model_validate(data)
