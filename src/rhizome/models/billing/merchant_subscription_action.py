"""
SQLModel definition for the merchant_subscription_action table.

This module provides the SQLModel class for the merchant_subscription_action table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantSubscriptionAction(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_subscription_action` table.

    This model represents merchant_subscription_action records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    cause: str | None = Field(default=None, description="cause")
    context: str | None = Field(default=None, description="context")
    detail: str = Field(max_length=31, description="detail")
    dry_run: bool | None = Field(default=None, description="dry_run")
    created_time: datetime.datetime = Field(description="created_time")
    deleted_time: datetime.datetime | None = Field(default=None, description="deleted_time")

    def sanitize(self) -> MerchantSubscriptionAction:
        """Return a sanitized copy of this MerchantSubscriptionAction instance."""
        return MerchantSubscriptionAction(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            merchant_id=self.merchant_id,
            cause=self.cause,
            context=self.context,
            detail=self.detail,
            dry_run=self.dry_run,
            created_time=self.created_time,
            deleted_time=self.deleted_time,
        )
