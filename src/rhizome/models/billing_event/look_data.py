"""
SQLModel definition for the look_data table.

This module provides the SQLModel class for the look_data table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LookData(RhizomeModel, table=False):
    """
    SQLModel for the `look_data` table.

    This model represents data payloads associated with look entries,
    containing the actual content referenced by look table entries.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing unsigned integer")
    look_uuid: str = Field(max_length=32, description="UUID reference to the look table entry")
    payload: bytes = Field(description="Binary payload data")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> LookData:
        """Return a sanitized copy of this LookData instance."""
        return LookData(
            id=self.id,
            look_uuid=sanitize_uuid_field(self.look_uuid, 32),  # type: ignore
            payload=self.payload,
            created_timestamp=self.created_timestamp,
        )