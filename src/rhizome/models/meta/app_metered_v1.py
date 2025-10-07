"""
SQLModel definition for the app_metered table, version 1.

This module provides the V1 implementation of the AppMetered model.
Currently, AppMeteredV1 is identical to the base AppMetered class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .app_metered import AppMetered


class AppMeteredV1(AppMetered, MetaSQLModel, table=True):
    """
    Version 1 of the AppMetered model.

    Currently a name-only inheritance from the base AppMetered class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_metered"  # type: ignore

    def sanitize(self) -> AppMeteredV1:
        """Return a sanitized copy of this AppMeteredV1 instance."""
        return AppMeteredV1(
            created_time=self.created_time,
            deleted_time=self.deleted_time,
            developer_app_id=self.developer_app_id,
            id=self.id,
            label=self.label,
            modified_time=self.modified_time,
            uuid=self.uuid,
        )
