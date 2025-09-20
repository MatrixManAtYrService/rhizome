"""
Expected data for look_data table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.look_data_v1 import LookDataV1


class LookDataDemo(Emplacement[LookDataV1]):
    """Expected data for LookData in demo environment."""

    @classmethod
    def get_expected(cls) -> LookDataV1:
        """Get expected look_data data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_look_data.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return LookDataV1.model_validate(data)
