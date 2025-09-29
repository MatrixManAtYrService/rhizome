"""
SQLModel definition for the stage_app_metered_event table.

This module provides the SQLModel class for the stage_app_metered_event table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageAppMeteredEvent(RhizomeModel, table=False):
    """
    SQLModel for the `stage_app_metered_event` table.

    This model represents stage_app_metered_event records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    app_metered_event_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    stage_charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> StageAppMeteredEvent:
        """Return a sanitized copy of this StageAppMeteredEvent instance."""
        return StageAppMeteredEvent(
            id=self.id,
            app_metered_event_id=self.app_metered_event_id,
            stage_charge_id=self.stage_charge_id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            merchant_id=self.merchant_id,
            promoted_time=self.promoted_time,
            created_time=self.created_time,
        )
