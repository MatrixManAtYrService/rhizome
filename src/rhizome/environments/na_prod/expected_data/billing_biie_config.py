"""
Expected data for biie_config table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.biie_config_v1 import BiieConfigV1


class BiieConfigNaProd(Emplacement[BiieConfigV1]):
    """Expected data for BiieConfig in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BiieConfigV1:
        """Get expected biie_config data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_biie_config.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BiieConfigV1.model_validate(data)
