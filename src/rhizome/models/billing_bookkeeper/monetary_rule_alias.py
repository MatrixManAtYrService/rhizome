"""
SQLModel definition for the monetary_rule_alias table.

This module provides the SQLModel class for the monetary_rule_alias table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MonetaryRuleAlias(RhizomeModel, table=False):
    """
    SQLModel for the `monetary_rule_alias` table.

    This model represents monetary rule alias records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    rule_alias: str = Field(max_length=25, description="Rule Alias")
    rule_type: str = Field(description="Rule Type")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> MonetaryRuleAlias:
        """Return a sanitized copy of this MonetaryRuleAlias instance."""
        return MonetaryRuleAlias(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            rule_alias=self.rule_alias,
            rule_type=self.rule_type,
            created_timestamp=self.created_timestamp,
        )
