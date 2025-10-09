"""
SQLModel definition for the lexi_attribute table.

This module provides the SQLModel class for the lexi_attribute table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LexiAttribute(RhizomeModel, table=False):
    """
    SQLModel for the `lexi_attribute` table.

    This model represents lexi attribute records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=36, unique=True, description="Uuid")
    word: str = Field(max_length=512, description="Word")
    lexicon: str = Field(max_length=128, description="Lexicon")
    attr_name: str = Field(max_length=128, description="Attr Name")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    deleted_timestamp: datetime.datetime | None = Field(default=None, description="Deleted Timestamp")

    def sanitize(self) -> LexiAttribute:
        """Return a sanitized copy of this LexiAttribute instance."""
        return LexiAttribute(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            word=self.word,
            lexicon=self.lexicon,
            attr_name=self.attr_name,
            created_timestamp=self.created_timestamp,
            deleted_timestamp=self.deleted_timestamp,
        )
