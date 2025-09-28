"""
SQLModel definition for the stage_merchant_app_charge table.

This module provides the SQLModel class for the stage_merchant_app_charge table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageMerchantAppCharge(RhizomeModel, table=False):
    """
    SQLModel for the `stage_merchant_app_charge` table.

    This model represents stage_merchant_app_charge records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_app_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    app_subscription_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime | None = Field(default=None, description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    developer_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    app_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageMerchantAppCharge:
        """Return a sanitized copy of this StageMerchantAppCharge instance."""
        return StageMerchantAppCharge(
            id=self.id,
            merchant_app_id=self.merchant_app_id,
            app_subscription_id=self.app_subscription_id,
            charge_id=self.charge_id,
            created_time=self.created_time,
            modified_time=self.modified_time,
            merchant_id=self.merchant_id,
            developer_id=self.developer_id,
            app_id=self.app_id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
