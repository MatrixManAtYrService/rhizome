"""
Expected data for mlc_captured_event table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.mlc_captured_event_v1 import MlcCapturedEventV1


class MlcCapturedEventDev(Emplacement[MlcCapturedEventV1]):
    """Expected data for MlcCapturedEvent in dev environment."""

    @classmethod
    def get_expected(cls) -> MlcCapturedEventV1:
        """Get expected mlc_captured_event data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_mlc_captured_event.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MlcCapturedEventV1.model_validate(data)
