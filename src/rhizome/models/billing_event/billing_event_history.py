"""
SQLModel definition for the billing_event_history table.

This module provides the SQLModel class for the billing_event_history table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class EventSource(StrEnum):
    """Enum for event sources in billing event history."""

    MLC = "MLC"
    PLAN_ADVANCE = "PLAN_ADVANCE"
    CELLULAR_ARREARS = "CELLULAR_ARREARS"
    APP_SUB_DAILY = "APP_SUB_DAILY"
    APP_METER_DAILY = "APP_METER_DAILY"
    APP_RATES = "APP_RATES"
    APP_SUB_ADVANCE = "APP_SUB_ADVANCE"
    BACKBOOK_MERCHANT = "BACKBOOK_MERCHANT"
    BACKBOOK_MLC = "BACKBOOK_MLC"
    BACKBOOK_APP = "BACKBOOK_APP"
    MISC_PAYMENT = "MISC_PAYMENT"
    PLAN_ARREARS = "PLAN_ARREARS"
    AGREEMENT = "AGREEMENT"


class BillingEventHistory(RhizomeModel, table=False):
    """
    SQLModel for the `billing_event_history` table.

    This model represents the history of billing events, tracking input and output
    for various event sources along with associated context and metadata.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    environment: str = Field(max_length=25, description="Environment where the event occurred")
    merchant_id: str | None = Field(default=None, max_length=13, description="ID of the merchant")
    input_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the input event")
    billing_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the billing event")
    event_source: EventSource = Field(description="Source of the billing event")
    event_context_json: str | None = Field(default=None, description="JSON context for the event")
    input: str | None = Field(default=None, description="Input data for the event")
    output: str | None = Field(default=None, description="Output data from the event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> BillingEventHistory:
        """Return a sanitized copy of this BillingEventHistory instance."""
        return BillingEventHistory(
            id=self.id,
            environment=self.environment,
            merchant_id=sanitize_uuid_field(self.merchant_id, 13),
            input_event_uuid=sanitize_uuid_field(self.input_event_uuid, 26),
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            event_source=self.event_source,
            event_context_json=self.event_context_json,
            input=self.input,
            output=self.output,
            created_timestamp=self.created_timestamp,
        )