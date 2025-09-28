"""
SQLModel definition for the reseller_app_rev_share table.

This module provides the SQLModel class for the reseller_app_rev_share table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ResellerAppRevShare(RhizomeModel, table=False):
    """
    SQLModel for the `reseller_app_rev_share` table.

    This model represents reseller_app_rev_share records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reseller_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    app_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    app_type: str | None = Field(default=None, description="app_type")
    rev_share: int = Field(description="rev_share")
    rev_share_type: str | None = Field(default=None, description="rev_share_type")
    effective_date: datetime.datetime = Field(description="effective_date")
    deleted_time: datetime.datetime | None = Field(default=None, description="deleted_time")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> ResellerAppRevShare:
        """Return a sanitized copy of this ResellerAppRevShare instance."""
        return ResellerAppRevShare(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            reseller_id=self.reseller_id,
            app_uuid=sanitize_uuid_field(self.app_uuid, 13),
            app_type=self.app_type,
            rev_share=self.rev_share,
            rev_share_type=self.rev_share_type,
            effective_date=self.effective_date,
            deleted_time=self.deleted_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
