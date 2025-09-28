"""
SQLModel definition for the merchant_role table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantRole")


class MerchantRole(RhizomeModel, table=True):
    """
    SQLModel for the `merchant_role` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    account_id: int = Field(foreign_key="account.id")
    merchant_id: int = Field(foreign_key="merchant.id")
    role: str = Field(max_length=8)
    pin: str | None = Field(default=None, max_length=8)
    nickname: str | None = Field(default=None, max_length=127)
    custom_id: str | None = Field(default=None, max_length=127)
    role_id: int
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantRole instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
