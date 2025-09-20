"""
SQLModel definition for the event_filter table.

This module provides the SQLModel class for the event_filter table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class EventFilterCriteriaEnum(StrEnum):
    """Enum for criteria field in event_filter table."""

    RESELLER = "RESELLER"
    MERCHANT = "MERCHANT"
    DEVELOPER_APP = "DEVELOPER_APP"
    APP = "APP"
    OFFBOARDING_RESELLER = "OFFBOARDING_RESELLER"
    ABBS = "ABBS"
    ABBS_COLLECTION = "ABBS_COLLECTION"


class EventFilterActionEnum(StrEnum):
    """Enum for action field in event_filter table."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"
    CAPTURE = "CAPTURE"


class EventFilter(RhizomeModel, table=False):
    """
    SQLModel for the `event_filter` table.

    This model represents event filters in the billing system,
    containing criteria and actions for filtering billing events.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=36, description="Unique identifier for the event filter")
    criteria: EventFilterCriteriaEnum = Field(description="Criteria for the filter")
    action: EventFilterActionEnum = Field(description="Action to take when criteria is met")
    value: str = Field(max_length=255, description="Value to match against the criteria")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    begin_timestamp: datetime.datetime | None = Field(default=None, description="Timestamp when filter becomes active")
    end_timestamp: datetime.datetime | None = Field(default=None, description="Timestamp when filter becomes inactive")

    def sanitize(self) -> EventFilter:
        """Return a sanitized copy of this EventFilter instance."""
        return EventFilter(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            criteria=self.criteria,
            action=self.action,
            value=self.value,
            created_timestamp=self.created_timestamp,
            begin_timestamp=self.begin_timestamp,
            end_timestamp=self.end_timestamp,
        )
