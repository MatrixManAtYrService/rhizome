"""
SQLModel definition for the jobrunr_jobs table, version 1.

This module provides the V1 implementation of the JobrunrJobs model.
"""

from __future__ import annotations

from .jobrunr_jobs import JobrunrJobs


class JobrunrJobsV1(JobrunrJobs, table=True):
    """
    Version 1 of the JobrunrJobs model.

    Currently a name-only inheritance from the base JobrunrJobs class.
    """

    __tablename__ = "jobrunr_jobs"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
