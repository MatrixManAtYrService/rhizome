"""
SQLModel definition for the consumer_failure_history table.

This module provides the SQLModel class for the consumer_failure_history table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ConsumerSourceHistoryEnum(StrEnum):
    """Enum for consumer_source field in history table."""

    MLC = "MLC"
    AGREEMENT = "AGREEMENT"


class ConsumerFailureHistory(RhizomeModel, table=False):
    """
    SQLModel for the `consumer_failure_history` table.

    This model represents historical consumer failure events in the billing system,
    containing archived information about failed consumer operations.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, description="Unique identifier for the consumer failure")
    environment: str = Field(max_length=25, description="Environment where the failure occurred")
    reference_id: str = Field(max_length=13, description="Reference ID associated with the failure")
    consumer_source: ConsumerSourceHistoryEnum = Field(description="Source of the consumer (MLC or AGREEMENT)")
    payload: str = Field(description="Payload data related to the failure")
    channel: str = Field(max_length=25, description="Channel where the failure occurred")
    topic: str = Field(max_length=127, description="Topic associated with the failure")
    cause: str = Field(max_length=100, description="Cause of the failure")
    message: str | None = Field(default=None, max_length=500, description="Failure message")
    comment: str | None = Field(default=None, max_length=500, description="Additional comment about the failure")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> ConsumerFailureHistory:
        """Return a sanitized copy of this ConsumerFailureHistory instance."""
        return ConsumerFailureHistory(
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
            comment=self.comment,
            created_timestamp=self.created_timestamp,
        )