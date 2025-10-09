"""
SQLModel definition for the invoice_alliance_code table.

This module provides the SQLModel class for the invoice_alliance_code table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceAllianceCode(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_alliance_code` table.

    This model represents invoice alliance code records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    alliance_code: str = Field(max_length=3, description="Alliance Code")
    invoice_count: int = Field(description="Invoice Count")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> InvoiceAllianceCode:
        """Return a sanitized copy of this InvoiceAllianceCode instance."""
        return InvoiceAllianceCode(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            alliance_code=self.alliance_code,
            invoice_count=self.invoice_count,
            created_timestamp=self.created_timestamp,
        )
