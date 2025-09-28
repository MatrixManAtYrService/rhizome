"""
SQLModel definition for the reseller_invoice_alliance table.

This module provides the SQLModel class for the reseller_invoice_alliance table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations


from sqlmodel import Field

from ...models.base import RhizomeModel


class ResellerInvoiceAlliance(RhizomeModel, table=False):
    """
    SQLModel for the `reseller_invoice_alliance` table.

    This model represents reseller_invoice_alliance records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reseller_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    alliance: str = Field(max_length=3, description="alliance")

    def sanitize(self) -> ResellerInvoiceAlliance:
        """Return a sanitized copy of this ResellerInvoiceAlliance instance."""
        return ResellerInvoiceAlliance(
            id=self.id,
            reseller_id=self.reseller_id,
            alliance=self.alliance,
        )
