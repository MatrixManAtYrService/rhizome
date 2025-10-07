"""
SQLModel definition for the app_bundle table, version 1.

This module provides the V1 implementation of the AppBundle model.
Currently, AppBundleV1 is identical to the base AppBundle class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .app_bundle import AppBundle


class AppBundleV1(AppBundle, MetaSQLModel, table=True):
    """
    Version 1 of the AppBundle model.

    Currently a name-only inheritance from the base AppBundle class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_bundle"  # type: ignore

    def sanitize(self) -> AppBundleV1:
        """Return a sanitized copy of this AppBundleV1 instance."""
        return AppBundleV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            name=self.name,
        )
