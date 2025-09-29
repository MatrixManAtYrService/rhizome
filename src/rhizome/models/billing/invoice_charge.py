"""
SQLModel definition for the invoice_charge table.

This module provides the SQLModel class for the invoice_charge table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceCharge(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_charge` table.

    This model represents invoice_charge records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    type: str | None = Field(default=None, description="type")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_app_charge_Id: int | None = Field(default=None, description="merchant_app_charge_Id")
    merchant_plan_charge_Id: int | None = Field(default=None, description="merchant_plan_charge_Id")
    error: str | None = Field(default=None, max_length=1023, description="error")
    status: str | None = Field(default=None, description="status")
    mid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    country_code: str = Field(max_length=32, description="country_code")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    developer_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    biie: str | None = Field(default=None, description="biie")
    dev_export: str | None = Field(default=None, description="dev_export")
    dev_export_month: datetime.date | None = Field(default=None, description="dev_export_month")
    post_date: datetime.date | None = Field(default=None, description="post_date")

    def sanitize(self) -> InvoiceCharge:
        """Return a sanitized copy of this InvoiceCharge instance."""
        return InvoiceCharge(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            type=self.type,
            charge_id=self.charge_id,
            merchant_app_charge_Id=self.merchant_app_charge_Id,
            merchant_plan_charge_Id=self.merchant_plan_charge_Id,
            error=self.error,
            status=self.status,
            mid=self.mid,
            country_code=self.country_code,
            merchant_id=self.merchant_id,
            developer_id=self.developer_id,
            promoted_time=self.promoted_time,
            biie=self.biie,
            dev_export=self.dev_export,
            dev_export_month=self.dev_export_month,
            post_date=self.post_date,
        )
