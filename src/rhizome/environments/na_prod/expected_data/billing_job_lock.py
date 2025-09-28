"""
Expected data for job_lock table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.job_lock_v1 import JobLockV1


class JobLockNaProd(Emplacement[JobLockV1]):
    """Expected data for JobLock in na_prod environment."""

    @classmethod
    def get_expected(cls) -> JobLockV1:
        """Get expected job_lock data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_job_lock.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return JobLockV1.model_validate(data)
