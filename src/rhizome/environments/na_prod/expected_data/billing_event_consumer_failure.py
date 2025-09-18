"""
Expected data for consumer_failure table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.consumer_failure_v1 import ConsumerFailureV1


class ConsumerFailureNaProd(Emplacement[ConsumerFailureV1]):
    """Expected data for ConsumerFailure in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ConsumerFailureV1:
        """Get expected consumer failure data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_consumer_failure.json"
        with open(file_path) as f:
            data = json.load(f)
        return ConsumerFailureV1.model_validate(data)