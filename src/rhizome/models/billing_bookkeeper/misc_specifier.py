"""
SQLModel definition for the misc_specifier table.

This module provides the SQLModel class for the misc_specifier table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MiscSpecifier(RhizomeModel, table=False):
    """
    SQLModel for the `misc_specifier` table.

    This model represents misc specifier records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    misc_specifier: str = Field(max_length=25, description="Misc Specifier")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> MiscSpecifier:
        """Return a sanitized copy of this MiscSpecifier instance."""
        return MiscSpecifier(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            misc_specifier=self.misc_specifier,
            created_timestamp=self.created_timestamp,
        )
