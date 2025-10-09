"""
SQLModel definition for the fee_ctd table.

This module provides the SQLModel class for the fee_ctd table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeCtd(RhizomeModel, table=False):
    """
    SQLModel for the `fee_ctd` table.

    This model represents fee ctd records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    currency: str = Field(max_length=3, description="Currency")
    ctd_num_units: Decimal = Field(max_digits=12, decimal_places=4, description="Ctd Num Units")
    abs_num_units: Decimal = Field(max_digits=12, decimal_places=4, description="Abs Num Units")
    ctd_basis_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Ctd Basis Amount")
    abs_basis_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Abs Basis Amount")
    num_actions: int = Field(description="Num Actions")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeCtd:
        """Return a sanitized copy of this FeeCtd instance."""
        return FeeCtd(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            currency=self.currency,
            ctd_num_units=self.ctd_num_units,
            abs_num_units=self.abs_num_units,
            ctd_basis_amount=self.ctd_basis_amount,
            abs_basis_amount=self.abs_basis_amount,
            num_actions=self.num_actions,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
