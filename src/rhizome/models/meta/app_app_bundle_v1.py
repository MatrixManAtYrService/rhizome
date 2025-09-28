"""
SQLModel definition for the app_app_bundle table, version 1.

This module provides the V1 implementation of the AppAppBundle model.
Currently, AppAppBundleV1 is identical to the base AppAppBundle class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .app_app_bundle import AppAppBundle


class AppAppBundleV1(AppAppBundle, MetaSQLModel, table=True):
    """
    Version 1 of the AppAppBundle model.

    Currently a name-only inheritance from the base AppAppBundle class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_app_bundle"

    def sanitize(self) -> AppAppBundleV1:
        """Return a sanitized copy of this AppAppBundleV1 instance."""
        return AppAppBundleV1(
            allow_uninstall=self.allow_uninstall,
            app_bundle_id=self.app_bundle_id,
            app_subscription_id=self.app_subscription_id,
            charge=self.charge,
            developer_app_id=self.developer_app_id,
            id=self.id,
        )
