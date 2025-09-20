"""
Expected data for producer_failure_history table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.producer_failure_history_v1 import ProducerFailureHistoryV1


class ProducerFailureHistoryDev(Emplacement[ProducerFailureHistoryV1]):
    """Expected data for ProducerFailureHistory in dev environment."""

    @classmethod
    def get_expected(cls) -> ProducerFailureHistoryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_producer_failure_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ProducerFailureHistoryV1.model_validate(data)
