"""
SQLModel definition for the stage_infolease_disbursement_attempt table.

This module provides the SQLModel class for the stage_infolease_disbursement_attempt table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageInfoleaseDisbursementAttempt(RhizomeModel, table=False):
    """
    SQLModel for the `stage_infolease_disbursement_attempt` table.

    This model represents stage_infolease_disbursement_attempt records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    type: str | None = Field(default=None, max_length=5, description="type")
    vendor_name: str | None = Field(default=None, max_length=50, description="vendor_name")
    payment_type: str | None = Field(default=None, max_length=10, description="payment_type")
    payment_description: str | None = Field(default=None, max_length=30, description="payment_description")
    contract_number: str | None = Field(default=None, max_length=30, description="contract_number")
    inventory_number: str | None = Field(default=None, max_length=30, description="inventory_number")
    inventory_amount: int | None = Field(default=None, description="inventory_amount")
    inventory_date: str | None = Field(default=None, max_length=10, description="inventory_date")
    due_date: str | None = Field(default=None, max_length=10, description="due_date")
    gl_code: str | None = Field(default=None, max_length=10, description="gl_code")
    inventory_status_date: str | None = Field(default=None, max_length=10, description="inventory_status_date")
    inventory_status_time: str | None = Field(default=None, max_length=10, description="inventory_status_time")
    created_time: datetime.datetime | None = Field(default=None, description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    request_uuid: str | None = Field(default=None, description="UUID field")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageInfoleaseDisbursementAttempt:
        """Return a sanitized copy of this StageInfoleaseDisbursementAttempt instance."""
        return StageInfoleaseDisbursementAttempt(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            charge_id=self.charge_id,
            type=self.type,
            vendor_name=self.vendor_name,
            payment_type=self.payment_type,
            payment_description=self.payment_description,
            contract_number=self.contract_number,
            inventory_number=self.inventory_number,
            inventory_amount=self.inventory_amount,
            inventory_date=self.inventory_date,
            due_date=self.due_date,
            gl_code=self.gl_code,
            inventory_status_date=self.inventory_status_date,
            inventory_status_time=self.inventory_status_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
