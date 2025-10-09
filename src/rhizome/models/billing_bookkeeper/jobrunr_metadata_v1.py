"""
SQLModel definition for the jobrunr_metadata table, version 1.

This module provides the V1 implementation of the JobrunrMetadata model.
"""

from __future__ import annotations

from .jobrunr_metadata import JobrunrMetadata


class JobrunrMetadataV1(JobrunrMetadata, table=True):
    """
    Version 1 of the JobrunrMetadata model.

    Currently a name-only inheritance from the base JobrunrMetadata class.
    """

    __tablename__ = "jobrunr_metadata"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
