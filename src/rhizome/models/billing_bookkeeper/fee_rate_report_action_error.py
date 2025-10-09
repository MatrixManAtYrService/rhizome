"""
SQLModel definition for the fee_rate_report_action_error table.

This module provides the SQLModel class for the fee_rate_report_action_error table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeRateReportActionError(RhizomeModel, table=False):
    """
    SQLModel for the `fee_rate_report_action_error` table.

    This model represents fee rate report action error records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    fee_rate_error_report_uuid: str = Field(max_length=26, description="Fee Rate Error Report Uuid")
    action_error_uuid: str = Field(max_length=26, description="Action Error Uuid")
    action_type: str = Field(max_length=25, description="Action Type")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> FeeRateReportActionError:
        """Return a sanitized copy of this FeeRateReportActionError instance."""
        return FeeRateReportActionError(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            fee_rate_error_report_uuid=sanitize_uuid_field(self.fee_rate_error_report_uuid, 26),  # type: ignore
            action_error_uuid=sanitize_uuid_field(self.action_error_uuid, 26),  # type: ignore
            action_type=self.action_type,
            created_timestamp=self.created_timestamp,
        )
