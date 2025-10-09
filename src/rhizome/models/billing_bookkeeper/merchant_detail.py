"""
SQLModel definition for the merchant_detail table.

This module provides the SQLModel class for the merchant_detail table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantDetail(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_detail` table.

    This model represents merchant detail records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    seasonal: int = Field(description="Seasonal")
    tax_exempt: int = Field(description="Tax Exempt")
    verified_terms_acceptance: int = Field(description="Verified Terms Acceptance")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> MerchantDetail:
        """Return a sanitized copy of this MerchantDetail instance."""
        return MerchantDetail(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            seasonal=self.seasonal,
            tax_exempt=self.tax_exempt,
            verified_terms_acceptance=self.verified_terms_acceptance,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
