"""
SQLModel definition for the prototype_fee_rate table.

This module provides the SQLModel class for the prototype_fee_rate table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PrototypeFeeRate(RhizomeModel, table=False):
    """
    SQLModel for the `prototype_fee_rate` table.

    This model represents prototype fee rate records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    prototype_fee_set_id: int = Field(description="Prototype Fee Set Id")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    currency: str = Field(max_length=3, description="Currency")
    apply_type: str = Field(description="Apply Type")
    per_item_amount: Decimal | None = Field(
        default=None, max_digits=12, decimal_places=3, description="Per Item Amount"
    )
    percentage: Decimal | None = Field(default=None, max_digits=5, decimal_places=2, description="Percentage")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> PrototypeFeeRate:
        """Return a sanitized copy of this PrototypeFeeRate instance."""
        return PrototypeFeeRate(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            prototype_fee_set_id=self.prototype_fee_set_id,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            currency=self.currency,
            apply_type=self.apply_type,
            per_item_amount=self.per_item_amount,
            percentage=self.percentage,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
