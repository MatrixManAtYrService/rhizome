"""
SQLModel definition for the tier_detail table.

This module provides the SQLModel class for the tier_detail table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class TierDetail(RhizomeModel, table=False):
    """
    SQLModel for the `tier_detail` table.

    This model represents tier detail records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    tiered_rule_uuid: str = Field(max_length=26, description="Tiered Rule Uuid")
    min_units: Decimal | None = Field(default=None, max_digits=12, decimal_places=4, description="Min Units")
    min_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Min Amount")
    currency: str | None = Field(default=None, max_length=3, description="Currency")
    rate_fee_category: str = Field(max_length=25, description="Rate Fee Category")
    rate_fee_code: str = Field(max_length=25, description="Rate Fee Code")
    short_desc: str = Field(max_length=40, description="Short Desc")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> TierDetail:
        """Return a sanitized copy of this TierDetail instance."""
        return TierDetail(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            tiered_rule_uuid=sanitize_uuid_field(self.tiered_rule_uuid, 26),  # type: ignore
            min_units=self.min_units,
            min_amount=self.min_amount,
            currency=self.currency,
            rate_fee_category=self.rate_fee_category,
            rate_fee_code=self.rate_fee_code,
            short_desc=self.short_desc,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
