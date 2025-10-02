"""
SQLModel definition for the app_permission table, version 1.

This module provides the V1 implementation of the AppPermission model.
Currently, AppPermissionV1 is identical to the base AppPermission class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .app_permission import AppPermission


class AppPermissionV1(AppPermission, MetaSQLModel, table=True):
    """
    Version 1 of the AppPermission model.

    Currently a name-only inheritance from the base AppPermission class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_permission"  # type: ignore

    def sanitize(self) -> AppPermissionV1:
        """Return a sanitized copy of this AppPermissionV1 instance."""
        return AppPermissionV1(
            created_time=self.created_time,
            id=self.id,
            modified_time=self.modified_time,
            name=self.name,
        )
