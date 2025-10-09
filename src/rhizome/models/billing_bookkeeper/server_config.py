"""
SQLModel definition for the server_config table.

This module provides the SQLModel class for the server_config table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ServerConfig(RhizomeModel, table=False):
    """
    SQLModel for the `server_config` table.

    This model represents server config records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    config_key: str = Field(max_length=127, description="Config Key")
    config_value: str | None = Field(default=None, max_length=2000, description="Config Value")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str = Field(max_length=26, description="Audit Id")

    def sanitize(self) -> ServerConfig:
        """Return a sanitized copy of this ServerConfig instance."""
        return ServerConfig(
            id=self.id,
            config_key=self.config_key,
            config_value=self.config_value,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),  # type: ignore
        )
