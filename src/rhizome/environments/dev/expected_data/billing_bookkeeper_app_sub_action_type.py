"""Expected data for app_sub_action_type table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.app_sub_action_type_v1 import AppSubActionTypeV1


class AppSubActionTypeDev(Emplacement[AppSubActionTypeV1]):
    """Expected data for AppSubActionType in dev environment."""

    @classmethod
    def get_expected(cls) -> AppSubActionTypeV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_app_sub_action_type.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AppSubActionTypeV1.model_validate(data)
