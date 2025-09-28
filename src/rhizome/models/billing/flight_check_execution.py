"""
SQLModel definition for the flight_check_execution table.

This module provides the SQLModel class for the flight_check_execution table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class FlightCheckExecution(RhizomeModel, table=False):
    """
    SQLModel for the `flight_check_execution` table.

    This model represents flight_check_execution records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    executor_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    status: str | None = Field(default=None, description="status")
    output: str | None = Field(default=None, description="output")
    payload: str | None = Field(default=None, description="payload")
    completed_time: datetime.datetime | None = Field(default=None, description="completed_time")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> FlightCheckExecution:
        """Return a sanitized copy of this FlightCheckExecution instance."""
        return FlightCheckExecution(
            id=self.id,
            executor_id=self.executor_id,
            status=self.status,
            output=self.output,
            payload=self.payload,
            completed_time=self.completed_time,
            created_time=self.created_time,
        )
