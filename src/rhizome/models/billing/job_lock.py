"""
SQLModel definition for the job_lock table.

This module provides the SQLModel class for the job_lock table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations


from sqlmodel import Field

from ...models.base import RhizomeModel


class JobLock(RhizomeModel, table=False):
    """
    SQLModel for the `job_lock` table.

    This model represents job_lock records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> JobLock:
        """Return a sanitized copy of this JobLock instance."""
        return JobLock(
            id=self.id,
        )
