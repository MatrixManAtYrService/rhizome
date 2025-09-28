"""
SQLModel definition for the payment_processor table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="PaymentProcessor")


class PaymentProcessor(RhizomeModel, table=False):
    """
    Base PaymentProcessor model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    name: str | None = Field(default=None, max_length=127)
    payment_gateway_api: str = Field(max_length=31)
    production: bool
    config: str | None = Field(default=None)
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this PaymentProcessor instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
