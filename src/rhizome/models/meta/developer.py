"""
SQLModel definition for the developer table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Developer")


class Developer(RhizomeModel, table=True):
    """
    SQLModel for the `developer` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    approval_status: str = Field(max_length=8)
    collection_approval_status: str = Field(max_length=8)
    secret: str = Field(max_length=36)
    owner_account_id: int = Field(foreign_key="account.id")
    name: str = Field(max_length=127)
    first_name: str | None = Field(default=None, max_length=127)
    last_name: str | None = Field(default=None, max_length=127)
    email: str | None = Field(default=None, max_length=127)
    phone: str | None = Field(default=None, max_length=25)
    dob: str | None = Field(default=None, max_length=10)
    address: str | None = Field(default=None, max_length=255)
    city: str | None = Field(default=None, max_length=127)
    county: str | None = Field(default=None, max_length=127)
    state: str | None = Field(default=None, max_length=127)
    country: str | None = Field(default=None, max_length=2)
    postal_code: str | None = Field(default=None, max_length=20)
    bank_routing_number: str | None = Field(default=None, max_length=40)
    tin: str | None = Field(default=None, max_length=127)
    tin_dps_uuid: str | None = Field(default=None, max_length=127)
    vat_register_number: str | None = Field(default=None, max_length=127)
    vat_dps_uuid: str | None = Field(default=None, max_length=127)
    business_legal_name: str | None = Field(default=None, max_length=255)
    business_address: str | None = Field(default=None, max_length=255)
    business_city: str | None = Field(default=None, max_length=127)
    business_state: str | None = Field(default=None, max_length=127)
    business_country: str | None = Field(default=None, max_length=2)
    business_postal_code: str | None = Field(default=None, max_length=20)
    billing_status: str | None = Field(default=None, max_length=8)
    billing_status_message: str | None = Field(default=None, max_length=127)
    accepted_agreement: bool = Field(default=False)
    pr_name: str | None = Field(default=None, max_length=255)
    pr_email: str | None = Field(default=None, max_length=127)
    pr_phone: str | None = Field(default=None, max_length=25)
    website: str | None = Field(default=None, max_length=255)
    created_time: datetime.datetime | None = Field(default=None)
    first_submitted_time: datetime.datetime | None = Field(default=None)
    first_approval_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    sensitive_data: str | None = Field(default=None)
    infolease_vendor_code: str | None = Field(default=None, max_length=30, unique=True)
    infolease_gl_code: str | None = Field(default=None, max_length=10)
    rev_share: int | None = Field(default=7000)
    is_rev_share_flat_rate: bool | None = Field(default=False)
    signor_name: str | None = Field(default=None, max_length=127)
    signor_title: str | None = Field(default=None, max_length=127)
    referral_submission_time: datetime.datetime | None = Field(default=None)
    billing_contract_number: str | None = Field(default=None, max_length=128)
    emergency_email: str | None = Field(default=None, max_length=127)
    developer_type: str | None = Field(default='EXTERNAL', max_length=16)
    approval_status_modified_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this Developer instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
