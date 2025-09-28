"""
SQLModel definition for the disbursement_invoice_number table.

This module provides the SQLModel class for the disbursement_invoice_number table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class DisbursementInvoiceNumber(RhizomeModel, table=False):
    """
    SQLModel for the `disbursement_invoice_number` table.

    This model represents disbursement_invoice_number records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    combined_disbursement_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    invoice_number: str = Field(max_length=30, description="invoice_number")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> DisbursementInvoiceNumber:
        """Return a sanitized copy of this DisbursementInvoiceNumber instance."""
        return DisbursementInvoiceNumber(
            id=self.id,
            combined_disbursement_id=self.combined_disbursement_id,
            invoice_number=self.invoice_number,
            created_time=self.created_time,
        )
