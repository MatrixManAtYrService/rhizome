"""
SQLModel definition for the jobrunr_jobs table, version 1.

This module provides the V1 implementation of the JobrunrJobs model.
Currently, JobrunrJobsV1 is identical to the base JobrunrJobs class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .jobrunr_jobs import JobrunrJobs


class JobrunrJobsV1(JobrunrJobs, table=True):
    """
    Version 1 of the JobrunrJobs model.

    Currently a name-only inheritance from the base JobrunrJobs class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "jobrunr_jobs"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
