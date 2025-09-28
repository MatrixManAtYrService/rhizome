"""
SQLModel definition for the device_provision table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="DeviceProvision")


class DeviceProvision(RhizomeModel, table=True):
    """
    SQLModel for the `device_provision` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    serial_number: str = Field(max_length=16, unique=True)
    chip_uid: str | None = Field(default=None, max_length=32)
    imei: str | None = Field(default=None, max_length=15)
    provision_info: str | None = Field(default=None)
    last_activation_code: str | None = Field(default=None, max_length=8)
    activation_code: str = Field(max_length=8)
    activation_code_created_time: datetime.datetime | None = Field(default=None)
    deauthorization_code: str | None = Field(default=None, max_length=8)
    deauthorization_attempts: int | None = Field(default=0)
    merchant_id: int | None = Field(default=None, foreign_key="merchant.id")
    reseller_id: int | None = Field(default=None, foreign_key="reseller.id")
    email_sent: bool | None = Field(default=False)
    sms_sent: bool | None = Field(default=False)
    order_type: str | None = Field(default=None, max_length=4)
    provisioned_time: datetime.datetime | None = Field(default=None)
    activated_time: datetime.datetime | None = Field(default=None)
    terminal_id: str | None = Field(default=None, max_length=8)
    deleted_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    shipping_status: str | None = Field(default=None, max_length=24)
    tasq_order_number: str | None = Field(default=None, max_length=50)
    next_calltag_notify_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this DeviceProvision instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
