"""
SQLModel definition for the flyway_schema_history table.

This module provides the SQLModel class for the flyway_schema_history table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class FlywaySchemaHistory(RhizomeModel, table=False):
    """
    SQLModel for the `flyway_schema_history` table.

    This model represents flyway schema history records in the billing system.
    """

    installed_rank: int | None = Field(default=None, primary_key=True, description="Installed Rank")
    version: str | None = Field(default=None, max_length=50, description="Version")
    description: str = Field(max_length=200, description="Description")
    type: str = Field(max_length=20, description="Type")
    script: str = Field(max_length=1000, description="Script")
    checksum: int | None = Field(default=None, description="Checksum")
    installed_by: str = Field(max_length=100, description="Installed By")
    installed_on: datetime.datetime = Field(description="Installed On")
    execution_time: int = Field(description="Execution Time")
    success: bool = Field(description="Success")

    def sanitize(self) -> FlywaySchemaHistory:
        """Return a sanitized copy of this FlywaySchemaHistory instance."""
        return FlywaySchemaHistory(
            installed_rank=self.installed_rank,
            version=self.version,
            description=self.description,
            type=self.type,
            script=self.script,
            checksum=self.checksum,
            installed_by=self.installed_by,
            installed_on=self.installed_on,
            execution_time=self.execution_time,
            success=self.success,
        )
