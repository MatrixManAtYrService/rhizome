"""
Expected data for uninstalled_app table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.uninstalled_app_v1 import UninstalledAppV1


class UninstalledAppDemo(Emplacement[UninstalledAppV1]):
    """Expected data for UninstalledApp in demo environment."""

    @classmethod
    def get_expected(cls) -> UninstalledAppV1:
        """Get expected uninstalled_app data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_uninstalled_app.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return UninstalledAppV1.model_validate(data)
