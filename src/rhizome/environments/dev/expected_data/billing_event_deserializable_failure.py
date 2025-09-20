"""
Expected data for deserializable_failure table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.deserializable_failure_v1 import DeserializableFailureV1


class DeserializableFailureDev(Emplacement[DeserializableFailureV1]):
    """Expected data for DeserializableFailure in dev environment."""

    @classmethod
    def get_expected(cls) -> DeserializableFailureV1:
        """Get expected deserializable failure data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_deserializable_failure.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return DeserializableFailureV1.model_validate(data)