"""
SQLModel definition for the settlement_mutation table.

This module provides the SQLModel class for the settlement_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class SettlementMutation(RhizomeModel, table=False):
    """
    SQLModel for the `settlement_mutation` table.

    This model represents settlement mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    settlement_id: int = Field(description="Settlement Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    settlement_date: datetime.date | None = Field(default=None, description="Settlement Date")
    billing_entity_uuid: str | None = Field(default=None, max_length=26, description="Billing Entity Uuid")
    entity_uuid: str | None = Field(default=None, max_length=13, description="Entity Uuid")
    alternate_id: str | None = Field(default=None, max_length=30, description="Alternate Id")
    payable_receivable: str | None = Field(default=None, description="Payable Receivable")
    currency: str | None = Field(default=None, max_length=3, description="Currency")
    total_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Total Amount")
    fee_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Fee Amount")
    tax1_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax1 Amount")
    tax2_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax2 Amount")
    tax3_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax3 Amount")
    tax4_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Tax4 Amount")
    lookup_ledger_account_key: str | None = Field(default=None, max_length=32, description="Lookup Ledger Account Key")
    gl_code: str | None = Field(default=None, max_length=40, description="Gl Code")
    item_code: str | None = Field(default=None, max_length=30, description="Item Code")
    last_invoice_num: str | None = Field(default=None, max_length=30, description="Last Invoice Num")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime | None = Field(default=None, description="Created Timestamp")
    modified_timestamp: datetime.datetime | None = Field(default=None, description="Modified Timestamp")

    def sanitize(self) -> SettlementMutation:
        """Return a sanitized copy of this SettlementMutation instance."""
        return SettlementMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            settlement_id=self.settlement_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            settlement_date=self.settlement_date,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),
            entity_uuid=sanitize_uuid_field(self.entity_uuid, 13),
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
