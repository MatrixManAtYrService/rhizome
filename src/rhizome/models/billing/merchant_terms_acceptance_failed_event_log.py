"""
SQLModel definition for the merchant_terms_acceptance_failed_event_log table.

This module provides the SQLModel class for the merchant_terms_acceptance_failed_event_log table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantTermsAcceptanceFailedEventLog(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_terms_acceptance_failed_event_log` table.

    This model represents merchant_terms_acceptance_failed_event_log records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    message_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    raw_data: str = Field(description="raw_data")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> MerchantTermsAcceptanceFailedEventLog:
        """Return a sanitized copy of this MerchantTermsAcceptanceFailedEventLog instance."""
        return MerchantTermsAcceptanceFailedEventLog(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            message_id=self.message_id,
            raw_data=self.raw_data,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
