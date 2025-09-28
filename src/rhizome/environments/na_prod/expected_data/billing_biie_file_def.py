"""
Expected data for biie_file_def table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.biie_file_def_v1 import BiieFileDefV1


class BiieFileDefNaProd(Emplacement[BiieFileDefV1]):
    """Expected data for BiieFileDef in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BiieFileDefV1:
        """Get expected biie_file_def data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_biie_file_def.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BiieFileDefV1.model_validate(data)
