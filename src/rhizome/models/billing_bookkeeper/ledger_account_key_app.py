"""
SQLModel definition for the ledger_account_key_app table.

This module provides the SQLModel class for the ledger_account_key_app table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountKeyApp(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_key_app` table.

    This model represents ledger account key app records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_key: str = Field(max_length=32, description="Ledger Account Key")
    developer_uuid: str = Field(max_length=13, description="Developer Uuid")
    developer_app_uuid: str | None = Field(default=None, max_length=13, description="Developer App Uuid")
    app_subscription_uuid: str | None = Field(default=None, max_length=13, description="App Subscription Uuid")
    app_metered_uuid: str | None = Field(default=None, max_length=13, description="App Metered Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> LedgerAccountKeyApp:
        """Return a sanitized copy of this LedgerAccountKeyApp instance."""
        return LedgerAccountKeyApp(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_key=self.ledger_account_key,
            developer_uuid=sanitize_uuid_field(self.developer_uuid, 13),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),
            app_metered_uuid=sanitize_uuid_field(self.app_metered_uuid, 13),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
