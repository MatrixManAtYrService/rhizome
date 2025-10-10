"""
SQLModel definition for the jobrunr_migrations table.

This module provides the SQLModel class for the jobrunr_migrations table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrMigrations(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_migrations` table.

    This model represents jobrunr migrations records in the billing system.
    """

    id: str = Field(primary_key=True, max_length=36, description="Id")
    script: str = Field(max_length=64, description="Script")
    installedOn: str = Field(max_length=29, description="Installedon")

    def sanitize(self) -> JobrunrMigrations:
        """Return a sanitized copy of this JobrunrMigrations instance."""
        return JobrunrMigrations(
            id=self.id,
            script=self.script,
            installedOn=self.installedOn,
        )
