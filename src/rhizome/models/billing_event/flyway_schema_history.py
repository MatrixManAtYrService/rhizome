"""
SQLModel definition for the flyway_schema_history table.

This module provides the SQLModel class for the flyway_schema_history table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class FlywaySchemaHistory(RhizomeModel, table=False):
    """
    SQLModel for the `flyway_schema_history` table.

    This model represents Flyway database migration history,
    containing information about applied database migrations.
    """

    # Override id from base class since this table uses installed_rank as primary key
    id: int | None = Field(default=None, exclude=True)  # Not used in this table
    installed_rank: int = Field(primary_key=True, description="Installation rank of the migration")
    version: str | None = Field(default=None, max_length=50, description="Version number of the migration")
    description: str = Field(max_length=200, description="Description of the migration")
    type_: str = Field(max_length=20, alias="type", description="Type of migration (e.g., SQL, JDBC)")
    script: str = Field(max_length=1000, description="Script name or identifier")
    checksum: int | None = Field(default=None, description="Checksum of the migration file")
    installed_by: str = Field(max_length=100, description="User who installed the migration")
    installed_on: datetime.datetime = Field(description="Timestamp when the migration was installed")
    execution_time: int = Field(description="Execution time in milliseconds")
    success: bool = Field(description="Whether the migration was successful")

    def sanitize(self) -> FlywaySchemaHistory:
        """Return a sanitized copy of this FlywaySchemaHistory instance."""
        return FlywaySchemaHistory(
            installed_rank=self.installed_rank,
            version=self.version,
            description=self.description,
            type_=self.type_,
            script=self.script,
            checksum=self.checksum,
            installed_by=self.installed_by,
            installed_on=self.installed_on,
            execution_time=self.execution_time,
            success=self.success,
        )