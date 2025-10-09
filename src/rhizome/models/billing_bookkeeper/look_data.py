"""
SQLModel definition for the look_data table.

This module provides the SQLModel class for the look_data table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LookData(RhizomeModel, table=False):
    """
    SQLModel for the `look_data` table.

    This model represents look data records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    look_uuid: str = Field(max_length=32, description="Look Uuid")
    payload: str = Field(description="Payload")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> LookData:
        """Return a sanitized copy of this LookData instance."""
        return LookData(
            id=self.id,
            look_uuid=sanitize_uuid_field(self.look_uuid, 32),  # type: ignore
            payload=self.payload,
            created_timestamp=self.created_timestamp,
        )
