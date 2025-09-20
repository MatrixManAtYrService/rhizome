"""
SQLModel definition for the merchant_payment table.

This module provides the SQLModel class for the merchant_payment table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantPayment(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_payment` table.

    This model represents merchant payment records in the billing system,
    containing payment requests and billing entity information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the merchant payment")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    billing_entity_uuid: str = Field(max_length=26, description="UUID of the billing entity")
    requested_thru_date: datetime.date = Field(description="Date through which payment is requested")
    request_uuid: str | None = Field(default=None, max_length=26, description="UUID of the request")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> MerchantPayment:
        """Return a sanitized copy of this MerchantPayment instance."""
        return MerchantPayment(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            environment=self.environment,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            requested_thru_date=self.requested_thru_date,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
