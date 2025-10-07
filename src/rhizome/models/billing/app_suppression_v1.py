"""
SQLModel definition for the app_suppression table, version 1.

This module provides the V1 implementation of the AppSuppression model.
Currently, AppSuppressionV1 is identical to the base AppSuppression class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .app_suppression import AppSuppression


class AppSuppressionV1(AppSuppression, NaProdSQLModel, table=True):
    """
    Version 1 of the AppSuppression model.

    Currently a name-only inheritance from the base AppSuppression class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_suppression"  # type: ignore
