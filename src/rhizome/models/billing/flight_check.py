"""
SQLModel definition for the flight_check table.

This module provides the SQLModel class for the flight_check table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FlightCheck(RhizomeModel, table=False):
    """
    SQLModel for the `flight_check` table.

    This model represents flight_check records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    executor: str = Field(max_length=255, description="executor")
    enabled: bool = Field(description="enabled")
    cycle_minutes: str = Field(description="cycle_minutes")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    deleted_time: datetime.datetime | None = Field(default=None, description="deleted_time")

    def sanitize(self) -> FlightCheck:
        """Return a sanitized copy of this FlightCheck instance."""
        return FlightCheck(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            executor=self.executor,
            enabled=self.enabled,
            cycle_minutes=self.cycle_minutes,
            created_time=self.created_time,
            modified_time=self.modified_time,
            deleted_time=self.deleted_time,
        )
