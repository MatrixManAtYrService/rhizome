"""
SQLModel definition for the fee_summary_mutation table.

This module provides the SQLModel class for the fee_summary_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeSummaryMutation(RhizomeModel, table=False):
    """
    SQLModel for the `fee_summary_mutation` table.

    This model represents fee summary mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    fee_summary_id: int = Field(description="Fee Summary Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    billing_date: datetime.date = Field(description="Billing Date")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    currency: str = Field(max_length=3, description="Currency")
    total_period_units: Decimal = Field(max_digits=12, decimal_places=4, description="Total Period Units")
    total_basis_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total Basis Amount")
    total_fee_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total Fee Amount")
    fee_rate_uuid: str = Field(max_length=26, description="Fee Rate Uuid")
    request_uuid: str = Field(max_length=26, description="Request Uuid")
    invoice_info_uuid: str | None = Field(default=None, max_length=26, description="Invoice Info Uuid")
    fee_code_ledger_account_uuid: str | None = Field(
        default=None, max_length=26, description="Fee Code Ledger Account Uuid"
    )
    credit_ledger_account_uuid: str | None = Field(
        default=None, max_length=26, description="Credit Ledger Account Uuid"
    )
    debit_ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Debit Ledger Account Uuid")
    exclude_from_invoice: int = Field(default=None, description="Exclude From Invoice")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeSummaryMutation:
        """Return a sanitized copy of this FeeSummaryMutation instance."""
        return FeeSummaryMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            fee_summary_id=self.fee_summary_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            billing_date=self.billing_date,
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            currency=self.currency,
            total_period_units=self.total_period_units,
            total_basis_amount=self.total_basis_amount,
            total_fee_amount=self.total_fee_amount,
            fee_rate_uuid=sanitize_uuid_field(self.fee_rate_uuid, 26),  # type: ignore
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),  # type: ignore
            invoice_info_uuid=sanitize_uuid_field(self.invoice_info_uuid, 26),
            fee_code_ledger_account_uuid=sanitize_uuid_field(self.fee_code_ledger_account_uuid, 26),
            credit_ledger_account_uuid=sanitize_uuid_field(self.credit_ledger_account_uuid, 26),
            debit_ledger_account_uuid=sanitize_uuid_field(self.debit_ledger_account_uuid, 26),
            exclude_from_invoice=self.exclude_from_invoice,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
