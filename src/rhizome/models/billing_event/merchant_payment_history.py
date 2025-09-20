"""
SQLModel definition for the merchant_payment_history table.

This module provides the SQLModel class for the merchant_payment_history table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantPaymentHistory(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_payment_history` table.

    This model represents historical payment records for merchants in the billing system,
    containing payment amounts, dates, and billing event information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the payment history record")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    billing_entity_uuid: str = Field(max_length=26, description="UUID of the billing entity")
    payment_date: datetime.date = Field(description="Date of the payment")
    currency: str | None = Field(default=None, max_length=3, description="Currency code for the payment")
    total_amount: Decimal = Field(
        default=Decimal("0.000"), max_digits=12, decimal_places=3, description="Total payment amount"
    )
    num_payments: int = Field(default=0, description="Number of payments")
    billing_event_uuid: str = Field(max_length=26, description="UUID of the billing event")
    request_uuid: str | None = Field(default=None, max_length=26, description="UUID of the request")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> MerchantPaymentHistory:
        """Return a sanitized copy of this MerchantPaymentHistory instance."""
        return MerchantPaymentHistory(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            environment=self.environment,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            payment_date=self.payment_date,
            currency=self.currency,
            total_amount=self.total_amount,
            num_payments=self.num_payments,
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),  # type: ignore
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
