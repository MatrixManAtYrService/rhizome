"""
SQLModel definition for the server_feature table, version 1.

This module provides the V1 implementation of the ServerFeature model.
Currently, ServerFeatureV1 is identical to the base ServerFeature class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .server_feature import ServerFeature


class ServerFeatureV1(ServerFeature, MetaSQLModel, table=True):
    """
    Version 1 of the ServerFeature model.

    Currently a name-only inheritance from the base ServerFeature class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "server_feature"  # type: ignore

    def sanitize(self) -> ServerFeatureV1:
        """Return a sanitized copy of this ServerFeatureV1 instance."""
        return ServerFeatureV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            name=self.name,
            config=self.config,
            enabled=self.enabled,
            modified_time=self.modified_time,
            deleted_time=self.deleted_time,
        )
