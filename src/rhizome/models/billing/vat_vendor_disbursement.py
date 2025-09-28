"""
SQLModel definition for the vat_vendor_disbursement table.

This module provides the SQLModel class for the vat_vendor_disbursement table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class VatVendorDisbursement(RhizomeModel, table=False):
    """
    SQLModel for the `vat_vendor_disbursement` table.

    This model represents vat_vendor_disbursement records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    combined_disbursement_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    vat_base_currency: str | None = Field(default=None, max_length=3, description="vat_base_currency")
    vat_base_amount: int | None = Field(default=None, description="vat_base_amount")
    state_date: datetime.date | None = Field(default=None, description="state_date")
    vat_pay_out_currency: str | None = Field(default=None, max_length=3, description="vat_pay_out_currency")
    vat_pay_out_amount: int | None = Field(default=None, description="vat_pay_out_amount")
    vat_pay_out_exchange_rate: str | None = Field(default=None, max_length=10, description="vat_pay_out_exchange_rate")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> VatVendorDisbursement:
        """Return a sanitized copy of this VatVendorDisbursement instance."""
        return VatVendorDisbursement(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            combined_disbursement_id=self.combined_disbursement_id,
            vat_base_currency=self.vat_base_currency,
            vat_base_amount=self.vat_base_amount,
            state_date=self.state_date,
            vat_pay_out_currency=self.vat_pay_out_currency,
            vat_pay_out_amount=self.vat_pay_out_amount,
            vat_pay_out_exchange_rate=self.vat_pay_out_exchange_rate,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
