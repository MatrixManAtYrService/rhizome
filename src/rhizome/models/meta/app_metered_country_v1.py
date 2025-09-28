"""
SQLModel definition for the app_metered_country table, version 1.

This module provides the V1 implementation of the AppMeteredCountry model.
Currently, AppMeteredCountryV1 is identical to the base AppMeteredCountry class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .app_metered_country import AppMeteredCountry


class AppMeteredCountryV1(AppMeteredCountry, MetaSQLModel, table=True):
    """
    Version 1 of the AppMeteredCountry model.

    Currently a name-only inheritance from the base AppMeteredCountry class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_metered_country"

    def sanitize(self) -> AppMeteredCountryV1:
        """Return a sanitized copy of this AppMeteredCountryV1 instance."""
        return AppMeteredCountryV1(
            action=self.action,
            active=self.active,
            amount=self.amount,
            app_metered_id=self.app_metered_id,
            country=self.country,
            created_time=self.created_time,
            deleted_time=self.deleted_time,
            id=self.id,
            modified_time=self.modified_time,
            uuid=self.uuid,
        )
