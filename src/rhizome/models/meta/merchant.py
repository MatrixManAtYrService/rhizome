"""
SQLModel definition for the merchant table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Merchant")


class Merchant(RhizomeModel, table=True):
    """
    SQLModel for the `merchant` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    name: str = Field(max_length=127)
    reseller_id: int = Field(foreign_key="reseller.id")
    owner_account_id: int
    address_id: int | None = Field(default=None, unique=True, foreign_key="merchant_address.id")
    timezone_id: int | None = Field(default=None, foreign_key="timezones.id")
    default_currency: str = Field(max_length=3)
    phone_number: str | None = Field(default=None, max_length=21)
    website: str | None = Field(default=None, max_length=255)
    created_time: datetime.datetime | None = Field(default=None)
    merchant_gateway_id: int | None = Field(default=None, foreign_key="merchant_gateway.id")
    merchant_plan_id: int | None = Field(default=None)
    tax_rate: int | None = Field(default=None)
    tips_enabled: bool | None = Field(default=False)
    receipt_properties: str | None = Field(default=None)
    summary_hour: int = Field(default=0)
    last_summary_order_id: int | None = Field(default=None)
    subscription_id: int | None = Field(default=None, foreign_key="subscription.id")
    levelup_auth_token: str | None = Field(default=None, max_length=255)
    levelup_merchant_id: int | None = Field(default=None)
    levelup_location_id: int | None = Field(default=None)
    signature_threshold: int | None = Field(default=0)
    tip_rate_default: int | None = Field(default=1500)
    on_paper_tip_signatures: bool | None = Field(default=None)
    force_signature_verify: bool | None = Field(default=None)
    auto_logout: bool = Field(default=False)
    order_title: str | None = Field(default='none', max_length=9)
    order_title_max: int | None = Field(default=99)
    reset_on_reporting_time: bool = Field(default=False)
    notes_on_orders: bool = Field(default=False)
    delete_orders: bool = Field(default=True)
    cash_management_enabled: bool = Field(default=True)
    remove_tax_enabled: bool = Field(default=False)
    group_line_items: bool = Field(default=True)
    alternate_inventory_names: bool = Field(default=False)
    auto_print: bool = Field(default=False)
    hardware_profile: str | None = Field(default=None, max_length=127)
    shipping_address: str | None = Field(default=None)
    marketing_preference_id: int | None = Field(default=None)
    bank_marker: int | None = Field(default=None)
    support_phone: str | None = Field(default=None, max_length=25)
    support_email: str | None = Field(default=None, max_length=127)
    debug_enabled: bool | None = Field(default=False)
    manual_closeout: bool | None = Field(default=False)
    stay_in_category: bool | None = Field(default=False)
    locale_id: int | None = Field(default=None, foreign_key="locale.id")
    is_vat: bool
    vat_tax_name: str | None = Field(default=None, max_length=255)
    track_stock: bool | None = Field(default=False)
    update_stock: bool | None = Field(default=False)
    allow_clock_out_with_open_orders: bool = Field(default=False)
    log_in_clock_in_prompt: bool = Field(default=True)
    account_type: str | None = Field(default=None, max_length=32)
    pin_length: int = Field(default=4)
    cash_back_enabled: bool = Field(default=False)
    cash_back_options: str | None = Field(default=None, max_length=255)
    cluster_id: int = Field(default=0)
    offline_opted_in: bool | None = Field(default=None)
    offline_job_notification_time: datetime.datetime | None = Field(default=None)
    max_cash_back: int | None = Field(default=None)
    business_type_code: str | None = Field(default=None, max_length=26)
    hierarchy: str | None = Field(default=None, max_length=255)
    app_config_id: int | None = Field(default=None)
    aba_account_number: str | None = Field(default=None, max_length=40)
    dda_account_number: str | None = Field(default=None, max_length=40)
    infolease_authorize_time: datetime.datetime | None = Field(default=None)
    infolease_authorize_code: str | None = Field(default=None, max_length=50)
    infolease_suppress_billing: bool = Field(default=False)
    infolease_suppress_plan_billing: bool = Field(default=False)
    send_closeout_email: bool | None = Field(default=False)
    modified_time: datetime.datetime
    customer_service_email: str | None = Field(default=None, max_length=127)
    customer_contact_email: str | None = Field(default=None, max_length=127)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this Merchant instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
