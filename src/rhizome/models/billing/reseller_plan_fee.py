"""
SQLModel definition for the reseller_plan_fee table.

This module provides the SQLModel class for the reseller_plan_fee table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AmountTypeType(str, Enum):
    """Enum for amount_type values."""

    FLAT_RATE = "FLAT_RATE"


class ResellerPlanFee(RhizomeModel, table=False):
    """
    SQLModel for the `reseller_plan_fee` table.

    This model represents reseller_plan_fee records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    reseller_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_plan_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_plan_type: str | None = Field(default=None, max_length=20, description="merchant_plan_type")
    merchant_plan_group_id: int | None = Field(
        default=None, primary_key=True, description="Primary key, auto-incrementing"
    )
    fee_type: str | None = Field(default=None, description="fee_type")
    currency: str = Field(max_length=3, description="currency")
    amount: int = Field(description="amount")
    amount_type: AmountTypeType = Field(description="amount_type")
    effective_date: datetime.datetime = Field(description="effective_date")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    deleted_time: datetime.datetime | None = Field(default=None, description="deleted_time")

    def sanitize(self) -> ResellerPlanFee:
        """Return a sanitized copy of this ResellerPlanFee instance."""
        return ResellerPlanFee(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            reseller_id=self.reseller_id,
            merchant_plan_id=self.merchant_plan_id,
            merchant_plan_type=self.merchant_plan_type,
            merchant_plan_group_id=self.merchant_plan_group_id,
            fee_type=self.fee_type,
            currency=self.currency,
            amount=self.amount,
            amount_type=self.amount_type,
            effective_date=self.effective_date,
            created_time=self.created_time,
            modified_time=self.modified_time,
            deleted_time=self.deleted_time,
        )
