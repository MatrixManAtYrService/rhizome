"""
SQLModel definition for the stage_charge table.

This module provides the SQLModel class for the stage_charge table from the
na-billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum
from typing import Literal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ChargeStatus(str, Enum):
    """Enum for charge status values."""
    
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    BILLED = "BILLED"
    CANCELED = "CANCELED"
    REFUND_PENDING = "REFUND_PENDING"
    REFUND_PENDING_IF_BILLED = "REFUND_PENDING_IF_BILLED"
    REFUND_IN_PROGRESS = "REFUND_IN_PROGRESS"
    REFUNDED = "REFUNDED"
    REFUND_DOWNGRADE_PENDING = "REFUND_DOWNGRADE_PENDING"
    REFUND_DOWNGRADE_IN_PROGRESS = "REFUND_DOWNGRADE_IN_PROGRESS"
    REFUND_DOWNGRADE_CANCELED = "REFUND_DOWNGRADE_CANCELED"
    REFUNDED_DOWNGRADE = "REFUNDED_DOWNGRADE"
    DISBURSED = "DISBURSED"
    ACH_REJECT = "ACH_REJECT"
    RESUBMITTED = "RESUBMITTED"
    INCURRED = "INCURRED"
    REFUND_INCURRED = "REFUND_INCURRED"
    REFUND_INCURRED_IF_BILLED = "REFUND_INCURRED_IF_BILLED"
    REFUND_DOWNGRADE_INCURRED = "REFUND_DOWNGRADE_INCURRED"
    REFUND_ACH_REJECT = "REFUND_ACH_REJECT"
    REFUND_DOWNGRADE_ACH_REJECT = "REFUND_DOWNGRADE_ACH_REJECT"
    REFUND_CANCELED = "REFUND_CANCELED"
    WAIVED = "WAIVED"
    REFUND_WAIVED = "REFUND_WAIVED"
    REFUND_DOWNGRADE_WAIVED = "REFUND_DOWNGRADE_WAIVED"
    WRITTEN_OFF = "WRITTEN_OFF"
    REFUND_WRITTEN_OFF = "REFUND_WRITTEN_OFF"
    REFUND_DOWNGRADE_WRITTEN_OFF = "REFUND_DOWNGRADE_WRITTEN_OFF"
    REVERSED = "REVERSED"
    REFUND_REVERSED = "REFUND_REVERSED"
    REFUND_DOWNGRADE_REVERSED = "REFUND_DOWNGRADE_REVERSED"


class DeveloperStatus(str, Enum):
    """Enum for developer status values."""
    
    DISBURSED = "DISBURSED"
    DISBURSE_FAILED = "DISBURSE_FAILED"
    DISBURSE_PENDING = "DISBURSE_PENDING"
    RECLAIMED = "RECLAIMED"
    RECLAIM_FAILED = "RECLAIM_FAILED"
    RECLAIM_PENDING = "RECLAIM_PENDING"


class ChargeType(str, Enum):
    """Enum for charge type values."""
    
    SUBSCRIPTION = "SUBSCRIPTION"
    METERED = "METERED"
    PRORATED_SUBSCRIPTION = "PRORATED_SUBSCRIPTION"
    PARTIAL_MONTH = "PARTIAL_MONTH"


class StageCharge(RhizomeModel, table=False):
    """
    SQLModel for the `stage_charge` table.

    This model represents stage charge records in the North America billing system,
    containing charge information for apps and subscriptions.
    """


    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True, description="Unique identifier for the stage charge")
    merchant_id: int = Field(description="ID of the merchant")
    currency: str | None = Field(default=None, max_length=3, description="Currency code (ISO 4217)")
    amount: int = Field(description="Charge amount in smallest currency unit")
    tax: int | None = Field(default=None, description="Tax amount in smallest currency unit")
    developer_portion: int | None = Field(default=None, description="Developer portion amount")
    status: ChargeStatus = Field(description="Current status of the charge")
    developer_status: DeveloperStatus | None = Field(default=None, description="Developer-specific status")
    status_owner: str = Field(max_length=30, description="Owner of the current status")
    type: ChargeType = Field(description="Type of charge")
    tax_classification_code: str | None = Field(default=None, max_length=10, description="Tax classification code")
    start_date: datetime.datetime | None = Field(default=None, description="Start date of the charge period")
    end_date: datetime.datetime | None = Field(default=None, description="End date of the charge period")
    created_time: datetime.datetime | None = Field(default=None, description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")
    export_month: datetime.date | None = Field(default=None, description="Month for export processing")
    status_modified_time: datetime.datetime | None = Field(default=None, description="When status was last modified")
    request_uuid: str = Field(max_length=13, description="UUID of the request that generated this charge")
    promoted_time: datetime.datetime | None = Field(default=None, description="When the charge was promoted")
    promoted_id: int | None = Field(default=None, description="ID of promoted charge")
    parent_id: int | None = Field(default=None, description="ID of parent charge")

    def sanitize(self) -> StageCharge:
        """Return a sanitized copy of this StageCharge instance."""
        return StageCharge(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),  # type: ignore
            merchant_id=self.merchant_id,
            currency=self.currency,
            amount=self.amount,
            tax=self.tax,
            developer_portion=self.developer_portion,
            status=self.status,
            developer_status=self.developer_status,
            status_owner=self.status_owner,
            type=self.type,
            tax_classification_code=self.tax_classification_code,
            start_date=self.start_date,
            end_date=self.end_date,
            created_time=self.created_time,
            modified_time=self.modified_time,
            export_month=self.export_month,
            status_modified_time=self.status_modified_time,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),  # type: ignore
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
            parent_id=self.parent_id,
        )