"""
SQLModel definition for the jobrunr_metadata table, version 1.

This module provides the V1 implementation of the JobrunrMetadata model.
Currently, JobrunrMetadataV1 is identical to the base JobrunrMetadata class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .jobrunr_metadata import JobrunrMetadata


class JobrunrMetadataV1(JobrunrMetadata, table=True):
    """
    Version 1 of the JobrunrMetadata model.

    Currently a name-only inheritance from the base JobrunrMetadata class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "jobrunr_metadata"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
