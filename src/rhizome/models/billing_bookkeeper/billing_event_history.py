"""
SQLModel definition for the billing_event_history table.

This module provides the SQLModel class for the billing_event_history table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingEventHistory(RhizomeModel, table=False):
    """
    SQLModel for the `billing_event_history` table.

    This model represents billing event history records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    environment: str = Field(max_length=25, description="Environment")
    entity_uuid: str = Field(max_length=13, description="Entity Uuid")
    entity_type: str = Field(description="Entity Type")
    event_uuid: str | None = Field(default=None, max_length=26, description="Event Uuid")
    input: str = Field(description="Input")
    message: str | None = Field(default=None, max_length=1024, description="Message")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> BillingEventHistory:
        """Return a sanitized copy of this BillingEventHistory instance."""
        return BillingEventHistory(
            id=self.id,
            environment=self.environment,
            entity_uuid=sanitize_uuid_field(self.entity_uuid, 13),  # type: ignore
            entity_type=self.entity_type,
            event_uuid=sanitize_uuid_field(self.event_uuid, 26),
            input=self.input,
            message=self.message,
            created_timestamp=self.created_timestamp,
        )
