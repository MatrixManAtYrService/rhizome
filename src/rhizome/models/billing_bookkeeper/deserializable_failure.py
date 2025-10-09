"""
SQLModel definition for the deserializable_failure table.

This module provides the SQLModel class for the deserializable_failure table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class DeserializableFailure(RhizomeModel, table=False):
    """
    SQLModel for the `deserializable_failure` table.

    This model represents deserializable failure records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=36, unique=True, description="Uuid")
    topic: str = Field(max_length=127, description="Topic")
    channel: str = Field(max_length=127, description="Channel")
    b64: str = Field(description="B64")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> DeserializableFailure:
        """Return a sanitized copy of this DeserializableFailure instance."""
        return DeserializableFailure(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            topic=self.topic,
            channel=self.channel,
            b64=self.b64,
            created_timestamp=self.created_timestamp,
        )
