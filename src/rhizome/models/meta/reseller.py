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

    def sanitize(self) -> Reseller:
        """Return a sanitized copy of this Reseller instance."""
        from ...sanitize_helpers import sanitize_uuid_field

        return Reseller(
            id=self.id,
            parent_id=self.parent_id,
            uuid=sanitize_uuid_field(self.uuid, 13) or self.uuid,
            fd_client_id=self.fd_client_id,
            name=self.name,
            alternate_name=self.alternate_name,
            code=self.code,
            owner_account_id=self.owner_account_id,
            default_payment_processor_id=self.default_payment_processor_id,
            default_processor_key_id=self.default_processor_key_id,
            default_country_code=self.default_country_code,
            supports_naked_credit=self.supports_naked_credit,
            created_time=self.created_time,
            modified_time=self.modified_time,
            support_phone=self.support_phone,
            support_email=self.support_email,
            filter_apps=self.filter_apps,
            force_phone=self.force_phone,
            stations_on_classic=self.stations_on_classic,
            allow_blackhole=self.allow_blackhole,
            tasq_customer_number=self.tasq_customer_number,
            is_bulk_purchaser=self.is_bulk_purchaser,
            partner_support_email=self.partner_support_email,
            supports_outbound_boarding=self.supports_outbound_boarding,
            is_rki_identifier=self.is_rki_identifier,
            enforce_merchant_plan=self.enforce_merchant_plan,
            is_self_boarding=self.is_self_boarding,
            is_intercom_enabled=self.is_intercom_enabled,
            fdmp_configuration_id=self.fdmp_configuration_id,
            locale_id=self.locale_id,
            is_codeless_activation=self.is_codeless_activation,
            reseller_privacy_policy_url=self.reseller_privacy_policy_url,
            feedback_disabled=self.feedback_disabled,
            is_rapid_deposit_enabled=self.is_rapid_deposit_enabled,
            rapid_deposit_service_entitlement_number=self.rapid_deposit_service_entitlement_number,
            prohibit_tokenization=self.prohibit_tokenization,
            is_new_billing=self.is_new_billing,
            plan_group_id=self.plan_group_id,
            type=self.type,
            source=self.source,
        )
