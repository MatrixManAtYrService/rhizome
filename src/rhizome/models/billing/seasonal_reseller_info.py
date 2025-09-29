"""
SQLModel definition for the seasonal_reseller_info table.

This module provides the SQLModel class for the seasonal_reseller_info table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class SeasonalResellerInfo(RhizomeModel, table=False):
    """
    SQLModel for the `seasonal_reseller_info` table.

    This model represents seasonal_reseller_info records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    reseller_uuid_parent: str = Field(max_length=13, description="reseller_uuid_parent")
    reseller_uuid_child: str = Field(max_length=13, description="reseller_uuid_child")
    seasonal_automation_supported: bool | None = Field(default=None, description="seasonal_automation_supported")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> SeasonalResellerInfo:
        """Return a sanitized copy of this SeasonalResellerInfo instance."""
        return SeasonalResellerInfo(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            reseller_uuid_parent=sanitize_uuid_field(self.reseller_uuid_parent, 13),
            reseller_uuid_child=sanitize_uuid_field(self.reseller_uuid_child, 13),
            seasonal_automation_supported=self.seasonal_automation_supported,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
