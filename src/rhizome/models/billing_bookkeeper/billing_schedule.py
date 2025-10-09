"""
SQLModel definition for the billing_schedule table.

This module provides the SQLModel class for the billing_schedule table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingSchedule(RhizomeModel, table=False):
    """
    SQLModel for the `billing_schedule` table.

    This model represents billing schedule records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    effective_date: datetime.date = Field(description="Effective Date")
    frequency: str = Field(description="Frequency")
    billing_day: int = Field(description="Billing Day")
    next_billing_date: datetime.date = Field(description="Next Billing Date")
    last_billing_date: datetime.date | None = Field(default=None, description="Last Billing Date")
    units_in_next_period: int = Field(description="Units In Next Period")
    units_in_last_period: int | None = Field(default=None, description="Units In Last Period")
    default_currency: str = Field(max_length=3, description="Default Currency")
    close_date: datetime.date | None = Field(default=None, description="Close Date")
    effective_close_date: datetime.date | None = Field(default=None, description="Effective Close Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> BillingSchedule:
        """Return a sanitized copy of this BillingSchedule instance."""
        return BillingSchedule(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            effective_date=self.effective_date,
            frequency=self.frequency,
            billing_day=self.billing_day,
            next_billing_date=self.next_billing_date,
            last_billing_date=self.last_billing_date,
            units_in_next_period=self.units_in_next_period,
            units_in_last_period=self.units_in_last_period,
            default_currency=self.default_currency,
            close_date=self.close_date,
            effective_close_date=self.effective_close_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
