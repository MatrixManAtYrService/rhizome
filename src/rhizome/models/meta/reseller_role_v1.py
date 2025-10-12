"""
SQLModel definition for the reseller_role table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="ResellerRoleV1")


class ResellerRoleV1(RhizomeModel, table=True):
    """
    SQLModel for the `reseller_role` table.
    """

    __tablename__ = "reseller_role"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    account_id: int = Field(foreign_key="account.id")
    reseller_id: int = Field(foreign_key="reseller.id")
    permissions_id: int = Field(foreign_key="reseller_permissions.id")
    created_time: datetime.datetime | None = Field(default=None)

    def sanitize(self) -> ResellerRoleV1:
        """Return a sanitized copy of this ResellerRoleV1 instance."""
        return ResellerRoleV1(
            id=self.id,
            account_id=self.account_id,
            reseller_id=self.reseller_id,
            permissions_id=self.permissions_id,
            created_time=self.created_time,
        )
