"""SQLModel definition for the merchant_evolution table.

This module provides the SQLModel class for the merchant_evolution table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantEvolution(RhizomeModel, table=False):
    """SQLModel for the `merchant_evolution` table.

    This model represents the evolution and lifecycle of merchants in the billing system,
    tracking their creation, closure, and other key events.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing unsigned bigint")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    reseller_uuid: str = Field(max_length=13, description="UUID of the reseller")
    merchant_name: str = Field(max_length=127, description="Name of the merchant")
    seasonal: bool | None = Field(default=None, description="Whether the merchant is seasonal")
    tax_exempt: bool | None = Field(default=None, description="Whether the merchant is tax exempt")
    mlc_merchant_created_event_datetime: datetime.datetime | None = Field(default=None, description="Date and time of MLC merchant-created event")
    mlc_merchant_created_event_uuid: str | None = Field(default=None, max_length=13, description="UUID of the MLC merchant created event")
    created_in_bookkeeper_datetime: datetime.datetime | None = Field(default=None, description="Date and time merchant created in bookkeeper")
    terms_accepted_datetime: datetime.datetime | None = Field(default=None, description="Date and time of the terms acceptance event")
    agreement_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the terms acceptance event")
    close_date: datetime.date | None = Field(default=None, description="Date the merchant was closed")
    effective_close_date: datetime.date | None = Field(default=None, description="Date the merchant was effectively closed")
    mlc_close_event_uuid: str | None = Field(default=None, max_length=13, description="UUID of the MLC close event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")
    billable_merchant_type: str | None = Field(default=None, max_length=25, description="Type of billable merchant")

    def sanitize(self) -> MerchantEvolution:
        """Return a sanitized copy of this MerchantEvolution instance."""
        return MerchantEvolution(
            id=self.id,
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            reseller_uuid=sanitize_uuid_field(self.reseller_uuid, 13),  # type: ignore
            merchant_name=self.merchant_name,
            seasonal=self.seasonal,
            tax_exempt=self.tax_exempt,
            mlc_merchant_created_event_datetime=self.mlc_merchant_created_event_datetime,
            mlc_merchant_created_event_uuid=sanitize_uuid_field(self.mlc_merchant_created_event_uuid, 13),
            created_in_bookkeeper_datetime=self.created_in_bookkeeper_datetime,
            terms_accepted_datetime=self.terms_accepted_datetime,
            agreement_event_uuid=sanitize_uuid_field(self.agreement_event_uuid, 26),
            close_date=self.close_date,
            effective_close_date=self.effective_close_date,
            mlc_close_event_uuid=sanitize_uuid_field(self.mlc_close_event_uuid, 13),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            billable_merchant_type=self.billable_merchant_type,
        )