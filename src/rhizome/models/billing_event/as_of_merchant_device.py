"""
SQLModel definition for the as_of_merchant_device table.

This module provides the SQLModel class for the as_of_merchant_device table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AsOfMerchantDevice(RhizomeModel, table=False):
    """
    SQLModel for the `as_of_merchant_device` table.

    This model represents device information associated with merchant snapshots,
    tracking device details at specific points in time.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the as-of-merchant-device record")
    as_of_merchant_uuid: str = Field(max_length=26, description="UUID of the associated as-of-merchant record")
    serial_number: str = Field(max_length=32, description="Serial number of the device")
    device_type: str | None = Field(default=None, max_length=25, description="Type of the device")
    bundle_indicator: str | None = Field(default=None, max_length=32, description="Bundle indicator for the device")
    modifier_1: str | None = Field(default=None, max_length=25, description="First modifier for the device")
    modifier_2: str | None = Field(default=None, max_length=25, description="Second modifier for the device")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> AsOfMerchantDevice:
        """Return a sanitized copy of this AsOfMerchantDevice instance."""
        return AsOfMerchantDevice(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            as_of_merchant_uuid=sanitize_uuid_field(self.as_of_merchant_uuid, 26),  # type: ignore
            serial_number=self.serial_number,
            device_type=self.device_type,
            bundle_indicator=self.bundle_indicator,
            modifier_1=self.modifier_1,
            modifier_2=self.modifier_2,
            created_timestamp=self.created_timestamp,
        )
