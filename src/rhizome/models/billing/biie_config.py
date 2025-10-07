"""
SQLModel definition for the biie_config table.

This module provides the SQLModel class for the biie_config table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BiieConfig(RhizomeModel, table=False):
    """
    SQLModel for the `biie_config` table.

    This model represents biie_config records in the billing system.
    """

    id: int = Field(primary_key=True, description="id")
    uuid: str = Field(max_length=13, description="uuid")
    enabled: bool = Field(description="enabled")

    def sanitize(self) -> BiieConfig:
        """Return a sanitized copy of this BiieConfig instance."""
        return BiieConfig(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            enabled=self.enabled,
        )
