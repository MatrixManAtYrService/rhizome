"""
SQLModel definition for the server_config table.

This module provides the SQLModel class for the server_config table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class ServerConfig(RhizomeModel, table=False):
    """
    SQLModel for the `server_config` table.

    This model represents server configuration settings in the billing system,
    containing key-value pairs for system configuration.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    config_key: str = Field(max_length=127, unique=True, description="Configuration key")
    config_value: str | None = Field(default=None, max_length=2000, description="Configuration value")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")
    audit_id: str = Field(default="DEFAULTED", max_length=26, description="Audit ID for tracking changes")

    def sanitize(self) -> ServerConfig:
        """Return a sanitized copy of this ServerConfig instance."""
        return ServerConfig(
            id=self.id,
            config_key=self.config_key,
            config_value=self.config_value,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=self.audit_id,
        )
