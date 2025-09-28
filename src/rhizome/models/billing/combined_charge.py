"""
SQLModel definition for the combined_charge table.

This module provides the SQLModel class for the combined_charge table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CombinedCharge(RhizomeModel, table=False):
    """
    SQLModel for the `combined_charge` table.

    This model represents combined_charge records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> CombinedCharge:
        """Return a sanitized copy of this CombinedCharge instance."""
        return CombinedCharge(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            created_time=self.created_time,
        )
