"""
Expected data for producer_failure table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.producer_failure_v1 import ProducerFailureV1


class ProducerFailureDemo(Emplacement[ProducerFailureV1]):
    """Expected data for ProducerFailure in demo environment."""

    @classmethod
    def get_expected(cls) -> ProducerFailureV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_producer_failure.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ProducerFailureV1.model_validate(data)
