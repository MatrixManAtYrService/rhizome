"""
SQLModel definition for the app_metered_event table, version 1.

This module provides the V1 implementation of the AppMeteredEvent model.
Currently, AppMeteredEventV1 is identical to the base AppMeteredEvent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from ...sanitize_helpers import sanitize_uuid_field
from .app_metered_event import AppMeteredEvent


class AppMeteredEventV1(AppMeteredEvent, MetaSQLModel, table=True):
    """
    Version 1 of the AppMeteredEvent model.

    Currently a name-only inheritance from the base AppMeteredEvent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_metered_event"

    def sanitize(self) -> AppMeteredEventV1:
        """Return a sanitized copy of this AppMeteredEventV1 instance."""
        return AppMeteredEventV1(
            app_metered_id=self.app_metered_id,
            charge_id=self.charge_id,
            count=self.count,
            created_time=self.created_time,
            id=self.id,
            merchant_app_id=self.merchant_app_id,
            modified_time=self.modified_time,
            uuid=self.uuid,
        )
