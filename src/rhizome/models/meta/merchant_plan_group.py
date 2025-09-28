"""
SQLModel definition for the merchant_plan_group table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantPlanGroup")


class MerchantPlanGroup(RhizomeModel, table=False):
    """
    Base MerchantPlanGroup model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    name: str = Field(max_length=127)
    enforce_assignment: bool | None = Field(default=False)
    linkable: bool = Field(default=False)
    trial_days: int | None = Field(default=None)
    deleted_time: datetime.datetime | None = Field(default=None)
    created_time: datetime.datetime
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantPlanGroup instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
