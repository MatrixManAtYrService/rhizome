"""
SQLModel definition for the producer_failure_history table.

This module provides the SQLModel class for the producer_failure_history table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field
from .producer_failure import EventSource


class ProducerFailureHistory(RhizomeModel, table=False):
    """
    SQLModel for the `producer_failure_history` table.

    This model represents historical records of producer failures in the billing system,
    containing failure information, event context, and additional comments.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, description="Unique identifier for the producer failure history")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    reference_id: str = Field(max_length=13, description="Reference ID for the failure")
    event_source: EventSource = Field(description="Source of the event that failed")
    event_context_json: str | None = Field(default=None, description="JSON context of the event")
    input_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the input event")
    input: str | None = Field(default=None, description="Input data for the event")
    output: str = Field(description="Output or error message from the failure")
    channel: str = Field(max_length=25, description="Channel where the failure occurred")
    topic: str = Field(max_length=127, description="Topic related to the failure")
    comment: str | None = Field(default=None, max_length=500, description="Additional comment about the failure")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> ProducerFailureHistory:
        """Return a sanitized copy of this ProducerFailureHistory instance."""
        return ProducerFailureHistory(
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
            comment=self.comment,
            created_timestamp=self.created_timestamp,
        )
