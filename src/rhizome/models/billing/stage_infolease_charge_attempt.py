"""
SQLModel definition for the stage_infolease_charge_attempt table.

This module provides the SQLModel class for the stage_infolease_charge_attempt table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageInfoleaseChargeAttempt(RhizomeModel, table=False):
    """
    SQLModel for the `stage_infolease_charge_attempt` table.

    This model represents stage_infolease_charge_attempt records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    status: str | None = Field(default=None, description="status")
    payment_type: str = Field(max_length=10, description="payment_type")
    infolease_key: str | None = Field(default=None, max_length=20, description="infolease_key")
    contract_number: str | None = Field(default=None, max_length=30, description="contract_number")
    gl_code: str | None = Field(default=None, max_length=10, description="gl_code")
    tax: int = Field(description="tax")
    post_date: str | None = Field(default=None, max_length=10, description="post_date")
    post_time: str | None = Field(default=None, max_length=10, description="post_time")
    created_time: datetime.datetime | None = Field(default=None, description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    request_uuid: str | None = Field(default=None, description="UUID field")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageInfoleaseChargeAttempt:
        """Return a sanitized copy of this StageInfoleaseChargeAttempt instance."""
        return StageInfoleaseChargeAttempt(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            charge_id=self.charge_id,
            status=self.status,
            payment_type=self.payment_type,
            infolease_key=self.infolease_key,
            contract_number=self.contract_number,
            gl_code=self.gl_code,
            tax=self.tax,
            post_date=self.post_date,
            post_time=self.post_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
