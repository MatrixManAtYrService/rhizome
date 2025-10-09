"""
SQLModel definition for the prototype_fee_set table.

This module provides the SQLModel class for the prototype_fee_set table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PrototypeFeeSet(RhizomeModel, table=False):
    """
    SQLModel for the `prototype_fee_set` table.

    This model represents prototype fee set records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    name: str = Field(max_length=40, description="Name")
    disposition: str = Field(description="Disposition")
    description: str | None = Field(default=None, max_length=255, description="Description")
    effective_date: datetime.date = Field(description="Effective Date")
    disposition_datetime: datetime.datetime = Field(description="Disposition Datetime")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> PrototypeFeeSet:
        """Return a sanitized copy of this PrototypeFeeSet instance."""
        return PrototypeFeeSet(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            name=self.name,
            disposition=self.disposition,
            description=self.description,
            effective_date=self.effective_date,
            disposition_datetime=self.disposition_datetime,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
