"""
SQLModel definition for the rev_share table.

This module provides the SQLModel class for the rev_share table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class RevShare(RhizomeModel, table=False):
    """
    SQLModel for the `rev_share` table.

    This model represents rev_share records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    developer: int | None = Field(default=None, description="developer")
    partner: int | None = Field(default=None, description="partner")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> RevShare:
        """Return a sanitized copy of this RevShare instance."""
        return RevShare(
            id=self.id,
            charge_uuid=sanitize_uuid_field(self.charge_uuid, 13),
            developer=self.developer,
            partner=self.partner,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
