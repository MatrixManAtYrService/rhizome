"""
SQLModel definition for the tiered_rule table.

This module provides the SQLModel class for the tiered_rule table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class TieredRule(RhizomeModel, table=False):
    """
    SQLModel for the `tiered_rule` table.

    This model represents tiered rule records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    rule_status: str = Field(description="Rule Status")
    rule_alias: str | None = Field(default=None, max_length=25, description="Rule Alias")
    tiered_basis: str = Field(description="Tiered Basis")
    tiered_model: str = Field(description="Tiered Model")
    target_entity_type: str = Field(description="Target Entity Type")
    short_desc: str = Field(max_length=40, description="Short Desc")
    full_desc: str | None = Field(default=None, max_length=255, description="Full Desc")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> TieredRule:
        """Return a sanitized copy of this TieredRule instance."""
        return TieredRule(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            rule_status=self.rule_status,
            rule_alias=self.rule_alias,
            tiered_basis=self.tiered_basis,
            tiered_model=self.tiered_model,
            target_entity_type=self.target_entity_type,
            short_desc=self.short_desc,
            full_desc=self.full_desc,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
