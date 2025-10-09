"""
SQLModel definition for the app_sub_action_error table.

This module provides the SQLModel class for the app_sub_action_error table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AppSubActionError(RhizomeModel, table=False):
    """
    SQLModel for the `app_sub_action_error` table.

    This model represents app sub action error records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    app_sub_action_uuid: str = Field(max_length=26, description="App Sub Action Uuid")
    request_uuid: str = Field(max_length=26, description="Request Uuid")
    posting_date: datetime.date = Field(description="Posting Date")
    original_request_uuid: str = Field(max_length=26, description="Original Request Uuid")
    original_posting_date: datetime.date = Field(description="Original Posting Date")
    posting_attempts: int = Field(default=None, description="Posting Attempts")
    error_code: str = Field(max_length=25, description="Error Code")
    error_details: str | None = Field(default=None, description="Error Details")
    resolved: int = Field(default=None, description="Resolved")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> AppSubActionError:
        """Return a sanitized copy of this AppSubActionError instance."""
        return AppSubActionError(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            app_sub_action_uuid=sanitize_uuid_field(self.app_sub_action_uuid, 26),  # type: ignore
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),  # type: ignore
            posting_date=self.posting_date,
            original_request_uuid=sanitize_uuid_field(self.original_request_uuid, 26),  # type: ignore
            original_posting_date=self.original_posting_date,
            posting_attempts=self.posting_attempts,
            error_code=self.error_code,
            error_details=self.error_details,
            resolved=self.resolved,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
