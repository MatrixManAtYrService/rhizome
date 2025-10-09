"""
SQLModel definition for the settlement_action table.

This module provides the SQLModel class for the settlement_action table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class SettlementAction(RhizomeModel, table=False):
    """
    SQLModel for the `settlement_action` table.

    This model represents settlement action records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    settlement_uuid: str = Field(max_length=26, description="Settlement Uuid")
    action_date: datetime.date = Field(description="Action Date")
    action: str = Field(max_length=25, description="Action")
    currency: str = Field(max_length=3, description="Currency")
    total_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total Amount")
    fee_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Fee Amount")
    tax1_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Tax1 Amount")
    tax2_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Tax2 Amount")
    tax3_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Tax3 Amount")
    tax4_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Tax4 Amount")
    reject_code: str | None = Field(default=None, max_length=10, description="Reject Code")
    message: str | None = Field(default=None, max_length=1024, description="Message")
    ledger_account_transition_uuid: str | None = Field(default=None, max_length=26, description="Ledger Account Transition Uuid")
    credit_ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Credit Ledger Account Uuid")
    debit_ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Debit Ledger Account Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> SettlementAction:
        """Return a sanitized copy of this SettlementAction instance."""
        return SettlementAction(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            settlement_uuid=sanitize_uuid_field(self.settlement_uuid, 26),  # type: ignore
            action_date=self.action_date,
            action=self.action,
            currency=self.currency,
            total_amount=self.total_amount,
            fee_amount=self.fee_amount,
            tax1_amount=self.tax1_amount,
            tax2_amount=self.tax2_amount,
            tax3_amount=self.tax3_amount,
            tax4_amount=self.tax4_amount,
            reject_code=self.reject_code,
            message=self.message,
            ledger_account_transition_uuid=sanitize_uuid_field(self.ledger_account_transition_uuid, 26),
            credit_ledger_account_uuid=sanitize_uuid_field(self.credit_ledger_account_uuid, 26),
            debit_ledger_account_uuid=sanitize_uuid_field(self.debit_ledger_account_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
