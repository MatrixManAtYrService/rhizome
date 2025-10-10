"""
Expected data for reseller table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.reseller import Reseller


class ResellerDemo(Emplacement[Reseller]):
    """Expected data for Reseller in demo environment."""

    @classmethod
    def get_expected(cls) -> Reseller:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_reseller.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return Reseller.model_validate(data)
