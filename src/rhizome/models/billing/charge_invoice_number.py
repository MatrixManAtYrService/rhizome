"""
SQLModel definition for the charge_invoice_number table.

This module provides the SQLModel class for the charge_invoice_number table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class ChargeInvoiceNumber(RhizomeModel, table=False):
    """
    SQLModel for the `charge_invoice_number` table.

    This model represents charge_invoice_number records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    invoice_number: str = Field(max_length=30, description="invoice_number")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> ChargeInvoiceNumber:
        """Return a sanitized copy of this ChargeInvoiceNumber instance."""
        return ChargeInvoiceNumber(
            id=self.id,
            charge_id=self.charge_id,
            invoice_number=self.invoice_number,
            created_time=self.created_time,
        )
