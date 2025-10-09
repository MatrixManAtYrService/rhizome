"""
SQLModel definition for the tiered_pricing table.

This module provides the SQLModel class for the tiered_pricing table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class TieredPricing(RhizomeModel, table=False):
    """
    SQLModel for the `tiered_pricing` table.

    This model represents tiered pricing records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    tiered_rule_uuid: str = Field(max_length=26, description="Tiered Rule Uuid")
    effective_date: datetime.date = Field(description="Effective Date")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> TieredPricing:
        """Return a sanitized copy of this TieredPricing instance."""
        return TieredPricing(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            tiered_rule_uuid=sanitize_uuid_field(self.tiered_rule_uuid, 26),  # type: ignore
            effective_date=self.effective_date,
            deleted_date=self.deleted_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
