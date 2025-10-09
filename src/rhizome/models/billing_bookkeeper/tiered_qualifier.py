"""
SQLModel definition for the tiered_qualifier table.

This module provides the SQLModel class for the tiered_qualifier table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class TieredQualifier(RhizomeModel, table=False):
    """
    SQLModel for the `tiered_qualifier` table.

    This model represents tiered qualifier records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    tiered_rule_uuid: str = Field(max_length=26, description="Tiered Rule Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    negate_fee_summary: int = Field(description="Negate Fee Summary")
    disqualify: int = Field(description="Disqualify")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> TieredQualifier:
        """Return a sanitized copy of this TieredQualifier instance."""
        return TieredQualifier(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            tiered_rule_uuid=sanitize_uuid_field(self.tiered_rule_uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            negate_fee_summary=self.negate_fee_summary,
            disqualify=self.disqualify,
            created_timestamp=self.created_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
