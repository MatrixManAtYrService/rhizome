"""
SQLModel definition for the fee_tax table.

This module provides the SQLModel class for the fee_tax table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeTax(RhizomeModel, table=False):
    """
    SQLModel for the `fee_tax` table.

    This model represents fee tax records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    fee_summary_uuid: str = Field(max_length=26, description="Fee Summary Uuid")
    tax1_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax1 Amount")
    tax2_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax2 Amount")
    tax3_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax3 Amount")
    tax4_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax4 Amount")
    tax1_rate: Decimal | None = Field(default=None, max_digits=7, decimal_places=4, description="Tax1 Rate")
    tax2_rate: Decimal | None = Field(default=None, max_digits=7, decimal_places=4, description="Tax2 Rate")
    tax3_rate: Decimal | None = Field(default=None, max_digits=7, decimal_places=4, description="Tax3 Rate")
    tax4_rate: Decimal | None = Field(default=None, max_digits=7, decimal_places=4, description="Tax4 Rate")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> FeeTax:
        """Return a sanitized copy of this FeeTax instance."""
        return FeeTax(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            fee_summary_uuid=sanitize_uuid_field(self.fee_summary_uuid, 26),  # type: ignore
            tax1_amount=self.tax1_amount,
            tax2_amount=self.tax2_amount,
            tax3_amount=self.tax3_amount,
            tax4_amount=self.tax4_amount,
            tax1_rate=self.tax1_rate,
            tax2_rate=self.tax2_rate,
            tax3_rate=self.tax3_rate,
            tax4_rate=self.tax4_rate,
            created_timestamp=self.created_timestamp,
        )
