"""
SQLModel definition for the billing_request_state table.

This module provides the SQLModel class for the billing_request_state table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingRequestState(RhizomeModel, table=False):
    """
    SQLModel for the `billing_request_state` table.

    This model represents billing_request_state records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    query_uuid: str | None = Field(default=None, description="UUID field")
    state: str | None = Field(default=None, description="state")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> BillingRequestState:
        """Return a sanitized copy of this BillingRequestState instance."""
        return BillingRequestState(
            id=self.id,
            query_uuid=sanitize_uuid_field(self.query_uuid, 13),
            state=self.state,
            created_time=self.created_time,
        )
