"""
SQLModel definition for the revenue_action_fee_code table.

This module provides the SQLModel class for the revenue_action_fee_code table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class RevenueActionFeeCode(RhizomeModel, table=False):
    """
    SQLModel for the `revenue_action_fee_code` table.

    This model represents revenue action fee code records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    fee_category_group: str = Field(max_length=25, description="Fee Category Group")
    revenue_group: str | None = Field(default=None, max_length=25, description="Revenue Group")
    revenue_share_group: str | None = Field(default=None, max_length=20, description="Revenue Share Group")
    developer_uuid: str | None = Field(default=None, max_length=13, description="Developer Uuid")
    developer_app_uuid: str | None = Field(default=None, max_length=13, description="Developer App Uuid")
    app_subscription_uuid: str | None = Field(default=None, max_length=13, description="App Subscription Uuid")
    app_metered_uuid: str | None = Field(default=None, max_length=13, description="App Metered Uuid")
    merchant_plan_uuid: str | None = Field(default=None, max_length=13, description="Merchant Plan Uuid")
    revenue_action_type: str = Field(max_length=25, description="Revenue Action Type")
    effective_date: datetime.date = Field(description="Effective Date")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> RevenueActionFeeCode:
        """Return a sanitized copy of this RevenueActionFeeCode instance."""
        return RevenueActionFeeCode(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            fee_category_group=self.fee_category_group,
            revenue_group=self.revenue_group,
            revenue_share_group=self.revenue_share_group,
            developer_uuid=sanitize_uuid_field(self.developer_uuid, 13),
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),
            app_metered_uuid=sanitize_uuid_field(self.app_metered_uuid, 13),
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),
            revenue_action_type=self.revenue_action_type,
            effective_date=self.effective_date,
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            deleted_date=self.deleted_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
