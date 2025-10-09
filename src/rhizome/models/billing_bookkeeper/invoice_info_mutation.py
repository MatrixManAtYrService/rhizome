"""
SQLModel definition for the invoice_info_mutation table.

This module provides the SQLModel class for the invoice_info_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceInfoMutation(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_info_mutation` table.

    This model represents invoice info mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    invoice_info_id: int = Field(description="Invoice Info Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str | None = Field(default=None, max_length=26, description="Billing Entity Uuid")
    entity_uuid: str | None = Field(default=None, max_length=13, description="Entity Uuid")
    alternate_id: str | None = Field(default=None, max_length=25, description="Alternate Id")
    billing_date: datetime.date | None = Field(default=None, description="Billing Date")
    invoice_num: str | None = Field(default=None, max_length=30, description="Invoice Num")
    currency: str | None = Field(default=None, max_length=3, description="Currency")
    total_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Total Amount")
    document_uuid: str | None = Field(default=None, max_length=26, description="Document Uuid")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime | None = Field(default=None, description="Created Timestamp")

    def sanitize(self) -> InvoiceInfoMutation:
        """Return a sanitized copy of this InvoiceInfoMutation instance."""
        return InvoiceInfoMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            invoice_info_id=self.invoice_info_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),
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
