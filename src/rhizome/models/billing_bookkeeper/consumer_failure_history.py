"""
SQLModel definition for the consumer_failure_history table.

This module provides the SQLModel class for the consumer_failure_history table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ConsumerFailureHistory(RhizomeModel, table=False):
    """
    SQLModel for the `consumer_failure_history` table.

    This model represents consumer failure history records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=36, unique=True, description="Uuid")
    environment: str = Field(max_length=25, description="Environment")
    reference_id: str = Field(max_length=13, description="Reference Id")
    payload: str = Field(description="Payload")
    channel: str | None = Field(default=None, max_length=127, description="Channel")
    topic: str | None = Field(default=None, max_length=127, description="Topic")
    cause: str = Field(max_length=100, description="Cause")
    message: str | None = Field(default=None, max_length=500, description="Message")
    comment: str | None = Field(default=None, max_length=500, description="Comment")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> ConsumerFailureHistory:
        """Return a sanitized copy of this ConsumerFailureHistory instance."""
        return ConsumerFailureHistory(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            environment=self.environment,
            reference_id=sanitize_uuid_field(self.reference_id, 13),  # type: ignore
            payload=self.payload,
            channel=self.channel,
            topic=self.topic,
            cause=self.cause,
            message=self.message,
            comment=self.comment,
            created_timestamp=self.created_timestamp,
        )
