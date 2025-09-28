"""
SQLModel definition for the account table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Account")


class Account(RhizomeModel, table=True):
    """
    SQLModel for the `account` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    name: str | None = Field(default=None, max_length=127)
    email: str | None = Field(default=None, max_length=127, unique=True)
    primary_merchant_role_id: int | None = Field(default=None, foreign_key="merchant_role.id")
    primary_developer_role_id: int | None = Field(default=None, foreign_key="developer_role.id")
    primary_reseller_role_id: int | None = Field(default=None, foreign_key="reseller_role.id")
    password_hash: str | None = Field(default=None, max_length=60)
    oauth_provider: str | None = Field(default=None) # Could be an Enum
    claim_code: str | None = Field(default=None, max_length=255)
    locked_out: bool | None = Field(default=False)
    password_updated_time: datetime.datetime | None = Field(default=None)
    is_active: bool | None = Field(default=True)
    created_time: datetime.datetime | None = Field(default=None)
    claimed_time: datetime.datetime | None = Field(default=None)
    last_login: datetime.datetime | None = Field(default=None)
    invite_sent: bool | None = Field(default=False)
    auth_issuer: str | None = Field(default=None, max_length=50)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this Account instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
