"""
Expected data for app_subscription_current table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_subscription_current_v1 import AppSubscriptionCurrentV1


class AppSubscriptionCurrentDev(Emplacement[AppSubscriptionCurrentV1]):
    """Expected data for AppSubscriptionCurrent in dev environment."""

    @classmethod
    def get_expected(cls) -> AppSubscriptionCurrentV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_app_subscription_current.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AppSubscriptionCurrentV1.model_validate(data)
