"""
SQLModel definition for the auto_debit_no_auth_config table.

This module provides the SQLModel class for the auto_debit_no_auth_config table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AutoDebitNoAuthConfig(RhizomeModel, table=False):
    """
    SQLModel for the `auto_debit_no_auth_config` table.

    This model represents auto debit no auth configuration records in the billing system,
    containing configuration information for auto debit without authorization.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, description="Unique identifier for the config")
    description: str = Field(max_length=200, description="Description of the configuration")
    hierarchy: str = Field(max_length=255, description="Hierarchy information")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> AutoDebitNoAuthConfig:
        """Return a sanitized copy of this AutoDebitNoAuthConfig instance."""
        return AutoDebitNoAuthConfig(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            description=self.description,
            hierarchy=self.hierarchy,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )