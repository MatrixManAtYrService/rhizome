"""
SQLModel definition for the app_subscription_country table, version 1.

This module provides the V1 implementation of the AppSubscriptionCountry model.
Currently, AppSubscriptionCountryV1 is identical to the base AppSubscriptionCountry class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .app_subscription_country import AppSubscriptionCountry


class AppSubscriptionCountryV1(AppSubscriptionCountry, MetaSQLModel, table=True):
    """
    Version 1 of the AppSubscriptionCountry model.

    Currently a name-only inheritance from the base AppSubscriptionCountry class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_subscription_country"  # type: ignore

    def sanitize(self) -> AppSubscriptionCountryV1:
        """Return a sanitized copy of this AppSubscriptionCountryV1 instance."""
        return AppSubscriptionCountryV1(
            active=self.active,
            amount=self.amount,
            app_subscription_id=self.app_subscription_id,
            country=self.country,
            created_time=self.created_time,
            deleted_time=self.deleted_time,
            description=self.description,
            id=self.id,
            modified_time=self.modified_time,
            name=self.name,
            uuid=self.uuid,
        )
