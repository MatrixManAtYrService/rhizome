"""
SQLModel definition for the lexi_rule table.

This module provides the SQLModel class for the lexi_rule table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LexiRule(RhizomeModel, table=False):
    """
    SQLModel for the `lexi_rule` table.

    This model represents lexi rule records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=36, unique=True, description="Uuid")
    parent_uuid: str | None = Field(default=None, max_length=36, description="Parent Uuid")
    lexicon: str = Field(max_length=128, description="Lexicon")
    rule_name: str = Field(max_length=128, description="Rule Name")
    description: str | None = Field(default=None, max_length=512, description="Description")
    rule_condition: str | None = Field(default=None, max_length=512, description="Rule Condition")
    target_attributes: str | None = Field(default=None, max_length=512, description="Target Attributes")
    priority: int = Field(default=None, description="Priority")
    rule_type: str = Field(description="Rule Type")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    deleted_timestamp: datetime.datetime | None = Field(default=None, description="Deleted Timestamp")

    def sanitize(self) -> LexiRule:
        """Return a sanitized copy of this LexiRule instance."""
        return LexiRule(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            parent_uuid=sanitize_uuid_field(self.parent_uuid, 36),
            lexicon=self.lexicon,
            rule_name=self.rule_name,
            description=self.description,
            rule_condition=self.rule_condition,
            target_attributes=self.target_attributes,
            priority=self.priority,
            rule_type=self.rule_type,
            created_timestamp=self.created_timestamp,
            deleted_timestamp=self.deleted_timestamp,
        )
