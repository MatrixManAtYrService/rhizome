"""
SQLModel definition for the reseller_plan_trial table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="ResellerPlanTrial")


class ResellerPlanTrial(RhizomeModel, table=False):
    """
    Base ResellerPlanTrial model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13)
    reseller_id: int
    merchant_plan_id: int
    trial_days: int
    finalize_time: datetime.datetime | None = Field(default=None)
    created_time: datetime.datetime
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this ResellerPlanTrial instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
