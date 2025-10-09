"""
SQLModel definition for the adjust_action_fee_code table.

This module provides the SQLModel class for the adjust_action_fee_code table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AdjustActionFeeCode(RhizomeModel, table=False):
    """
    SQLModel for the `adjust_action_fee_code` table.

    This model represents adjust action fee code records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    developer_uuid: str | None = Field(default=None, max_length=13, description="Developer Uuid")
    developer_app_uuid: str | None = Field(default=None, max_length=13, description="Developer App Uuid")
    adjust_reason: str = Field(max_length=20, description="Adjust Reason")
    adjust_action_type: str = Field(max_length=25, description="Adjust Action Type")
    effective_date: datetime.date = Field(description="Effective Date")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> AdjustActionFeeCode:
        """Return a sanitized copy of this AdjustActionFeeCode instance."""
        return AdjustActionFeeCode(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            developer_uuid=sanitize_uuid_field(self.developer_uuid, 13),
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),
            adjust_reason=self.adjust_reason,
            adjust_action_type=self.adjust_action_type,
            effective_date=self.effective_date,
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            deleted_date=self.deleted_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
