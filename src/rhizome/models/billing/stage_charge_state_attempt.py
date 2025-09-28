"""
SQLModel definition for the stage_charge_state_attempt table.

This module provides the SQLModel class for the stage_charge_state_attempt table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageChargeStateAttempt(RhizomeModel, table=False):
    """
    SQLModel for the `stage_charge_state_attempt` table.

    This model represents stage_charge_state_attempt records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    state: str | None = Field(default=None, description="state")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageChargeStateAttempt:
        """Return a sanitized copy of this StageChargeStateAttempt instance."""
        return StageChargeStateAttempt(
            id=self.id,
            charge_id=self.charge_id,
            state=self.state,
            created_time=self.created_time,
            modified_time=self.modified_time,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
