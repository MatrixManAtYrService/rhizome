"""
SQLModel definition for the invoice_info table.

This module provides the SQLModel class for the invoice_info table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceInfo(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_info` table.

    This model represents invoice information in the billing system,
    tracking invoice details, amounts, and associated entities.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the invoice info record")
    billing_entity_uuid: str = Field(max_length=26, description="UUID of the billing entity")
    entity_uuid: str | None = Field(default=None, max_length=13, description="UUID of the entity")
    alternate_id: str | None = Field(default=None, max_length=25, description="Alternate identifier")
    billing_date: datetime.date = Field(description="Date of billing")
    invoice_num: str = Field(max_length=30, description="Invoice number")
    currency: str = Field(max_length=3, description="Currency code (ISO 3-letter)")
    total_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total invoice amount")
    document_uuid: str | None = Field(default=None, max_length=26, description="UUID of associated document")
    request_uuid: str | None = Field(default=None, max_length=26, description="UUID of the request")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> InvoiceInfo:
        """Return a sanitized copy of this InvoiceInfo instance."""
        return InvoiceInfo(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            entity_uuid=sanitize_uuid_field(self.entity_uuid, 13),
            alternate_id=self.alternate_id,
            billing_date=self.billing_date,
            invoice_num=self.invoice_num,
            currency=self.currency,
            total_amount=self.total_amount,
            document_uuid=sanitize_uuid_field(self.document_uuid, 26),
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
