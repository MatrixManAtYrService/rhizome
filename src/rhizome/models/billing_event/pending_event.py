"""
SQLModel definition for the pending_event table.

This module provides the SQLModel class for the pending_event table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ConsumerSource(StrEnum):
    """Enum for consumer_source field values."""

    MLC = "MLC"
    AGREEMENT = "AGREEMENT"


class PendingEvent(RhizomeModel, table=False):
    """
    SQLModel for the `pending_event` table.

    This model represents pending events in the billing system,
    containing events that are waiting to be processed.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    environment: str = Field(max_length=25, description="Environment where the event originated")
    reference_id: str = Field(max_length=13, description="Reference ID for the event")
    consumer_source: ConsumerSource = Field(description="Source of the consumer (MLC or AGREEMENT)")
    payload: str = Field(description="Event payload data")
    channel: str = Field(max_length=25, description="Channel through which the event was received")
    topic: str = Field(max_length=127, description="Topic of the event")
    processor_uuid: str | None = Field(default=None, max_length=26, description="UUID of the processor handling the event")
    processing_start_timestamp: datetime.datetime | None = Field(
        default=None, description="Timestamp when processing started"
    )
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> PendingEvent:
        """Return a sanitized copy of this PendingEvent instance."""
        return PendingEvent(
            id=self.id,
            environment=self.environment,
            reference_id=sanitize_uuid_field(self.reference_id, 13),  # type: ignore
            consumer_source=self.consumer_source,
            payload=self.payload,
            channel=self.channel,
            topic=self.topic,
            processor_uuid=sanitize_uuid_field(self.processor_uuid, 26),
            processing_start_timestamp=self.processing_start_timestamp,
            created_timestamp=self.created_timestamp,
        )