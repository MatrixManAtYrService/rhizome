"""
Expected data for consumer_failure_history table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.consumer_failure_history_v1 import ConsumerFailureHistoryV1


class ConsumerFailureHistoryDev(Emplacement[ConsumerFailureHistoryV1]):
    """Expected data for ConsumerFailureHistory in dev environment."""

    @classmethod
    def get_expected(cls) -> ConsumerFailureHistoryV1:
        """Get expected consumer failure history data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_consumer_failure_history.json"
        with open(file_path) as f:
            data = json.load(f)
        return ConsumerFailureHistoryV1.model_validate(data)