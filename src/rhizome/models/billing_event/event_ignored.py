"""
SQLModel definition for the event_ignored table.

This module provides the SQLModel class for the event_ignored table from the
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


class EventIgnored(RhizomeModel, table=False):
    """
    SQLModel for the `event_ignored` table.

    This model represents ignored events in the billing system,
    containing information about events that were ignored during processing.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the ignored event")
    reference_id: str = Field(max_length=13, description="Reference ID for the event")
    consumer_source: ConsumerSource = Field(description="Source of the consumer (MLC or AGREEMENT)")
    payload: str = Field(description="Event payload data")
    channel: str = Field(max_length=25, description="Channel through which the event was received")
    topic: str = Field(max_length=127, description="Topic of the event")
    ignore_reason: str = Field(max_length=25, description="Reason why the event was ignored")
    message: str | None = Field(default=None, max_length=500, description="Additional message about the ignored event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> EventIgnored:
        """Return a sanitized copy of this EventIgnored instance."""
        return EventIgnored(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            reference_id=sanitize_uuid_field(self.reference_id, 13),  # type: ignore
            consumer_source=self.consumer_source,
            payload=self.payload,
            channel=self.channel,
            topic=self.topic,
            ignore_reason=self.ignore_reason,
            message=self.message,
            created_timestamp=self.created_timestamp,
        )