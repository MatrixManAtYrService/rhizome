"""
SQLModel definition for the jobrunr_jobs table.

This module provides the SQLModel class for the jobrunr_jobs table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrJobs(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_jobs` table.

    This model represents jobs in the JobRunr system,
    containing job definitions, state, and scheduling information.
    """

    id: str | None = Field(default=None, primary_key=True, max_length=36, description="Primary key, UUID of the job")
    version: int = Field(description="Version number of the job")
    jobAsJson: str | None = Field(default=None, description="Job definition as JSON")
    jobSignature: str = Field(max_length=512, description="Signature of the job")
    state: str = Field(max_length=36, description="Current state of the job")
    createdAt: datetime.datetime = Field(description="Timestamp when the job was created")
    updatedAt: datetime.datetime = Field(description="Timestamp when the job was last updated")
    scheduledAt: datetime.datetime | None = Field(
        default=None, description="Timestamp when the job is scheduled to run"
    )
    recurringJobId: str | None = Field(
        default=None, max_length=128, description="ID of the recurring job this belongs to"
    )

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
