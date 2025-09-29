"""
SQLModel definition for the merchant_terms_missing_acceptance table.

This module provides the SQLModel class for the merchant_terms_missing_acceptance table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantTermsMissingAcceptance(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_terms_missing_acceptance` table.

    This model represents merchant_terms_missing_acceptance records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    plan_charge_type: str | None = Field(default=None, description="plan_charge_type")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> MerchantTermsMissingAcceptance:
        """Return a sanitized copy of this MerchantTermsMissingAcceptance instance."""
        return MerchantTermsMissingAcceptance(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            merchant_id=self.merchant_id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            plan_charge_type=self.plan_charge_type,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
