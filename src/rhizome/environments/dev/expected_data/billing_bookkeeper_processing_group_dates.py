"""Expected data for processing_group_dates table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.processing_group_dates_v1 import ProcessingGroupDatesV1


class ProcessingGroupDatesDev(Emplacement[ProcessingGroupDatesV1]):
    """Expected data for ProcessingGroupDates in dev environment."""

    @classmethod
    def get_expected(cls) -> ProcessingGroupDatesV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_processing_group_dates.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ProcessingGroupDatesV1.model_validate(data)
