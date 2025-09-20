"""
Expected data for app_subscription_event table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_subscription_event_v1 import AppSubscriptionEventV1


class AppSubscriptionEventDemo(Emplacement[AppSubscriptionEventV1]):
    """Expected data for AppSubscriptionEvent in demo environment."""

    @classmethod
    def get_expected(cls) -> AppSubscriptionEventV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_app_subscription_event.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AppSubscriptionEventV1.model_validate(data)
