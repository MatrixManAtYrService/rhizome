"""
SQLModel definition for the consumer_failure table.

This module provides the SQLModel class for the consumer_failure table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ConsumerSourceEnum(StrEnum):
    """Enum for consumer_source field."""

    MLC = "MLC"
    AGREEMENT = "AGREEMENT"


class ConsumerFailure(RhizomeModel, table=False):
    """
    SQLModel for the `consumer_failure` table.

    This model represents consumer failure events in the billing system,
    containing information about failed consumer operations.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, description="Unique identifier for the consumer failure")
    environment: str = Field(max_length=25, description="Environment where the failure occurred")
    reference_id: str = Field(max_length=13, description="Reference ID associated with the failure")
    consumer_source: ConsumerSourceEnum = Field(description="Source of the consumer (MLC or AGREEMENT)")
    payload: str = Field(description="Payload data related to the failure")
    channel: str = Field(max_length=25, description="Channel where the failure occurred")
    topic: str = Field(max_length=127, description="Topic associated with the failure")
    cause: str = Field(max_length=100, description="Cause of the failure")
    message: str | None = Field(default=None, max_length=500, description="Failure message")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> ConsumerFailure:
        """Return a sanitized copy of this ConsumerFailure instance."""
        return ConsumerFailure(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            environment=self.environment,
            reference_id=sanitize_uuid_field(self.reference_id, 13),  # type: ignore
            consumer_source=self.consumer_source,
            payload=self.payload,
            channel=self.channel,
            topic=self.topic,
            cause=self.cause,
            message=self.message,
            created_timestamp=self.created_timestamp,
        )