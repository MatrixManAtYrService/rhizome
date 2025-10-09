"""Expected data for adjust_reason table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.adjust_reason_v1 import AdjustReasonV1


class AdjustReasonDev(Emplacement[AdjustReasonV1]):
    """Expected data for AdjustReason in dev environment."""

    @classmethod
    def get_expected(cls) -> AdjustReasonV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_adjust_reason.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AdjustReasonV1.model_validate(data)
