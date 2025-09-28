"""
Expected data for developer table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.developer import Developer


class DeveloperNaProd(Emplacement[Developer]):
    """Expected data for Developer in na_prod environment."""

    @classmethod
    def get_expected(cls) -> Developer:
        """Get expected developer data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_developer.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return Developer.model_validate(data)
