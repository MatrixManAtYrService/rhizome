"""
Expected data for managed_item table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.managed_item_v1 import ManagedItemV1


class ManagedItemDev(Emplacement[ManagedItemV1]):
    """Expected data for ManagedItem in dev environment."""

    @classmethod
    def get_expected(cls) -> ManagedItemV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_managed_item.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ManagedItemV1.model_validate(data)
