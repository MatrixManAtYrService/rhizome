"""
SQLModel definition for the billing_archetype table.

This module provides the SQLModel class for the billing_archetype table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingArchetype(RhizomeModel, table=False):
    """
    SQLModel for the `billing_archetype` table.

    This model represents billing archetype records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=13, unique=True, description="Uuid")
    archetype_type: str = Field(description="Archetype Type")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> BillingArchetype:
        """Return a sanitized copy of this BillingArchetype instance."""
        return BillingArchetype(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),  # type: ignore
            archetype_type=self.archetype_type,
            created_timestamp=self.created_timestamp,
        )
