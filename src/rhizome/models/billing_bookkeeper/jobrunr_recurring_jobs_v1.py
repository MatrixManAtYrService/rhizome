"""
SQLModel definition for the jobrunr_recurring_jobs table, version 1.

This module provides the V1 implementation of the JobrunrRecurringJobs model.
"""

from __future__ import annotations

from .jobrunr_recurring_jobs import JobrunrRecurringJobs


class JobrunrRecurringJobsV1(JobrunrRecurringJobs, table=True):
    """
    Version 1 of the JobrunrRecurringJobs model.

    Currently a name-only inheritance from the base JobrunrRecurringJobs class.
    """

    __tablename__ = "jobrunr_recurring_jobs"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
