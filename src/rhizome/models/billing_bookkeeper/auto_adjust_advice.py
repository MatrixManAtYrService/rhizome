"""
SQLModel definition for the auto_adjust_advice table.

This module provides the SQLModel class for the auto_adjust_advice table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AutoAdjustAdvice(RhizomeModel, table=False):
    """
    SQLModel for the `auto_adjust_advice` table.

    This model represents auto adjust advice records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    auto_adjust_rule_uuid: str = Field(max_length=26, description="Auto Adjust Rule Uuid")
    start_date: datetime.date = Field(description="Start Date")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    total_periods: int = Field(description="Total Periods")
    evaluated_periods: int = Field(description="Evaluated Periods")
    applied_periods: int = Field(description="Applied Periods")
    max_units: Decimal | None = Field(default=None, max_digits=12, decimal_places=4, description="Max Units")
    max_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Max Amount")
    currency: str | None = Field(default=None, max_length=3, description="Currency")
    reference: str | None = Field(default=None, max_length=50, description="Reference")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> AutoAdjustAdvice:
        """Return a sanitized copy of this AutoAdjustAdvice instance."""
        return AutoAdjustAdvice(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            auto_adjust_rule_uuid=sanitize_uuid_field(self.auto_adjust_rule_uuid, 26),  # type: ignore
            start_date=self.start_date,
            deleted_date=self.deleted_date,
            total_periods=self.total_periods,
            evaluated_periods=self.evaluated_periods,
            applied_periods=self.applied_periods,
            max_units=self.max_units,
            max_amount=self.max_amount,
            currency=self.currency,
            reference=self.reference,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
