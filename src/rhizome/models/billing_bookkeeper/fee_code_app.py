"""
SQLModel definition for the fee_code_app table.

This module provides the SQLModel class for the fee_code_app table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeCodeApp(RhizomeModel, table=False):
    """
    SQLModel for the `fee_code_app` table.

    This model represents fee code app records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    developer_uuid: str = Field(max_length=13, description="Developer Uuid")
    developer_app_uuid: str | None = Field(default=None, max_length=13, description="Developer App Uuid")
    app_subscription_uuid: str | None = Field(default=None, max_length=13, description="App Subscription Uuid")
    app_metered_uuid: str | None = Field(default=None, max_length=13, description="App Metered Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeCodeApp:
        """Return a sanitized copy of this FeeCodeApp instance."""
        return FeeCodeApp(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            developer_uuid=sanitize_uuid_field(self.developer_uuid, 13),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),
            app_metered_uuid=sanitize_uuid_field(self.app_metered_uuid, 13),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
