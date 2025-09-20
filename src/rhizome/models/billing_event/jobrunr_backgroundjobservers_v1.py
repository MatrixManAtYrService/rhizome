"""
SQLModel definition for the jobrunr_backgroundjobservers table, version 1.

This module provides the V1 implementation of the JobrunrBackgroundjobservers model.
Currently, JobrunrBackgroundjobserversV1 is identical to the base JobrunrBackgroundjobservers class
(name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .jobrunr_backgroundjobservers import JobrunrBackgroundjobservers


class JobrunrBackgroundjobserversV1(JobrunrBackgroundjobservers, table=True):
    """
    Version 1 of the JobrunrBackgroundjobservers model.

    Currently a name-only inheritance from the base JobrunrBackgroundjobservers class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "jobrunr_backgroundjobservers"  # type: ignore
