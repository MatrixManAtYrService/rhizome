"""
SQLModel definition for the stage_email_merchant_charge table.

This module provides the SQLModel class for the stage_email_merchant_charge table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageEmailMerchantCharge(RhizomeModel, table=False):
    """
    SQLModel for the `stage_email_merchant_charge` table.

    This model represents stage_email_merchant_charge records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    type: str | None = Field(default=None, description="type")
    payment_type: str | None = Field(default=None, max_length=10, description="payment_type")
    payload: str | None = Field(default=None, description="payload")
    recipient_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    done_time: datetime.datetime | None = Field(default=None, description="done_time")
    created_time: datetime.datetime | None = Field(default=None, description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageEmailMerchantCharge:
        """Return a sanitized copy of this StageEmailMerchantCharge instance."""
        return StageEmailMerchantCharge(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            type=self.type,
            payment_type=self.payment_type,
            payload=self.payload,
            recipient_id=self.recipient_id,
            charge_id=self.charge_id,
            done_time=self.done_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
