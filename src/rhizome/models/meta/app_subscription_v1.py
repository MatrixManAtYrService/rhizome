"""
SQLModel definition for the app_subscription table, version 1.

This module provides the V1 implementation of the AppSubscription model.
Currently, AppSubscriptionV1 is identical to the base AppSubscription class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .app_subscription import AppSubscription


class AppSubscriptionV1(AppSubscription, MetaSQLModel, table=True):
    """
    Version 1 of the AppSubscription model.

    Currently a name-only inheritance from the base AppSubscription class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_subscription"  # type: ignore

    def sanitize(self) -> AppSubscriptionV1:
        """Return a sanitized copy of this AppSubscriptionV1 instance."""
        return AppSubscriptionV1(
            created_time=self.created_time,
            deleted_time=self.deleted_time,
            developer_app_id=self.developer_app_id,
            id=self.id,
            label=self.label,
            modified_time=self.modified_time,
            plan=self.plan,
            uuid=self.uuid,
        )
