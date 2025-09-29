"""
SQLModel definition for the stage_charge_update table.

This module provides the SQLModel class for the stage_charge_update table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageChargeUpdate(RhizomeModel, table=False):
    """
    SQLModel for the `stage_charge_update` table.

    This model represents stage_charge_update records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    status: str | None = Field(default=None, description="status")
    developer_status: str | None = Field(default=None, description="developer_status")
    tax: int | None = Field(default=None, description="tax")
    developer_portion: int | None = Field(default=None, description="developer_portion")
    status_owner: str = Field(max_length=30, description="status_owner")
    request_uuid: str | None = Field(default=None, description="UUID field")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")

    def sanitize(self) -> StageChargeUpdate:
        """Return a sanitized copy of this StageChargeUpdate instance."""
        return StageChargeUpdate(
            id=self.id,
            charge_id=self.charge_id,
            merchant_id=self.merchant_id,
            status=self.status,
            developer_status=self.developer_status,
            tax=self.tax,
            developer_portion=self.developer_portion,
            status_owner=self.status_owner,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
        )
