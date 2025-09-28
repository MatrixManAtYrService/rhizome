"""
SQLModel definition for the merchant_address table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantAddress")


class MerchantAddress(RhizomeModel, table=False):
    """
    Base MerchantAddress model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    address_1: str | None = Field(default=None, max_length=255)
    address_2: str | None = Field(default=None, max_length=255)
    address_3: str | None = Field(default=None, max_length=255)
    city: str | None = Field(default=None, max_length=127)
    state: str | None = Field(default=None, max_length=127)
    zip: str | None = Field(default=None, max_length=127)
    country: str | None = Field(default=None, max_length=127)
    phone_number: str | None = Field(default=None, max_length=21)
    latitude: int | None = Field(default=None)
    longitude: int | None = Field(default=None)
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantAddress instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
