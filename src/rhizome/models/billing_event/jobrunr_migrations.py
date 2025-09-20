"""
SQLModel definition for the jobrunr_migrations table.

This module provides the SQLModel class for the jobrunr_migrations table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrMigrations(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_migrations` table.

    This model represents migration history in the JobRunr system,
    tracking which migration scripts have been executed.
    """

    id: str | None = Field(
        default=None, primary_key=True, max_length=36, description="Primary key, UUID of the migration"
    )
    script: str = Field(max_length=64, description="Name of the migration script")
    installedOn: str = Field(max_length=29, description="Timestamp when the migration was installed")

    def sanitize(self) -> JobrunrMigrations:
        """Return a sanitized copy of this JobrunrMigrations instance."""
        return JobrunrMigrations(
            id=self.id,
            script=self.script,
            installedOn=self.installedOn,
        )
