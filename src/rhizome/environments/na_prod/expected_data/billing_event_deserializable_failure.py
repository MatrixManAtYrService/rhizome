"""
Expected data for deserializable_failure table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.deserializable_failure_v1 import DeserializableFailureV1


class DeserializableFailureNaProd(Emplacement[DeserializableFailureV1]):
    """Expected data for DeserializableFailure in na_prod environment."""

    @classmethod
    def get_expected(cls) -> DeserializableFailureV1:
        """Get expected deserializable failure data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_deserializable_failure.json"
        with open(file_path) as f:
            data = json.load(f)
        return DeserializableFailureV1.model_validate(data)