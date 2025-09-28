"""
SQLModel definition for the merchant_creation_details table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantCreationDetails")


class MerchantCreationDetails(RhizomeModel, table=True):
    """
    SQLModel for the `merchant_creation_details` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    merchant_id: int = Field(unique=True, foreign_key="merchant.id")
    creation_source: str = Field(max_length=17)
    source_identifier: str | None = Field(default=None, max_length=255)
    created_time: datetime.datetime
    modified_time: datetime.datetime
    pre_create: str | None = Field(default=None, max_length=5)
    pre_source: str | None = Field(default=None, max_length=13)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantCreationDetails instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
