"""
Expected data for billing_event_history table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.billing_event_history_v1 import BillingEventHistoryV1


class BillingEventHistoryDev(Emplacement[BillingEventHistoryV1]):
    """Expected data for BillingEventHistory in dev environment."""

    @classmethod
    def get_expected(cls) -> BillingEventHistoryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_billing_event_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return BillingEventHistoryV1.model_validate(data)