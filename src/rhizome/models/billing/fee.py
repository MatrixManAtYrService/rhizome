"""
SQLModel definition for the fee table.

This module provides the SQLModel class for the fee table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeType(str, Enum):
    """Enum for fee type values."""

    SETUP = "SETUP"
    MONTHLY = "MONTHLY"


class FeeStatus(str, Enum):
    """Enum for fee status values."""

    PENDING = "PENDING"
    PENDING_EXCEPT = "PENDING_EXCEPT"
    IN_PROGRESS = "IN_PROGRESS"
    BILLED = "BILLED"
    CANCELED = "CANCELED"
    EXCEPTED = "EXCEPTED"
    WAIVED = "WAIVED"
    FAILED_TO_BILL = "FAILED_TO_BILL"
    EXPORTED = "EXPORTED"


class Fee(RhizomeModel, table=False):
    """
    SQLModel for the `fee` table.

    This model represents fee records in the billing system,
    containing fee information for merchants and their plans.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True, description="Unique identifier for the fee")
    merchant_id: int = Field(description="ID of the merchant")
    merchant_plan_id: int = Field(description="ID of the merchant plan")
    merchant_plan_type: str | None = Field(default=None, max_length=20, description="Type of merchant plan")
    merchant_plan_group_id: int | None = Field(default=None, description="ID of the merchant plan group")
    fee_type: FeeType = Field(description="Type of fee")
    currency: str = Field(max_length=3, description="Currency code (ISO 4217)")
    amount: int = Field(description="Fee amount in smallest currency unit")
    status: FeeStatus = Field(description="Current status of the fee")
    export_month: datetime.date | None = Field(default=None, description="Month for export processing")
    request_uuid: str = Field(max_length=13, description="UUID of the request that generated this fee")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")
    reason: str | None = Field(default=None, max_length=100, description="Reason for the fee status")

    def sanitize(self) -> Fee:
        """Return a sanitized copy of this Fee instance."""
        return Fee(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            merchant_id=self.merchant_id,
            merchant_plan_id=self.merchant_plan_id,
            merchant_plan_type=self.merchant_plan_type,
            merchant_plan_group_id=self.merchant_plan_group_id,
            fee_type=self.fee_type,
            currency=self.currency,
            amount=self.amount,
            status=self.status,
            export_month=self.export_month,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            created_time=self.created_time,
            modified_time=self.modified_time,
            reason=self.reason,
        )