"""
SQLModel definition for the jobrunr_recurring_jobs table.

This module provides the SQLModel class for the jobrunr_recurring_jobs table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrRecurringJobs(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_recurring_jobs` table.

    This model represents recurring job definitions in the JobRunr system,
    containing jobs that are scheduled to run repeatedly.
    """

    id: str | None = Field(
        default=None, primary_key=True, max_length=128, description="Primary key, identifier of the recurring job"
    )
    version: int = Field(description="Version number of the recurring job")
    jobAsJson: str = Field(description="Job definition as JSON")
    createdAt: int = Field(default=0, description="Timestamp when the recurring job was created (epoch time)")

    def sanitize(self) -> JobrunrRecurringJobs:
        """Return a sanitized copy of this JobrunrRecurringJobs instance."""
        return JobrunrRecurringJobs(
            id=self.id,
            version=self.version,
            jobAsJson=self.jobAsJson,
            createdAt=self.createdAt,
        )
