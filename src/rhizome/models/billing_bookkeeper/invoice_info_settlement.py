"""
SQLModel definition for the invoice_info_settlement table.

This module provides the SQLModel class for the invoice_info_settlement table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceInfoSettlement(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_info_settlement` table.

    This model represents invoice info settlement records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    invoice_info_uuid: str = Field(max_length=26, description="Invoice Info Uuid")
    settlement_uuid: str = Field(max_length=26, description="Settlement Uuid")
    request_uuid: str = Field(max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> InvoiceInfoSettlement:
        """Return a sanitized copy of this InvoiceInfoSettlement instance."""
        return InvoiceInfoSettlement(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            invoice_info_uuid=sanitize_uuid_field(self.invoice_info_uuid, 26),  # type: ignore
            settlement_uuid=sanitize_uuid_field(self.settlement_uuid, 26),  # type: ignore
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),  # type: ignore
            created_timestamp=self.created_timestamp,
        )
