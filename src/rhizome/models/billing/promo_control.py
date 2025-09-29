"""
SQLModel definition for the promo_control table.

This module provides the SQLModel class for the promo_control table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PromoControl(RhizomeModel, table=False):
    """
    SQLModel for the `promo_control` table.

    This model represents promo_control records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    code: str = Field(max_length=32, description="code")
    reseller_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    agent: str | None = Field(default=None, max_length=32, description="agent")
    bank: str | None = Field(default=None, max_length=32, description="bank")
    business: str | None = Field(default=None, max_length=32, description="business")
    chain: str | None = Field(default=None, max_length=32, description="chain")
    corp: str | None = Field(default=None, max_length=7, description="corp")
    marker: str | None = Field(default=None, max_length=10, description="marker")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    deleted_time: datetime.datetime | None = Field(default=None, description="deleted_time")

    def sanitize(self) -> PromoControl:
        """Return a sanitized copy of this PromoControl instance."""
        return PromoControl(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            code=self.code,
            reseller_id=self.reseller_id,
            agent=self.agent,
            bank=self.bank,
            business=self.business,
            chain=self.chain,
            corp=self.corp,
            marker=self.marker,
            created_time=self.created_time,
            modified_time=self.modified_time,
            deleted_time=self.deleted_time,
        )
