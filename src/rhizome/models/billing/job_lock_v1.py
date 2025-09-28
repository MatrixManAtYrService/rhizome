"""
SQLModel definition for the job_lock table, version 1.

This module provides the V1 implementation of the JobLock model.
Currently, JobLockV1 is identical to the base JobLock class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .job_lock import JobLock


class JobLockV1(JobLock, NaProdSQLModel, table=True):
    """
    Version 1 of the JobLock model.

    Currently a name-only inheritance from the base JobLock class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "job_lock"  # type: ignore
