"""
SQLModel definition for the monetary_rule_set_rule table.

This module provides the SQLModel class for the monetary_rule_set_rule table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MonetaryRuleSetRule(RhizomeModel, table=False):
    """
    SQLModel for the `monetary_rule_set_rule` table.

    This model represents monetary rule set rule records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    monetary_rule_set_uuid: str = Field(max_length=26, description="Monetary Rule Set Uuid")
    rule_uuid: str = Field(max_length=26, description="Rule Uuid")
    rule_type: str = Field(description="Rule Type")
    effective_date: datetime.date = Field(description="Effective Date")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> MonetaryRuleSetRule:
        """Return a sanitized copy of this MonetaryRuleSetRule instance."""
        return MonetaryRuleSetRule(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            monetary_rule_set_uuid=sanitize_uuid_field(self.monetary_rule_set_uuid, 26),  # type: ignore
            rule_uuid=sanitize_uuid_field(self.rule_uuid, 26),  # type: ignore
            rule_type=self.rule_type,
            effective_date=self.effective_date,
            deleted_date=self.deleted_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
