"""
SQLModel definition for the fee_rate_error_report table.

This module provides the SQLModel class for the fee_rate_error_report table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeRateErrorReport(RhizomeModel, table=False):
    """
    SQLModel for the `fee_rate_error_report` table.

    This model represents fee rate error report records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    currency: str = Field(max_length=3, description="Currency")
    apply_type: str | None = Field(default=None, description="Apply Type")
    resolved_status: int = Field(default=None, description="Resolved Status")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeRateErrorReport:
        """Return a sanitized copy of this FeeRateErrorReport instance."""
        return FeeRateErrorReport(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            currency=self.currency,
            apply_type=self.apply_type,
            resolved_status=self.resolved_status,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
