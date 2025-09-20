"""
Expected data for job_assassination_contract table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.job_assassination_contract_v1 import JobAssassinationContractV1


class JobAssassinationContractDev(Emplacement[JobAssassinationContractV1]):
    """Expected data for JobAssassinationContract in dev environment."""

    @classmethod
    def get_expected(cls) -> JobAssassinationContractV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_job_assassination_contract.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return JobAssassinationContractV1.model_validate(data)