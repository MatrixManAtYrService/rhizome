"""
SQLModel definition for the deserializable_failure table.

This module provides the SQLModel class for the deserializable_failure table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class DeserializableConsumerSourceEnum(StrEnum):
    """Enum for consumer_source field in deserializable_failure table."""

    MLC = "MLC"
    AGREEMENT = "AGREEMENT"


class DeserializableFailure(RhizomeModel, table=False):
    """
    SQLModel for the `deserializable_failure` table.

    This model represents deserializable failure events in the billing system,
    containing information about failed deserialization operations.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, description="Unique identifier for the deserializable failure")
    topic: str | None = Field(default=None, max_length=127, description="Topic associated with the failure")
    channel: str | None = Field(default=None, max_length=127, description="Channel where the failure occurred")
    environment: str = Field(max_length=25, description="Environment where the failure occurred")
    consumer_source: DeserializableConsumerSourceEnum = Field(description="Source of the consumer (MLC or AGREEMENT)")
    b64: str = Field(description="Base64 encoded data that failed to deserialize")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> DeserializableFailure:
        """Return a sanitized copy of this DeserializableFailure instance."""
        return DeserializableFailure(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            topic=self.topic,
            channel=self.channel,
            environment=self.environment,
            consumer_source=self.consumer_source,
            b64=self.b64,
            created_timestamp=self.created_timestamp,
        )
