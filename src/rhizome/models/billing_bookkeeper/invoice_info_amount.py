"""
SQLModel definition for the invoice_info_amount table.

This module provides the SQLModel class for the invoice_info_amount table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceInfoAmount(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_info_amount` table.

    This model represents invoice info amount records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    invoice_info_uuid: str = Field(max_length=26, description="Invoice Info Uuid")
    currency: str = Field(max_length=3, description="Currency")
    amount: Decimal = Field(max_digits=12, decimal_places=3, description="Amount")
    fee_category_group: str = Field(max_length=25, description="Fee Category Group")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> InvoiceInfoAmount:
        """Return a sanitized copy of this InvoiceInfoAmount instance."""
        return InvoiceInfoAmount(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            invoice_info_uuid=sanitize_uuid_field(self.invoice_info_uuid, 26),  # type: ignore
            currency=self.currency,
            amount=self.amount,
            fee_category_group=self.fee_category_group,
            created_timestamp=self.created_timestamp,
        )
