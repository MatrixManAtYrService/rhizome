"""
Expected data for consumer_failure table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.consumer_failure_v1 import ConsumerFailureV1


class ConsumerFailureDev(Emplacement[ConsumerFailureV1]):
    """Expected data for ConsumerFailure in dev environment."""

    @classmethod
    def get_expected(cls) -> ConsumerFailureV1:
        """Get expected consumer failure data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_consumer_failure.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ConsumerFailureV1.model_validate(data)
