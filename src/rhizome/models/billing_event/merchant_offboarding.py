"""
SQLModel definition for the merchant_offboarding table.

This module provides the SQLModel class for the merchant_offboarding table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class OffboardingStep(StrEnum):
    """Enum for step field values."""

    INITIATE = "INITIATE"
    REMINDER = "REMINDER"
    OFFBOARD = "OFFBOARD"
    IMMEDIATE = "IMMEDIATE"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    CANCELED = "CANCELED"
    REOPENED = "REOPENED"
    BLOCKED = "BLOCKED"


class MerchantOffboarding(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_offboarding` table.

    This model represents merchant offboarding processes in the billing system,
    tracking the steps and timeline for merchant termination.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing bigint")
    uuid: str = Field(max_length=36, description="UUID identifier for the offboarding process")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant being offboarded")
    environment: str = Field(max_length=25, description="Environment where the offboarding is occurring")
    step: OffboardingStep = Field(description="Current step in the offboarding process")
    due_date: datetime.date = Field(description="Due date for the offboarding")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    offboard_timestamp: datetime.datetime = Field(description="Timestamp for the offboarding")
    deleted_timestamp: datetime.datetime | None = Field(default=None, description="Timestamp when the record was deleted")

    def sanitize(self) -> MerchantOffboarding:
        """Return a sanitized copy of this MerchantOffboarding instance."""
        return MerchantOffboarding(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            environment=self.environment,
            step=self.step,
            due_date=self.due_date,
            created_timestamp=self.created_timestamp,
            offboard_timestamp=self.offboard_timestamp,
            deleted_timestamp=self.deleted_timestamp,
        )