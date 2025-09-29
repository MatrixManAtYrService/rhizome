"""
SQLModel definition for the stage_merchant_plan_charge table.

This module provides the SQLModel class for the stage_merchant_plan_charge table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageMerchantPlanCharge(RhizomeModel, table=False):
    """
    SQLModel for the `stage_merchant_plan_charge` table.

    This model represents stage_merchant_plan_charge records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    num_of_devices: int = Field(description="num_of_devices")
    merchant_plan_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    plan_charge_type: str | None = Field(default=None, description="plan_charge_type")
    request_uuid: str | None = Field(default=None, description="UUID field")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    device_type_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageMerchantPlanCharge:
        """Return a sanitized copy of this StageMerchantPlanCharge instance."""
        return StageMerchantPlanCharge(
            id=self.id,
            merchant_id=self.merchant_id,
            charge_id=self.charge_id,
            created_time=self.created_time,
            modified_time=self.modified_time,
            num_of_devices=self.num_of_devices,
            merchant_plan_id=self.merchant_plan_id,
            plan_charge_type=self.plan_charge_type,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
            device_type_id=self.device_type_id,
        )
