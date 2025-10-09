"""Expected data for app_meter_action table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.app_meter_action_v1 import AppMeterActionV1


class AppMeterActionDemo(Emplacement[AppMeterActionV1]):
    """Expected data for AppMeterAction in demo environment."""

    @classmethod
    def get_expected(cls) -> AppMeterActionV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_app_meter_action.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AppMeterActionV1.model_validate(data)
