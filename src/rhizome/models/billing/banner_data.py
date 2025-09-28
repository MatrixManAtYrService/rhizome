"""
SQLModel definition for the banner_data table.

This module provides the SQLModel class for the banner_data table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel


class BannerLookupNameType(str, Enum):
    """Enum for banner_lookup_name values."""

    COUNTRY = "COUNTRY"
    RESELLER = "RESELLER"
    PLAN = "PLAN"
    MERCHANT = "MERCHANT"
    MERCHANT_GROUP = "MERCHANT_GROUP"


class BannerData(RhizomeModel, table=False):
    """
    SQLModel for the `banner_data` table.

    This model represents banner data records in the billing system,
    containing banner configuration and lookup information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    banner_uuid: str = Field(max_length=30, description="Banner UUID")
    banner_lookup_name: BannerLookupNameType | None = Field(default=None, description="Banner lookup name category")
    banner_lookup_value: str = Field(max_length=30, description="Banner lookup value")
    start_date: datetime.datetime | None = Field(default=None, description="Banner start date")
    end_date: datetime.datetime | None = Field(default=None, description="Banner end date")
    contentful_template_id: str = Field(max_length=50, description="Contentful template ID")
    active: bool = Field(default=False, description="Whether the banner is active")
    owner: str = Field(max_length=30, description="Banner owner")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> BannerData:
        """Return a sanitized copy of this BannerData instance."""
        return BannerData(
            id=self.id,
            banner_uuid=self.banner_uuid,
            banner_lookup_name=self.banner_lookup_name,
            banner_lookup_value=self.banner_lookup_value,
            start_date=self.start_date,
            end_date=self.end_date,
            contentful_template_id=self.contentful_template_id,
            active=self.active,
            owner=self.owner,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )