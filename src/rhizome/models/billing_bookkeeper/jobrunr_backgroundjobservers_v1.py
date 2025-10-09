"""
SQLModel definition for the jobrunr_backgroundjobservers table, version 1.

This module provides the V1 implementation of the JobrunrBackgroundjobservers model.
"""

from __future__ import annotations

from .jobrunr_backgroundjobservers import JobrunrBackgroundjobservers


class JobrunrBackgroundjobserversV1(JobrunrBackgroundjobservers, table=True):
    """
    Version 1 of the JobrunrBackgroundjobservers model.

    Currently a name-only inheritance from the base JobrunrBackgroundjobservers class.
    """

    __tablename__ = "jobrunr_backgroundjobservers"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
