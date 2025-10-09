"""
SQLModel definition for the misc_action_type table.

This module provides the SQLModel class for the misc_action_type table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MiscActionType(RhizomeModel, table=False):
    """
    SQLModel for the `misc_action_type` table.

    This model represents misc action type records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    misc_action_type: str = Field(max_length=25, description="Misc Action Type")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> MiscActionType:
        """Return a sanitized copy of this MiscActionType instance."""
        return MiscActionType(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            misc_action_type=self.misc_action_type,
            created_timestamp=self.created_timestamp,
        )
