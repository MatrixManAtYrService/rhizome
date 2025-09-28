"""
SQLModel definition for the reseller table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Reseller")


class Reseller(RhizomeModel, table=True):
    """
    SQLModel for the `reseller` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    parent_id: int | None = Field(default=None, foreign_key="reseller.id")
    uuid: str = Field(max_length=13, unique=True)
    fd_client_id: str | None = Field(default=None, max_length=10)
    name: str = Field(max_length=127)
    alternate_name: str | None = Field(default=None, max_length=127)
    code: str | None = Field(default=None, max_length=20, unique=True)
    owner_account_id: int = Field(foreign_key="account.id")
    default_payment_processor_id: int | None = Field(default=None, foreign_key="payment_processor.id")
    default_processor_key_id: int | None = Field(default=None, foreign_key="processor_key.id")
    default_country_code: str | None = Field(default=None, max_length=2)
    supports_naked_credit: bool | None = Field(default=True)
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    support_phone: str | None = Field(default=None, max_length=25)
    support_email: str | None = Field(default=None, max_length=127)
    filter_apps: bool | None = Field(default=False)
    force_phone: bool | None = Field(default=False)
    stations_on_classic: bool = Field(default=True)
    allow_blackhole: bool | None = Field(default=False)
    tasq_customer_number: str | None = Field(default=None, max_length=7)
    is_bulk_purchaser: bool | None = Field(default=False)
    partner_support_email: str | None = Field(default=None, max_length=127)
    supports_outbound_boarding: bool = Field(default=False)
    is_rki_identifier: bool = Field(default=False)
    enforce_merchant_plan: bool | None = Field(default=False)
    is_self_boarding: bool | None = Field(default=False)
    is_intercom_enabled: bool | None = Field(default=True)
    fdmp_configuration_id: int | None = Field(default=None, foreign_key="fdmp_configuration.id")
    locale_id: int | None = Field(default=None)
    is_codeless_activation: bool | None = Field(default=False)
    reseller_privacy_policy_url: str | None = Field(default=None, max_length=2083)
    feedback_disabled: bool = Field(default=False)
    is_rapid_deposit_enabled: bool = Field(default=False)
    rapid_deposit_service_entitlement_number: str | None = Field(default=None, max_length=128)
    prohibit_tokenization: bool = Field(default=False)
    is_new_billing: int = Field(default=1)
    plan_group_id: int | None = Field(default=None, foreign_key="merchant_plan_group.id")
    type: str | None = Field(default=None, max_length=18)
    source: str = Field(default='INTERNAL', max_length=8)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this Reseller instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
