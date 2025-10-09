"""
SQLModel definition for the monetary_rule_set table.

This module provides the SQLModel class for the monetary_rule_set table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MonetaryRuleSet(RhizomeModel, table=False):
    """
    SQLModel for the `monetary_rule_set` table.

    This model represents monetary rule set records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    rule_status: str = Field(description="Rule Status")
    short_desc: str = Field(max_length=40, description="Short Desc")
    full_desc: str | None = Field(default=None, max_length=255, description="Full Desc")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> MonetaryRuleSet:
        """Return a sanitized copy of this MonetaryRuleSet instance."""
        return MonetaryRuleSet(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            rule_status=self.rule_status,
            short_desc=self.short_desc,
            full_desc=self.full_desc,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
