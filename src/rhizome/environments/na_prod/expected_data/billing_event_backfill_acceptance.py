"""
Expected data for backfill_acceptance table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.backfill_acceptance_v1 import BackfillAcceptanceV1


class BackfillAcceptanceNaProd(Emplacement[BackfillAcceptanceV1]):
    """Expected data for BackfillAcceptance in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BackfillAcceptanceV1:
        """Get expected backfill acceptance data for na_prod environment."""
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
