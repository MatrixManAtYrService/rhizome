"""
SQLModel definition for the banner_details table.

This module provides the SQLModel class for the banner_details table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class BannerDetails(RhizomeModel, table=False):
    """
    SQLModel for the `banner_details` table.

    This model represents banner details records in the billing system,
    containing detailed configuration for banner data.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    banner_data_id: int = Field(description="ID of the associated banner data")
    tag: str | None = Field(default=None, max_length=256, description="Banner tag")
    config: str | None = Field(default=None, max_length=256, description="Banner configuration")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> BannerDetails:
        """Return a sanitized copy of this BannerDetails instance."""
        return BannerDetails(
            id=self.id,
            banner_data_id=self.banner_data_id,
            tag=self.tag,
            config=self.config,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
