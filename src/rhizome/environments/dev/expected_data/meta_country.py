"""
Expected data for country table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.country import Country


class CountryDev(Emplacement[Country]):
    """Expected data for Country in dev environment."""

    @classmethod
    def get_expected(cls) -> Country:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_country.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return Country.model_validate(data)
