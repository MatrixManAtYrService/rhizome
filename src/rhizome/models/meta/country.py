"""
SQLModel definition for the country table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Country")


class Country(RhizomeModel, table=True):
    """
    SQLModel for the `country` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    country_code: str = Field(max_length=2, unique=True)
    default_currency: str = Field(max_length=3)
    default_locale_id: int = Field(foreign_key="locale.id")
    default_timezone_id: int = Field(foreign_key="timezones.id")
    state_province_required: bool | None = Field(default=False)
    zip_postal_required: bool | None = Field(default=False)
    county_required: bool | None = Field(default=False)
    app_market_billing_enabled: bool | None = Field(default=False)
    vat: bool | None = Field(default=False)

    def sanitize(self) -> Country:
        """Return a sanitized copy of this Country instance."""
        return Country(
            id=self.id,
            country_code=self.country_code,
            default_currency=self.default_currency,
            default_locale_id=self.default_locale_id,
            default_timezone_id=self.default_timezone_id,
            state_province_required=self.state_province_required,
            zip_postal_required=self.zip_postal_required,
            county_required=self.county_required,
            app_market_billing_enabled=self.app_market_billing_enabled,
            vat=self.vat,
        )
