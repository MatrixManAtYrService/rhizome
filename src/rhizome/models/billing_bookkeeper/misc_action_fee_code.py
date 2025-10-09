"""
SQLModel definition for the misc_action_fee_code table.

This module provides the SQLModel class for the misc_action_fee_code table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MiscActionFeeCode(RhizomeModel, table=False):
    """
    SQLModel for the `misc_action_fee_code` table.

    This model represents misc action fee code records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    misc_specifier: str = Field(max_length=25, description="Misc Specifier")
    misc_action_type: str = Field(max_length=25, description="Misc Action Type")
    effective_date: datetime.date = Field(description="Effective Date")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> MiscActionFeeCode:
        """Return a sanitized copy of this MiscActionFeeCode instance."""
        return MiscActionFeeCode(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            misc_specifier=self.misc_specifier,
            misc_action_type=self.misc_action_type,
            effective_date=self.effective_date,
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            deleted_date=self.deleted_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
