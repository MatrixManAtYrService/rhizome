"""
SQLModel definition for the fee_rate table.

This module provides the SQLModel class for the fee_rate table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ApplyType(StrEnum):
    """Enum for fee rate apply types."""

    DEFAULT = "DEFAULT"
    PER_ITEM = "PER_ITEM"
    PERCENTAGE = "PERCENTAGE"
    BOTH = "BOTH"
    NONE = "NONE"
    FLAT = "FLAT"


class FeeRate(RhizomeModel, table=False):
    """
    SQLModel for the `fee_rate` table.

    This model represents fee rates in the billing system,
    tracking different fee categories, codes, and rate structures.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the fee rate record")
    billing_entity_uuid: str = Field(max_length=26, description="UUID of the billing entity")
    fee_category: str = Field(max_length=25, description="Category of the fee")
    fee_code: str = Field(max_length=25, description="Code for the fee")
    currency: str = Field(max_length=3, description="Currency code (ISO 3-letter)")
    effective_date: datetime.date = Field(description="Date when this rate becomes effective")
    apply_type: ApplyType = Field(description="How to apply the fee (DEFAULT, PER_ITEM, PERCENTAGE, BOTH, NONE, FLAT)")
    per_item_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Per-item fee amount")
    percentage: Decimal | None = Field(default=None, max_digits=5, decimal_places=2, description="Percentage fee")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit trail identifier")

    def sanitize(self) -> FeeRate:
        """Return a sanitized copy of this FeeRate instance."""
        return FeeRate(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            currency=self.currency,
            effective_date=self.effective_date,
            apply_type=self.apply_type,
            per_item_amount=self.per_item_amount,
            percentage=self.percentage,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )