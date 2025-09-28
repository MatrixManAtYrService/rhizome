"""
SQLModel definition for the merchant_app table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantApp")


class MerchantApp(RhizomeModel, table=True):
    """
    SQLModel for the `merchant_app` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    app_id: int = Field(foreign_key="developer_app.id")
    merchant_id: int
    app_subscription_id: int = Field(foreign_key="app_subscription.id")
    billing_start_time: datetime.datetime | None = Field(default=None)
    deleted_time: datetime.datetime | None = Field(default=None)
    permission_merchant_read: bool | None = Field(default=False)
    permission_merchant_write: bool | None = Field(default=False)
    permission_process_cards: bool = Field(default=False)
    permission_mid_read: bool | None = Field(default=False)
    permission_customers_read: bool | None = Field(default=False)
    permission_customers_write: bool | None = Field(default=False)
    permission_customers_address_read: int | None = Field(default=0)
    permission_customers_address_write: int | None = Field(default=0)
    permission_customers_email_read: int | None = Field(default=0)
    permission_customers_email_write: int | None = Field(default=0)
    permission_customers_phone_read: int | None = Field(default=0)
    permission_customers_phone_write: int | None = Field(default=0)
    permission_customers_businessname_read: int | None = Field(default=0)
    permission_customers_businessname_write: int | None = Field(default=0)
    permission_customers_birthdate_read: int | None = Field(default=0)
    permission_customers_birthdate_write: int | None = Field(default=0)
    permission_customers_note_read: int | None = Field(default=0)
    permission_customers_note_write: int | None = Field(default=0)
    permission_customers_card_read: int | None = Field(default=0)
    permission_customers_card_write: int | None = Field(default=0)
    permission_customers_ach_read: int | None = Field(default=0)
    permission_customers_ach_write: int | None = Field(default=0)
    permission_customers_marketing_read: int | None = Field(default=0)
    permission_customers_marketing_write: int | None = Field(default=0)
    permission_inventory_read: bool | None = Field(default=False)
    permission_inventory_write: bool | None = Field(default=False)
    permission_orders_read: bool | None = Field(default=False)
    permission_orders_write: bool | None = Field(default=False)
    permission_payments_read: bool | None = Field(default=False)
    permission_payments_write: bool | None = Field(default=False)
    permission_employees_read: bool | None = Field(default=False)
    permission_employees_write: bool | None = Field(default=False)
    launched_in_web_browser_count: int = Field(default=0)
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    uninstall_type: str | None = Field(default=None, max_length=23)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantApp instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
