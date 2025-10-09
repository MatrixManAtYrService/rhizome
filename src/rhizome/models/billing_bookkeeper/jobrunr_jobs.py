"""
SQLModel definition for the jobrunr_jobs table.

This module provides the SQLModel class for the jobrunr_jobs table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrJobs(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_jobs` table.

    This model represents jobrunr jobs records in the billing system.
    """

    id: str = Field(primary_key=True, max_length=36, description="Id")
    version: int = Field(description="Version")
    jobAsJson: str | None = Field(default=None, description="Jobasjson")
    jobSignature: str = Field(max_length=512, description="Jobsignature")
    state: str = Field(max_length=36, description="State")
    createdAt: datetime.datetime = Field(description="Createdat")
    updatedAt: datetime.datetime = Field(description="Updatedat")
    scheduledAt: datetime.datetime | None = Field(default=None, description="Scheduledat")
    recurringJobId: str | None = Field(default=None, max_length=128, description="Recurringjobid")

    def sanitize(self) -> JobrunrJobs:
        """Return a sanitized copy of this JobrunrJobs instance."""
        return JobrunrJobs(
            id=self.id,
            version=self.version,
            jobAsJson=self.jobAsJson,
            jobSignature=self.jobSignature,
            state=self.state,
            createdAt=self.createdAt,
            updatedAt=self.updatedAt,
            scheduledAt=self.scheduledAt,
            recurringJobId=self.recurringJobId,
        )
