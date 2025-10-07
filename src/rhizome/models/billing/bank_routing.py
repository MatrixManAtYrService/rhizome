"""
SQLModel definition for the bank_routing table.

This module provides the SQLModel class for the bank_routing table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel


class BankRouting(RhizomeModel, table=False):
    """
    SQLModel for the `bank_routing` table.

    This model represents bank routing records in the billing system,
    containing bank routing number and name information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    routing_number: str = Field(max_length=40, unique=True, description="Bank routing number")
    bank_name: str = Field(max_length=256, description="Name of the bank")

    def sanitize(self) -> BankRouting:
        """Return a sanitized copy of this BankRouting instance."""
        return BankRouting(
            id=self.id,
            routing_number=self.routing_number,
            bank_name=self.bank_name,
        )
