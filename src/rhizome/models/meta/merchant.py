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

    def sanitize(self) -> Merchant:
        """Return a sanitized copy of this Merchant instance."""
        from ...sanitize_helpers import sanitize_uuid_field

        return Merchant(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13) or self.uuid,
            name=self.name,
            reseller_id=self.reseller_id,
            owner_account_id=self.owner_account_id,
            address_id=self.address_id,
            timezone_id=self.timezone_id,
            default_currency=self.default_currency,
            phone_number=self.phone_number,
            website=self.website,
            created_time=self.created_time,
            merchant_gateway_id=self.merchant_gateway_id,
            merchant_plan_id=self.merchant_plan_id,
            tax_rate=self.tax_rate,
            tips_enabled=self.tips_enabled,
            receipt_properties=self.receipt_properties,
            summary_hour=self.summary_hour,
            last_summary_order_id=self.last_summary_order_id,
            subscription_id=self.subscription_id,
            levelup_auth_token=self.levelup_auth_token,
            levelup_merchant_id=self.levelup_merchant_id,
            levelup_location_id=self.levelup_location_id,
            signature_threshold=self.signature_threshold,
            tip_rate_default=self.tip_rate_default,
            on_paper_tip_signatures=self.on_paper_tip_signatures,
            force_signature_verify=self.force_signature_verify,
            auto_logout=self.auto_logout,
            order_title=self.order_title,
            order_title_max=self.order_title_max,
            reset_on_reporting_time=self.reset_on_reporting_time,
            notes_on_orders=self.notes_on_orders,
            delete_orders=self.delete_orders,
            cash_management_enabled=self.cash_management_enabled,
            remove_tax_enabled=self.remove_tax_enabled,
            group_line_items=self.group_line_items,
            alternate_inventory_names=self.alternate_inventory_names,
            auto_print=self.auto_print,
            hardware_profile=self.hardware_profile,
            shipping_address=self.shipping_address,
            marketing_preference_id=self.marketing_preference_id,
            bank_marker=self.bank_marker,
            support_phone=self.support_phone,
            support_email=self.support_email,
            debug_enabled=self.debug_enabled,
            manual_closeout=self.manual_closeout,
            stay_in_category=self.stay_in_category,
            locale_id=self.locale_id,
            is_vat=self.is_vat,
            vat_tax_name=self.vat_tax_name,
            track_stock=self.track_stock,
            update_stock=self.update_stock,
            allow_clock_out_with_open_orders=self.allow_clock_out_with_open_orders,
            log_in_clock_in_prompt=self.log_in_clock_in_prompt,
            account_type=self.account_type,
            pin_length=self.pin_length,
            cash_back_enabled=self.cash_back_enabled,
            cash_back_options=self.cash_back_options,
            cluster_id=self.cluster_id,
            offline_opted_in=self.offline_opted_in,
            offline_job_notification_time=self.offline_job_notification_time,
            max_cash_back=self.max_cash_back,
            business_type_code=self.business_type_code,
            hierarchy=self.hierarchy,
            app_config_id=self.app_config_id,
            aba_account_number=self.aba_account_number,
            dda_account_number=self.dda_account_number,
            infolease_authorize_time=self.infolease_authorize_time,
            infolease_authorize_code=self.infolease_authorize_code,
            infolease_suppress_billing=self.infolease_suppress_billing,
            infolease_suppress_plan_billing=self.infolease_suppress_plan_billing,
            send_closeout_email=self.send_closeout_email,
            modified_time=self.modified_time,
            customer_service_email=self.customer_service_email,
            customer_contact_email=self.customer_contact_email,
        )
