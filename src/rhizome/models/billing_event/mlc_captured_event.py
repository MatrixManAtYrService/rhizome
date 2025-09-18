"""
SQLModel definition for the mlc_captured_event table.

This module provides the SQLModel class for the mlc_captured_event table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MlcCapturedEvent(RhizomeModel, table=False):
    """
    SQLModel for the `mlc_captured_event` table.

    This model represents MLC captured events in the billing system,
    containing events captured from the Merchant Lifecycle (MLC) system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the captured event")
    environment: str = Field(max_length=25, description="Environment where the event was captured")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    reseller_uuid: str = Field(max_length=13, description="UUID of the reseller")
    event_timestamp: datetime.datetime = Field(description="Timestamp when the original event occurred")
    mlc_event_uuid: str = Field(max_length=13, description="UUID of the MLC event")
    event_json: str = Field(description="JSON representation of the event data")
    event_context_json: str = Field(description="JSON representation of the event context")
    processed_timestamp: datetime.datetime | None = Field(
        default=None, description="Timestamp when the event was processed"
    )
    processed_billing_event_uuid: str | None = Field(
        default=None, max_length=26, description="UUID of the processed billing event"
    )
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> MlcCapturedEvent:
        """Return a sanitized copy of this MlcCapturedEvent instance."""
        return MlcCapturedEvent(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            environment=self.environment,
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            reseller_uuid=sanitize_uuid_field(self.reseller_uuid, 13),  # type: ignore
            event_timestamp=self.event_timestamp,
            mlc_event_uuid=sanitize_uuid_field(self.mlc_event_uuid, 13),  # type: ignore
            event_json=self.event_json,
            event_context_json=self.event_context_json,
            processed_timestamp=self.processed_timestamp,
            processed_billing_event_uuid=sanitize_uuid_field(self.processed_billing_event_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )