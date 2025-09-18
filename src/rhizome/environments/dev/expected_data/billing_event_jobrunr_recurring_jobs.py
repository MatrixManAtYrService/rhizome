"""
Expected data for jobrunr_recurring_jobs table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_recurring_jobs_v1 import JobrunrRecurringJobsV1


class JobrunrRecurringJobsDev(Emplacement[JobrunrRecurringJobsV1]):
    """Expected data for JobrunrRecurringJobs in dev environment."""

    @classmethod
    def get_expected(cls) -> JobrunrRecurringJobsV1:
        """Get expected jobrunr_recurring_jobs data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
