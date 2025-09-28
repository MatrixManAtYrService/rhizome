"""
SQLModel definition for the export_tracker table, version 1.

This module provides the V1 implementation of the ExportTracker model.
Currently, ExportTrackerV1 is identical to the base ExportTracker class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .export_tracker import ExportTracker


class ExportTrackerV1(ExportTracker, NaProdSQLModel, table=True):
    """
    Version 1 of the ExportTracker model.

    Currently a name-only inheritance from the base ExportTracker class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "export_tracker"  # type: ignore
