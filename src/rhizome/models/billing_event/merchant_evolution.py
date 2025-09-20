"""SQLModel definition for the merchant_evolution table.

This module provides the SQLModel class for the merchant_evolution table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class MerchantEvolution(RhizomeModel, table=False):
    """Base MerchantEvolution model - fields present in all environments.

    This model represents the evolution and lifecycle of merchants in the billing system,
    tracking their creation, closure, and other key events.

    Note: billable_merchant_type field is only available in some environments (dev/demo),
    so it's not included in this base model. Use versioned models for environment-specific fields.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing unsigned bigint")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    reseller_uuid: str = Field(max_length=13, description="UUID of the reseller")
    merchant_name: str = Field(max_length=127, description="Name of the merchant")
    seasonal: bool | None = Field(default=None, description="Whether the merchant is seasonal")
    tax_exempt: bool | None = Field(default=None, description="Whether the merchant is tax exempt")
    mlc_merchant_created_event_datetime: datetime.datetime | None = Field(
        default=None, description="Date and time of MLC merchant-created event"
    )
    mlc_merchant_created_event_uuid: str | None = Field(
        default=None, max_length=13, description="UUID of the MLC merchant created event"
    )
    created_in_bookkeeper_datetime: datetime.datetime | None = Field(
        default=None, description="Date and time merchant created in bookkeeper"
    )
    terms_accepted_datetime: datetime.datetime | None = Field(
        default=None, description="Date and time of the terms acceptance event"
    )
    agreement_event_uuid: str | None = Field(
        default=None, max_length=26, description="UUID of the terms acceptance event"
    )
    close_date: datetime.date | None = Field(default=None, description="Date the merchant was closed")
    effective_close_date: datetime.date | None = Field(
        default=None, description="Date the merchant was effectively closed"
    )
    mlc_close_event_uuid: str | None = Field(default=None, max_length=13, description="UUID of the MLC close event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> MerchantEvolution:
        """Return a sanitized copy of this MerchantEvolution instance."""
        # Subclasses must implement this method
        raise NotImplementedError("Subclasses must implement sanitize()")
