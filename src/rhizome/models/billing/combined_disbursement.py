"""
SQLModel definition for the combined_disbursement table.

This module provides the SQLModel class for the combined_disbursement table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CombinedDisbursement(RhizomeModel, table=False):
    """
    SQLModel for the `combined_disbursement` table.

    This model represents combined_disbursement records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    request_uuid: str | None = Field(default=None, description="UUID field")
    vendor_code: str | None = Field(default=None, max_length=30, description="vendor_code")
    base_currency: str | None = Field(default=None, max_length=3, description="base_currency")
    base_amount: int | None = Field(default=None, description="base_amount")
    state_date: datetime.date | None = Field(default=None, description="state_date")
    pay_out_currency: str | None = Field(default=None, max_length=3, description="pay_out_currency")
    pay_out_amount: int | None = Field(default=None, description="pay_out_amount")
    pay_out_exchange_rate: str | None = Field(default=None, max_length=10, description="pay_out_exchange_rate")
    state: str | None = Field(default=None, description="state")
    reject_code: str | None = Field(default=None, max_length=32, description="reject_code")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> CombinedDisbursement:
        """Return a sanitized copy of this CombinedDisbursement instance."""
        return CombinedDisbursement(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            vendor_code=self.vendor_code,
            base_currency=self.base_currency,
            base_amount=self.base_amount,
            state_date=self.state_date,
            pay_out_currency=self.pay_out_currency,
            pay_out_amount=self.pay_out_amount,
            pay_out_exchange_rate=self.pay_out_exchange_rate,
            state=self.state,
            reject_code=self.reject_code,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
