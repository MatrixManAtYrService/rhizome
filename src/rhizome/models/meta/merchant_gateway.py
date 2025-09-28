"""
SQLModel definition for the merchant_gateway table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantGateway")


class MerchantGateway(RhizomeModel, table=True):
    """
    SQLModel for the `merchant_gateway` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    merchant_id: int | None = Field(default=None)
    payment_processor_id: int
    processor_key_id: int | None = Field(default=None, foreign_key="processor_key.id")
    rki_processor_id: int | None = Field(default=None)
    partner_uuid: str | None = Field(default=None, max_length=64)
    stan: int = Field(default=0)
    config: str | None = Field(default=None)
    closing_time: str | None = Field(default=None, max_length=5)
    new_batch_close_enabled: bool = Field(default=False)
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantGateway instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
