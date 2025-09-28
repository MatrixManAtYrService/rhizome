"""
SQLModel definition for the device_order_tracking table.

This module provides the SQLModel class for the device_order_tracking table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class DeviceOrderTracking(RhizomeModel, table=False):
    """
    SQLModel for the `device_order_tracking` table.

    This model represents device_order_tracking records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    order_month: datetime.date = Field(description="order_month")
    serial_number: str = Field(max_length=16, description="serial_number")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    activity: str | None = Field(default=None, description="activity")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> DeviceOrderTracking:
        """Return a sanitized copy of this DeviceOrderTracking instance."""
        return DeviceOrderTracking(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            order_month=self.order_month,
            serial_number=self.serial_number,
            merchant_id=self.merchant_id,
            activity=self.activity,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
