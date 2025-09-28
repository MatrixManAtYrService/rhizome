"""
SQLModel definition for the merchant_device_info table.

This module provides the SQLModel class for the merchant_device_info table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class MerchantDeviceInfo(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_device_info` table.

    This model represents merchant_device_info records in the billing system.
    """

    merchant_id: int = Field(primary_key=True, description="merchant_id")
    device_id: int = Field(primary_key=True, description="device_id")
    terminal_id: str = Field(primary_key=True, max_length=16, description="terminal_id")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> MerchantDeviceInfo:
        """Return a sanitized copy of this MerchantDeviceInfo instance."""
        return MerchantDeviceInfo(
            merchant_id=self.merchant_id,
            device_id=self.device_id,
            terminal_id=self.terminal_id,
            modified_time=self.modified_time,
        )
