"""
SQLModel definition for the app_subscription_country table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppSubscriptionCountry")


class AppSubscriptionCountry(RhizomeModel, table=True):
    """
    SQLModel for the `app_subscription_country` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    amount: int
    country: str = Field(max_length=2)
    name: str = Field(max_length=20)
    description: str | None = Field(default=None, max_length=1024)
    app_subscription_id: int = Field(foreign_key="app_subscription.id")
    active: bool
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppSubscriptionCountry instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
