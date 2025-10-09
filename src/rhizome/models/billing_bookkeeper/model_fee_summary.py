"""
SQLModel definition for the model_fee_summary table.

This module provides the SQLModel class for the model_fee_summary table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ModelFeeSummary(RhizomeModel, table=False):
    """
    SQLModel for the `model_fee_summary` table.

    This model represents model fee summary records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
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
    fee_code_ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Fee Code Ledger Account Uuid")
    credit_ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Credit Ledger Account Uuid")
    debit_ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Debit Ledger Account Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> ModelFeeSummary:
        """Return a sanitized copy of this ModelFeeSummary instance."""
        return ModelFeeSummary(
            id=self.id,
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
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
