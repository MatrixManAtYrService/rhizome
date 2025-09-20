"""
Expected data for jobrunr_backgroundjobservers table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1


class JobrunrBackgroundjobserversDev(Emplacement[JobrunrBackgroundjobserversV1]):
    """Expected data for JobrunrBackgroundjobservers in dev environment."""

    @classmethod
    def get_expected(cls) -> JobrunrBackgroundjobserversV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_jobrunr_backgroundjobservers.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return JobrunrBackgroundjobserversV1.model_validate(data)
