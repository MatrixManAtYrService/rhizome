"""
SQLModel definition for the stage_charge_history table.

This module provides the SQLModel class for the stage_charge_history table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageChargeHistory(RhizomeModel, table=False):
    """
    SQLModel for the `stage_charge_history` table.

    This model represents stage_charge_history records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    old_status: str | None = Field(default=None, description="old_status")
    old_developer_status: str | None = Field(default=None, description="old_developer_status")
    old_status_owner: str = Field(max_length=30, description="old_status_owner")
    old_modified_time: datetime.datetime | None = Field(default=None, description="old_modified_time")
    created_time: datetime.datetime = Field(description="created_time")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageChargeHistory:
        """Return a sanitized copy of this StageChargeHistory instance."""
        return StageChargeHistory(
            id=self.id,
            charge_id=self.charge_id,
            old_status=self.old_status,
            old_developer_status=self.old_developer_status,
            old_status_owner=self.old_status_owner,
            old_modified_time=self.old_modified_time,
            created_time=self.created_time,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
