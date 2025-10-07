"""
SQLModel definition for the server_config table.

This module provides the SQLModel class for the server_config table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class ServerConfig(RhizomeModel, table=False):
    """
    SQLModel for the `server_config` table.

    This model represents server configuration records in the billing system,
    containing configuration settings for various server components.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    tag: str = Field(max_length=127, unique=True, description="Configuration tag identifier")
    config: str | None = Field(default=None, max_length=2000, description="Configuration value")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> ServerConfig:
        """Return a sanitized copy of this ServerConfig instance."""
        return ServerConfig(
            id=self.id,
            tag=self.tag,
            config=self.config,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
