"""
SQLModel definition for the merchant_terms_acceptance table.

This module provides the SQLModel class for the merchant_terms_acceptance table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantTermsAcceptance(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_terms_acceptance` table.

    This model represents merchant_terms_acceptance records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    acceptance_id: str | None = Field(default=None, description="UUID field")
    acceptance_created: datetime.datetime = Field(description="acceptance_created")
    acceptance_modified: datetime.datetime | None = Field(default=None, description="acceptance_modified")
    acceptance_deleted: datetime.datetime | None = Field(default=None, description="acceptance_deleted")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    agreement_type: str | None = Field(default=None, max_length=128, description="agreement_type")
    action: str | None = Field(default=None, description="action")

    def sanitize(self) -> MerchantTermsAcceptance:
        """Return a sanitized copy of this MerchantTermsAcceptance instance."""
        return MerchantTermsAcceptance(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            merchant_id=self.merchant_id,
            acceptance_id=self.acceptance_id,
            acceptance_created=self.acceptance_created,
            acceptance_modified=self.acceptance_modified,
            acceptance_deleted=self.acceptance_deleted,
            created_time=self.created_time,
            modified_time=self.modified_time,
            agreement_type=self.agreement_type,
            action=self.action,
        )
