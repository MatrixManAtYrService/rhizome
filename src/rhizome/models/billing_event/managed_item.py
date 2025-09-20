"""
SQLModel definition for the managed_item table.

This module provides the SQLModel class for the managed_item table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ManagedItemCriteria(StrEnum):
    """Enum for criteria field values."""

    RESELLER = "RESELLER"
    MERCHANT = "MERCHANT"


class ManagedItem(RhizomeModel, table=False):
    """
    SQLModel for the `managed_item` table.

    This model represents managed items in the billing system,
    tracking items with specific criteria and time ranges.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing unsigned bigint")
    uuid: str = Field(max_length=36, description="UUID identifier for the managed item")
    criteria: ManagedItemCriteria = Field(description="Criteria type (RESELLER or MERCHANT)")
    item: str = Field(max_length=255, description="Item identifier or name")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    begin_timestamp: datetime.datetime | None = Field(default=None, description="Start timestamp for the managed item")
    end_timestamp: datetime.datetime | None = Field(default=None, description="End timestamp for the managed item")

    def sanitize(self) -> ManagedItem:
        """Return a sanitized copy of this ManagedItem instance."""
        return ManagedItem(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            criteria=self.criteria,
            item=self.item,
            created_timestamp=self.created_timestamp,
            begin_timestamp=self.begin_timestamp,
            end_timestamp=self.end_timestamp,
        )
