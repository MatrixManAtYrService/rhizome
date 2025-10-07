"""
SQLModel definition for the banner_curb table.

This module provides the SQLModel class for the banner_curb table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class BannerCurb(RhizomeModel, table=False):
    """
    SQLModel for the `banner_curb` table.

    This model represents banner curb records in the billing system,
    containing banner data associations with merchants.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    banner_data_id: int = Field(description="ID of the associated banner data")
    merchant_uuid: str = Field(max_length=30, description="Merchant UUID")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> BannerCurb:
        """Return a sanitized copy of this BannerCurb instance."""
        return BannerCurb(
            id=self.id,
            banner_data_id=self.banner_data_id,
            merchant_uuid=self.merchant_uuid,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
