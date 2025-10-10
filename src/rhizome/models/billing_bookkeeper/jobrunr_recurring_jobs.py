"""
SQLModel definition for the jobrunr_recurring_jobs table.

This module provides the SQLModel class for the jobrunr_recurring_jobs table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrRecurringJobs(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_recurring_jobs` table.

    This model represents jobrunr recurring jobs records in the billing system.
    """

    id: str = Field(primary_key=True, max_length=128, description="Id")
    version: int = Field(description="Version")
    jobAsJson: str = Field(description="Jobasjson")
    createdAt: int = Field(description="Createdat")

    def sanitize(self) -> JobrunrRecurringJobs:
        """Return a sanitized copy of this JobrunrRecurringJobs instance."""
        return JobrunrRecurringJobs(
            id=self.id,
            version=self.version,
            jobAsJson=self.jobAsJson,
            createdAt=self.createdAt,
        )
