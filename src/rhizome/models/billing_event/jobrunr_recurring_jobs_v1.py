"""
SQLModel definition for the jobrunr_recurring_jobs table, version 1.

This module provides the V1 implementation of the JobrunrRecurringJobs model.
Currently, JobrunrRecurringJobsV1 is identical to the base JobrunrRecurringJobs class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .jobrunr_recurring_jobs import JobrunrRecurringJobs


class JobrunrRecurringJobsV1(JobrunrRecurringJobs, table=True):
    """
    Version 1 of the JobrunrRecurringJobs model.

    Currently a name-only inheritance from the base JobrunrRecurringJobs class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "jobrunr_recurring_jobs"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
