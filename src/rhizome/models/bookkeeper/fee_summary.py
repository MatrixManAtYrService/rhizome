"""
SQLModel definition for the fee_summary table.

This module provides the SQLModel class for the fee_summary table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field, SQLModel

from ...sanitize_helpers import sanitize_uuid_field


class FeeSummary(SQLModel, table=True):
    """
    SQLModel for the `fee_summary` table.

    This model represents fee summary records in the billing system,
    containing aggregated fee information for billing entities.
    """

    __tablename__ = "fee_summary"  # type: ignore

    id: int = Field(primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the fee summary")
    billing_entity_uuid: str = Field(max_length=26, description="UUID of the billing entity")
    billing_date: datetime.date = Field(description="Date for which the fee is being calculated")
    fee_category: str = Field(max_length=25, description="Category of the fee")
    fee_code: str = Field(max_length=25, description="Code identifying the specific fee type")
    currency: str = Field(max_length=3, description="Currency code (ISO 4217)")
    total_period_units: Decimal = Field(
        max_digits=12, decimal_places=4, description="Total units for the billing period"
    )
    abs_period_units: Decimal = Field(
        max_digits=12, decimal_places=4, description="Absolute units for the billing period"
    )
    total_basis_amount: Decimal = Field(
        max_digits=12, decimal_places=3, description="Total basis amount for fee calculation"
    )
    abs_basis_amount: Decimal = Field(
        max_digits=12, decimal_places=3, description="Absolute basis amount for fee calculation"
    )
    total_fee_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total calculated fee amount")
    fee_rate_uuid: str = Field(max_length=26, description="UUID of the fee rate used")
    request_uuid: str = Field(max_length=26, description="UUID of the request that generated this fee")
    invoice_info_uuid: str | None = Field(default=None, max_length=26, description="UUID of associated invoice info")
    fee_code_ledger_account_uuid: str | None = Field(
        default=None, max_length=26, description="UUID of fee code ledger account"
    )
    credit_ledger_account_uuid: str | None = Field(
        default=None, max_length=26, description="UUID of credit ledger account"
    )
    debit_ledger_account_uuid: str | None = Field(
        default=None, max_length=26, description="UUID of debit ledger account"
    )
    exclude_from_invoice: int = Field(description="Flag indicating if this fee should be excluded from invoicing")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")


def sanitize(fee_summary: FeeSummary) -> FeeSummary:
    """
    Sanitize a FeeSummary instance for safe use in testing/analysis.

    This function creates a copy of the fee summary with UUIDs replaced by
    deterministic SHA256 hashes encoded in base58, maintaining the original
    character length and prefixed with "Hash".

    Args:
        fee_summary: The FeeSummary instance to sanitize

    Returns:
        FeeSummary: A sanitized copy of the fee summary
    """
    # Create a new instance without session state to avoid SQLAlchemy issues
    sanitized = FeeSummary(
        id=fee_summary.id,
        uuid=sanitize_uuid_field(fee_summary.uuid, 26),  # type: ignore
        billing_entity_uuid=sanitize_uuid_field(fee_summary.billing_entity_uuid, 26),  # type: ignore
        billing_date=fee_summary.billing_date,
        fee_category=fee_summary.fee_category,
        fee_code=fee_summary.fee_code,
        currency=fee_summary.currency,
        total_period_units=fee_summary.total_period_units,
        abs_period_units=fee_summary.abs_period_units,
        total_basis_amount=fee_summary.total_basis_amount,
        abs_basis_amount=fee_summary.abs_basis_amount,
        total_fee_amount=fee_summary.total_fee_amount,
        fee_rate_uuid=sanitize_uuid_field(fee_summary.fee_rate_uuid, 26),  # type: ignore
        request_uuid=sanitize_uuid_field(fee_summary.request_uuid, 26),  # type: ignore
        invoice_info_uuid=sanitize_uuid_field(fee_summary.invoice_info_uuid, 26),
        fee_code_ledger_account_uuid=sanitize_uuid_field(fee_summary.fee_code_ledger_account_uuid, 26),
        credit_ledger_account_uuid=sanitize_uuid_field(fee_summary.credit_ledger_account_uuid, 26),
        debit_ledger_account_uuid=sanitize_uuid_field(fee_summary.debit_ledger_account_uuid, 26),
        exclude_from_invoice=fee_summary.exclude_from_invoice,
        created_timestamp=fee_summary.created_timestamp,
        modified_timestamp=fee_summary.modified_timestamp,
    )

    return sanitized
