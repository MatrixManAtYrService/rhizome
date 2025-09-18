"""
SQLModel definition for the cellular_billing_arrears_info table.

This module provides the SQLModel class for the cellular_billing_arrears_info table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CellularBillingArrearsInfo(RhizomeModel, table=False):
    """
    SQLModel for the `cellular_billing_arrears_info` table.

    This model represents cellular billing arrears information,
    containing data about billing arrears for cellular services.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str = Field(max_length=30, description="UUID of the request")
    merchant_uuid: str | None = Field(default=None, max_length=13, description="UUID of the merchant")
    billing_date: datetime.date = Field(description="Date of billing")
    merchant_plan_uuid: str | None = Field(default=None, max_length=13, description="UUID of the merchant plan")
    billing_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the billing event")
    total_units: int | None = Field(default=None, description="Total units for billing")
    created_at: datetime.datetime | None = Field(default=None, description="Timestamp when the record was created")
    updated_at: datetime.datetime | None = Field(default=None, description="Timestamp when the record was last updated")

    def sanitize(self) -> CellularBillingArrearsInfo:
        """Return a sanitized copy of this CellularBillingArrearsInfo instance."""
        return CellularBillingArrearsInfo(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 30),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),
            billing_date=self.billing_date,
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            total_units=self.total_units,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )