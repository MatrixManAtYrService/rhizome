"""
Expected data for jobrunr_recurring_jobs table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_recurring_jobs_v1 import JobrunrRecurringJobsV1


class JobrunrRecurringJobsNaProd(Emplacement[JobrunrRecurringJobsV1]):
    """Expected data for JobrunrRecurringJobs in na_prod environment."""

    @classmethod
    def get_expected(cls) -> JobrunrRecurringJobsV1:
        """Get expected jobrunr_recurring_jobs data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
