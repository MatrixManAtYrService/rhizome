"""
SQLModel definition for the merchant_terms_acceptance_events table.

This module provides the SQLModel class for the merchant_terms_acceptance_events table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantTermsAcceptanceEvents(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_terms_acceptance_events` table.

    This model represents merchant_terms_acceptance_events records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    acceptance_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    agreement_type: str | None = Field(default=None, max_length=128, description="agreement_type")
    account_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    acceptance_created: datetime.datetime = Field(description="acceptance_created")
    acceptance_modified: datetime.datetime | None = Field(default=None, description="acceptance_modified")
    acceptance_deleted: datetime.datetime | None = Field(default=None, description="acceptance_deleted")
    action: str | None = Field(default=None, max_length=100, description="action")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> MerchantTermsAcceptanceEvents:
        """Return a sanitized copy of this MerchantTermsAcceptanceEvents instance."""
        return MerchantTermsAcceptanceEvents(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            merchant_id=self.merchant_id,
            acceptance_id=self.acceptance_id,
            agreement_type=self.agreement_type,
            account_id=self.account_id,
            acceptance_created=self.acceptance_created,
            acceptance_modified=self.acceptance_modified,
            acceptance_deleted=self.acceptance_deleted,
            action=self.action,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
