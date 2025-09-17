"""
SQLModel definition for the settlement table.

This module provides the SQLModel class for the settlement table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PayableReceivable(StrEnum):
    """Enum for payable/receivable type."""

    PAYABLE = "PAYABLE"
    RECEIVABLE = "RECEIVABLE"


class Settlement(RhizomeModel, table=False):
    """
    SQLModel for the `settlement` table.

    This model represents settlement transactions in the billing bookkeeper system,
    tracking financial settlements between parties.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the settlement")
    settlement_date: datetime.date = Field(description="Date of settlement")
    billing_entity_uuid: str = Field(max_length=26, description="UUID of the billing entity")
    entity_uuid: str = Field(max_length=13, description="UUID of the entity (merchant)")
    alternate_id: str | None = Field(default=None, max_length=30, description="Alternate identifier")
    payable_receivable: PayableReceivable = Field(description="Whether this is a payable or receivable")
    currency: str = Field(max_length=3, description="Currency code")
    total_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total settlement amount")
    fee_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Fee amount")
    tax1_amount: Decimal = Field(
        default=Decimal("0.000"), max_digits=12, decimal_places=3, description="Tax 1 amount"
    )
    tax2_amount: Decimal = Field(
        default=Decimal("0.000"), max_digits=12, decimal_places=3, description="Tax 2 amount"
    )
    tax3_amount: Decimal = Field(
        default=Decimal("0.000"), max_digits=12, decimal_places=3, description="Tax 3 amount"
    )
    tax4_amount: Decimal = Field(
        default=Decimal("0.000"), max_digits=12, decimal_places=3, description="Tax 4 amount"
    )
    lookup_ledger_account_key: str = Field(max_length=32, description="Ledger account lookup key")
    gl_code: str | None = Field(default=None, max_length=40, description="General ledger code")
    item_code: str | None = Field(default=None, max_length=30, description="Item code")
    last_invoice_num: str | None = Field(default=None, max_length=30, description="Last invoice number")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request UUID")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> Settlement:
        """Return a sanitized copy of this Settlement instance."""
        return Settlement(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            settlement_date=self.settlement_date,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            entity_uuid=sanitize_uuid_field(self.entity_uuid, 13),  # type: ignore
            alternate_id=self.alternate_id,
            payable_receivable=self.payable_receivable,
            currency=self.currency,
            total_amount=self.total_amount,
            fee_amount=self.fee_amount,
            tax1_amount=self.tax1_amount,
            tax2_amount=self.tax2_amount,
            tax3_amount=self.tax3_amount,
            tax4_amount=self.tax4_amount,
            lookup_ledger_account_key=self.lookup_ledger_account_key,
            gl_code=self.gl_code,
            item_code=self.item_code,
            last_invoice_num=self.last_invoice_num,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
