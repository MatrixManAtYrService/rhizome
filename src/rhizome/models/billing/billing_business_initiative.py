"""
SQLModel definition for the billing_business_initiative table.

This module provides the SQLModel class for the billing_business_initiative table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingBusinessInitiative(RhizomeModel, table=False):
    """
    SQLModel for the `billing_business_initiative` table.

    This model represents billing_business_initiative records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    name: str = Field(max_length=63, description="name")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> BillingBusinessInitiative:
        """Return a sanitized copy of this BillingBusinessInitiative instance."""
        return BillingBusinessInitiative(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            name=self.name,
            created_time=self.created_time,
        )
