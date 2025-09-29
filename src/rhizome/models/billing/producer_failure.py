"""
SQLModel definition for the producer_failure table.

This module provides the SQLModel class for the producer_failure table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ProducerFailure(RhizomeModel, table=False):
    """
    SQLModel for the `producer_failure` table.

    This model represents producer_failure records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    environment: str | None = Field(default=None, max_length=25, description="environment")
    reference_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    kafka_event_type: str | None = Field(default=None, description="kafka_event_type")
    payload: str = Field(description="payload")
    processed: bool = Field(description="processed")
    topic: str = Field(max_length=25, description="topic")
    offset: int | None = Field(default=None, description="offset")
    cause: str | None = Field(default=None, max_length=100, description="cause")
    failure_message: str | None = Field(default=None, max_length=500, description="failure_message")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> ProducerFailure:
        """Return a sanitized copy of this ProducerFailure instance."""
        return ProducerFailure(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            environment=self.environment,
            reference_id=self.reference_id,
            kafka_event_type=self.kafka_event_type,
            payload=self.payload,
            processed=self.processed,
            topic=self.topic,
            offset=self.offset,
            cause=self.cause,
            failure_message=self.failure_message,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
