"""
Expected data for locale table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.locale import Locale


class LocaleDev(Emplacement[Locale]):
    """Expected data for Locale in dev environment."""

    @classmethod
    def get_expected(cls) -> Locale:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_locale.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return Locale.model_validate(data)
