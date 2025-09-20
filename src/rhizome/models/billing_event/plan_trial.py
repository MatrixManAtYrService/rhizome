"""
SQLModel definition for the plan_trial table.

This module provides the SQLModel class for the plan_trial table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PlanTrial(RhizomeModel, table=False):
    """
    SQLModel for the `plan_trial` table.

    This model represents plan trial periods for merchants in the billing system,
    containing trial dates and billing event information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the plan trial")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    effective_datetime: datetime.datetime = Field(description="Datetime when the trial becomes effective")
    merchant_plan_uuid: str = Field(max_length=13, description="UUID of the merchant plan")
    trial_start_date: datetime.date = Field(description="Start date of the trial period")
    trial_days: int = Field(description="Number of trial days")
    billing_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the billing event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> PlanTrial:
        """Return a sanitized copy of this PlanTrial instance."""
        return PlanTrial(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            environment=self.environment,
            effective_datetime=self.effective_datetime,
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),  # type: ignore
            trial_start_date=self.trial_start_date,
            trial_days=self.trial_days,
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
