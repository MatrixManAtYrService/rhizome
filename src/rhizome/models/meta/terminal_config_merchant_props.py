"""
SQLModel definition for the terminal_config_merchant_props table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="TerminalConfigMerchantProps")


class TerminalConfigMerchantProps(RhizomeModel, table=False):
    """
    Base TerminalConfigMerchantProps model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    country: str | None = Field(default=None, max_length=2)
    currency: str | None = Field(default=None, max_length=3)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this TerminalConfigMerchantProps instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
