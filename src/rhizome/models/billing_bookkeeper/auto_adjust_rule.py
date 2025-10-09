"""
SQLModel definition for the auto_adjust_rule table.

This module provides the SQLModel class for the auto_adjust_rule table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AutoAdjustRule(RhizomeModel, table=False):
    """
    SQLModel for the `auto_adjust_rule` table.

    This model represents auto adjust rule records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    rule_status: str = Field(description="Rule Status")
    rule_alias: str | None = Field(default=None, max_length=25, description="Rule Alias")
    rate_fee_category: str = Field(max_length=25, description="Rate Fee Category")
    rate_fee_code: str = Field(max_length=25, description="Rate Fee Code")
    target_entity_type: str = Field(description="Target Entity Type")
    short_desc: str = Field(max_length=40, description="Short Desc")
    full_desc: str | None = Field(default=None, max_length=255, description="Full Desc")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> AutoAdjustRule:
        """Return a sanitized copy of this AutoAdjustRule instance."""
        return AutoAdjustRule(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            rule_status=self.rule_status,
            rule_alias=self.rule_alias,
            rate_fee_category=self.rate_fee_category,
            rate_fee_code=self.rate_fee_code,
            target_entity_type=self.target_entity_type,
            short_desc=self.short_desc,
            full_desc=self.full_desc,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
