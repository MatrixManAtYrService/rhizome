"""
Expected data for app_metered_event table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1


class AppMeteredEventDemo(Emplacement[AppMeteredEventV1]):
    """Expected data for AppMeteredEvent in demo environment."""

    @classmethod
    def get_expected(cls) -> AppMeteredEventV1:
        """Get expected app metered event data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_app_metered_event.json"
        with open(file_path) as f:
            data = json.load(f)
        return AppMeteredEventV1.model_validate(data)
