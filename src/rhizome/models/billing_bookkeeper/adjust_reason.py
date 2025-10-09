"""
SQLModel definition for the adjust_reason table.

This module provides the SQLModel class for the adjust_reason table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AdjustReason(RhizomeModel, table=False):
    """
    SQLModel for the `adjust_reason` table.

    This model represents adjust reason records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    adjust_reason: str = Field(max_length=25, description="Adjust Reason")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> AdjustReason:
        """Return a sanitized copy of this AdjustReason instance."""
        return AdjustReason(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            adjust_reason=self.adjust_reason,
            created_timestamp=self.created_timestamp,
        )
