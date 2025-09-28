"""
SQLModel definition for the merchant_plan table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantPlan")


class MerchantPlan(RhizomeModel, table=False):
    """
    Base MerchantPlan model - defines common fields across all versions.
    """
    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    name: str = Field(max_length=31)
    type: str | None = Field(default=None, max_length=13)
    plan_code: str | None = Field(default=None, max_length=50)
    app_bundle_id: int = Field(foreign_key="app_bundle.id")
    description: str | None = Field(default=None, max_length=2047)
    reseller_id: int | None = Field(default=None)
    merchant_plan_group_id: int | None = Field(default=None)
    activation_time: datetime.datetime | None = Field(default=None)
    deactivation_time: datetime.datetime | None = Field(default=None)
    bill_to_mid: bool | None = Field(default=False)
    enforced: bool | None = Field(default=False)
    created_time: datetime.datetime
    modified_time: datetime.datetime
    default_plan: bool = Field(default=False)
    hidden: bool | None = Field(default=False)
    tags: str | None = Field(default=None, max_length=2047)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantPlan instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
