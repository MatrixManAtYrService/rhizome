"""
Expected data for jobrunr_jobs table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_jobs_v1 import JobrunrJobsV1


class JobrunrJobsDemo(Emplacement[JobrunrJobsV1]):
    """Expected data for JobrunrJobs in demo environment."""

    @classmethod
    def get_expected(cls) -> JobrunrJobsV1:
        """Get expected jobrunr jobs data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )