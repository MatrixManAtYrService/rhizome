"""
SQLModel definition for the merchant_app_subscription_history table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantAppSubscriptionHistory")


class MerchantAppSubscriptionHistory(RhizomeModel, table=True):
    """
    SQLModel for the `merchant_app_subscription_history` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    merchant_app_id: int = Field(foreign_key="merchant_app.id")
    old_app_subscription_id: int | None = Field(default=None, foreign_key="app_subscription.id")
    created_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantAppSubscriptionHistory instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
