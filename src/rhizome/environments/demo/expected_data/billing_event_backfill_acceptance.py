"""
Expected data for backfill_acceptance table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.backfill_acceptance_v1 import BackfillAcceptanceV1


class BackfillAcceptanceDemo(Emplacement[BackfillAcceptanceV1]):
    """Expected data for BackfillAcceptance in demo environment."""

    @classmethod
    def get_expected(cls) -> BackfillAcceptanceV1:
        """Get expected backfill acceptance data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_backfill_acceptance.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BackfillAcceptanceV1.model_validate(data)
