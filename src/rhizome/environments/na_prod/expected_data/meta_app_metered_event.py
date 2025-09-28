"""
Expected data for app_metered_event table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.app_metered_event import AppMeteredEvent


class AppMeteredEventNaProd(Emplacement[AppMeteredEvent]):
    """Expected data for AppMeteredEvent in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppMeteredEvent:
        """Get expected app_metered_event data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_app_metered_event.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return AppMeteredEvent.model_validate(data)
