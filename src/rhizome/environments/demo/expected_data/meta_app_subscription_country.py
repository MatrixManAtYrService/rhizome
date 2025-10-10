"""
Expected data for app_subscription_country table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.app_subscription_country_v1 import AppSubscriptionCountryV1


class AppSubscriptionCountryDemo(Emplacement[AppSubscriptionCountryV1]):
    """Expected data for AppSubscriptionCountry in demo environment."""

    @classmethod
    def get_expected(cls) -> AppSubscriptionCountryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_app_subscription_country.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AppSubscriptionCountryV1.model_validate(data)
