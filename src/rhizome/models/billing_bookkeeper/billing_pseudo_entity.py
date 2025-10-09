"""
SQLModel definition for the billing_pseudo_entity table.

This module provides the SQLModel class for the billing_pseudo_entity table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingPseudoEntity(RhizomeModel, table=False):
    """
    SQLModel for the `billing_pseudo_entity` table.

    This model represents billing pseudo entity records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=13, unique=True, description="Uuid")
    name: str = Field(max_length=127, description="Name")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> BillingPseudoEntity:
        """Return a sanitized copy of this BillingPseudoEntity instance."""
        return BillingPseudoEntity(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),  # type: ignore
            name=self.name,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
