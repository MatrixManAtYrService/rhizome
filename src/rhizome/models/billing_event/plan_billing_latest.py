"""
SQLModel definition for the plan_billing_latest table.

This module provides the SQLModel class for the plan_billing_latest table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PlanBillingLatest(RhizomeModel, table=False):
    """
    SQLModel for the `plan_billing_latest` table.

    This model represents the latest billing information for merchant plans,
    containing the most recent billing date and plan details.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    last_billing_date: datetime.date = Field(description="Date of the last billing")
    last_billed_plan_uuid: str = Field(max_length=13, description="UUID of the last billed plan")
    last_plan_billing_method: str = Field(max_length=20, description="Billing method for the last plan")
    billing_event_uuid: str = Field(max_length=26, description="UUID of the billing event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> PlanBillingLatest:
        """Return a sanitized copy of this PlanBillingLatest instance."""
        return PlanBillingLatest(
            id=self.id,
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            environment=self.environment,
            last_billing_date=self.last_billing_date,
            last_billed_plan_uuid=sanitize_uuid_field(self.last_billed_plan_uuid, 13),  # type: ignore
            last_plan_billing_method=self.last_plan_billing_method,
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),  # type: ignore
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
