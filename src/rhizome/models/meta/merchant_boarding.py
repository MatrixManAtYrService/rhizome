"""
SQLModel definition for the merchant_boarding table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantBoarding")


class MerchantBoarding(RhizomeModel, table=False):
    """
    Base MerchantBoarding model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int = Field(unique=True, foreign_key="merchant.id")
    bill_to_name: str | None = Field(default=None, max_length=50)
    merchant_data: str | None = Field(default=None, max_length=20)
    store: str | None = Field(default=None, max_length=30)
    daylight_savings: bool | None = Field(default=None)
    seasonal: bool | None = Field(default=None)
    trans_armor_key: str | None = Field(default=None, max_length=11)
    ach_bank_id: str | None = Field(default=None, max_length=15)
    credit_limit: int | None = Field(default=None)
    auth_limit: int | None = Field(default=None)
    sale_limit: int | None = Field(default=None)
    account_status: str | None = Field(default=None, max_length=23)
    tax_exempt: bool | None = Field(default=None)
    salesman: str | None = Field(default=None, max_length=24)
    value_link: bool | None = Field(default=None)
    value_link_mid: str | None = Field(default=None, max_length=11)
    alt_value_link_mid: str | None = Field(default=None, max_length=11)
    receipt_dba: str | None = Field(default=None, max_length=22)
    bank_number: str | None = Field(default=None, max_length=22)
    parent_merchant_id: str | None = Field(default=None, max_length=16)
    relationship_manager: str | None = Field(default=None, max_length=3)
    multi_merchant_type: str | None = Field(default=None, max_length=1)
    external_merchant: bool | None = Field(default=None)
    dynamic_dba: bool | None = Field(default=None)
    fax_phone: str | None = Field(default=None, max_length=10)
    merchant_type: str | None = Field(default=None, max_length=125)
    multi_currency_indicator: str | None = Field(default=None, max_length=50)
    preferred_merchant: str | None = Field(default=None, max_length=1)
    visa_iram: str | None = Field(default=None, max_length=1)
    trans_armor_indicator: str | None = Field(default=None, max_length=100)
    signing_key: str | None = Field(default=None, max_length=2)
    visa_debit_accept: str | None = Field(default=None, max_length=1)
    mastercard_debit_accept: str | None = Field(default=None, max_length=1)
    source_indicator: str | None = Field(default=None, max_length=1)
    foreign_domestic_indicator: str | None = Field(default=None, max_length=1)
    account_funding: str | None = Field(default=None, max_length=1)
    direct_marketing: str | None = Field(default=None, max_length=1)
    participant_relationship: str | None = Field(default=None, max_length=1)
    process_settlement: str | None = Field(default=None, max_length=1)
    recurring_flag: str | None = Field(default=None, max_length=1)
    link_from: str | None = Field(default=None, max_length=9)
    link_to: str | None = Field(default=None, max_length=9)
    emv_allowed: str | None = Field(default=None, max_length=1)
    previous_account_status: str | None = Field(default=None, max_length=2)
    lease_company_code: str | None = Field(default=None, max_length=2)
    process_mode: bool | None = Field(default=None)
    agent_bank_indicator: str | None = Field(default=None, max_length=1)
    non_mpa_indicator: str | None = Field(default=None, max_length=1)
    internet_indicator: str | None = Field(default=None, max_length=1)
    charge_back_retrieval_address_flag: str | None = Field(default=None, max_length=1)
    vi_relationship_participant: str | None = Field(default=None, max_length=1)
    retail_description: str | None = Field(default=None, max_length=22)
    client_representative: str | None = Field(default=None, max_length=30)
    merchant_auth_type: str | None = Field(default=None, max_length=1)
    sys_prin: str | None = Field(default=None, max_length=10)
    tax_id: str | None = Field(default=None, max_length=40)
    business_type: str | None = Field(default=None, max_length=15)
    partner_id: str | None = Field(default=None, max_length=64)
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    account_status_modified_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantBoarding instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
