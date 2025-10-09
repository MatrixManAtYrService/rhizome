"""
SQLModel definition for the fee_ytd table.

This module provides the SQLModel class for the fee_ytd table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeYtd(RhizomeModel, table=False):
    """
    SQLModel for the `fee_ytd` table.

    This model represents fee ytd records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    year: int = Field(description="Year")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    currency: str = Field(max_length=3, description="Currency")
    total_period_units: Decimal = Field(max_digits=12, decimal_places=4, description="Total Period Units")
    total_basis_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total Basis Amount")
    total_fee_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total Fee Amount")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeYtd:
        """Return a sanitized copy of this FeeYtd instance."""
        return FeeYtd(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            year=self.year,
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            currency=self.currency,
            total_period_units=self.total_period_units,
            total_basis_amount=self.total_basis_amount,
            total_fee_amount=self.total_fee_amount,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
