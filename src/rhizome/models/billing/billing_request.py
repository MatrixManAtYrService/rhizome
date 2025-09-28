"""
SQLModel definition for the billing_request table.

This module provides the SQLModel class for the billing_request table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingRequest(RhizomeModel, table=False):
    """
    SQLModel for the `billing_request` table.

    This model represents billing_request records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    query_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    name: str = Field(max_length=127, description="name")
    status: str | None = Field(default=None, description="status")
    input_class: str | None = Field(default=None, max_length=255, description="input_class")
    entry_point: str = Field(max_length=255, description="entry_point")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    completed_time: datetime.datetime | None = Field(default=None, description="completed_time")
    server_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> BillingRequest:
        """Return a sanitized copy of this BillingRequest instance."""
        return BillingRequest(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            query_uuid=sanitize_uuid_field(self.query_uuid, 13),
            name=self.name,
            status=self.status,
            input_class=self.input_class,
            entry_point=self.entry_point,
            created_time=self.created_time,
            modified_time=self.modified_time,
            completed_time=self.completed_time,
            server_id=self.server_id,
        )
