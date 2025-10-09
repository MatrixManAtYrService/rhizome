"""
SQLModel definition for the ledger_account_settlement table.

This module provides the SQLModel class for the ledger_account_settlement table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountSettlement(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_settlement` table.

    This model represents ledger account settlement records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_key: str = Field(max_length=32, description="Ledger Account Key")
    effective_date: datetime.date = Field(description="Effective Date")
    settlement_item_code: str | None = Field(default=None, max_length=30, description="Settlement Item Code")
    settlement_desc: str | None = Field(default=None, max_length=100, description="Settlement Desc")
    fee_category_group: str | None = Field(default=None, max_length=25, description="Fee Category Group")
    revenue_group: str | None = Field(default=None, max_length=25, description="Revenue Group")
    merchant_plan_uuid: str | None = Field(default=None, max_length=13, description="Merchant Plan Uuid")
    developer_uuid: str | None = Field(default=None, max_length=13, description="Developer Uuid")
    developer_app_uuid: str | None = Field(default=None, max_length=13, description="Developer App Uuid")
    app_subscription_uuid: str | None = Field(default=None, max_length=13, description="App Subscription Uuid")
    app_metered_uuid: str | None = Field(default=None, max_length=13, description="App Metered Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> LedgerAccountSettlement:
        """Return a sanitized copy of this LedgerAccountSettlement instance."""
        return LedgerAccountSettlement(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_key=self.ledger_account_key,
            effective_date=self.effective_date,
            settlement_item_code=self.settlement_item_code,
            settlement_desc=self.settlement_desc,
            fee_category_group=self.fee_category_group,
            revenue_group=self.revenue_group,
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),
            developer_uuid=sanitize_uuid_field(self.developer_uuid, 13),
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),
            app_metered_uuid=sanitize_uuid_field(self.app_metered_uuid, 13),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
