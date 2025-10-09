"""
SQLModel definition for the invoice_info_settlement_mutation table.

This module provides the SQLModel class for the invoice_info_settlement_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class InvoiceInfoSettlementMutation(RhizomeModel, table=False):
    """
    SQLModel for the `invoice_info_settlement_mutation` table.

    This model represents invoice info settlement mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    invoice_info_settlement_id: int = Field(description="Invoice Info Settlement Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    invoice_info_uuid: str | None = Field(default=None, max_length=26, description="Invoice Info Uuid")
    settlement_uuid: str | None = Field(default=None, max_length=26, description="Settlement Uuid")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime | None = Field(default=None, description="Created Timestamp")

    def sanitize(self) -> InvoiceInfoSettlementMutation:
        """Return a sanitized copy of this InvoiceInfoSettlementMutation instance."""
        return InvoiceInfoSettlementMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            invoice_info_settlement_id=self.invoice_info_settlement_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            invoice_info_uuid=sanitize_uuid_field(self.invoice_info_uuid, 26),
            settlement_uuid=sanitize_uuid_field(self.settlement_uuid, 26),
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
