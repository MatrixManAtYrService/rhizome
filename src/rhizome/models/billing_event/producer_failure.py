"""
SQLModel definition for the producer_failure table.

This module provides the SQLModel class for the producer_failure table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class EventSource(str, Enum):
    """Enum for event source types."""

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


class ProducerFailure(RhizomeModel, table=False):
    """
    SQLModel for the `producer_failure` table.

    This model represents producer failures in the billing system,
    containing failure information and event context.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, description="Unique identifier for the producer failure")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    reference_id: str = Field(max_length=13, description="Reference ID for the failure")
    event_source: EventSource = Field(description="Source of the event that failed")
    event_context_json: str | None = Field(default=None, description="JSON context of the event")
    input_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the input event")
    input: str | None = Field(default=None, description="Input data for the event")
    output: str = Field(description="Output or error message from the failure")
    channel: str = Field(max_length=25, description="Channel where the failure occurred")
    topic: str = Field(max_length=127, description="Topic related to the failure")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> ProducerFailure:
        """Return a sanitized copy of this ProducerFailure instance."""
        return ProducerFailure(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            environment=self.environment,
            reference_id=sanitize_uuid_field(self.reference_id, 13),  # type: ignore
            event_source=self.event_source,
            event_context_json=self.event_context_json,
            input_event_uuid=sanitize_uuid_field(self.input_event_uuid, 26),
            input=self.input,
            output=self.output,
            channel=self.channel,
            topic=self.topic,
            created_timestamp=self.created_timestamp,
        )
