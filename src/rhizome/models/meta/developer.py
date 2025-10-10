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
    developer_type: str | None = Field(default="EXTERNAL", max_length=16)
    approval_status_modified_time: datetime.datetime | None = Field(default=None)

    def sanitize(self) -> Developer:
        """Return a sanitized copy of this Developer instance."""
        from ...sanitize_helpers import sanitize_uuid_field

        return Developer(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13) or self.uuid,
            approval_status=self.approval_status,
            collection_approval_status=self.collection_approval_status,
            secret=self.secret,
            owner_account_id=self.owner_account_id,
            name=self.name,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            dob=self.dob,
            address=self.address,
            city=self.city,
            county=self.county,
            state=self.state,
            country=self.country,
            postal_code=self.postal_code,
            bank_routing_number=self.bank_routing_number,
            tin=self.tin,
            tin_dps_uuid=self.tin_dps_uuid,
            vat_register_number=self.vat_register_number,
            vat_dps_uuid=self.vat_dps_uuid,
            business_legal_name=self.business_legal_name,
            business_address=self.business_address,
            business_city=self.business_city,
            business_state=self.business_state,
            business_country=self.business_country,
            business_postal_code=self.business_postal_code,
            billing_status=self.billing_status,
            billing_status_message=self.billing_status_message,
            accepted_agreement=self.accepted_agreement,
            pr_name=self.pr_name,
            pr_email=self.pr_email,
            pr_phone=self.pr_phone,
            website=self.website,
            created_time=self.created_time,
            first_submitted_time=self.first_submitted_time,
            first_approval_time=self.first_approval_time,
            modified_time=self.modified_time,
            sensitive_data=self.sensitive_data,
            infolease_vendor_code=self.infolease_vendor_code,
            infolease_gl_code=self.infolease_gl_code,
            rev_share=self.rev_share,
            is_rev_share_flat_rate=self.is_rev_share_flat_rate,
            signor_name=self.signor_name,
            signor_title=self.signor_title,
            referral_submission_time=self.referral_submission_time,
            billing_contract_number=self.billing_contract_number,
            emergency_email=self.emergency_email,
            developer_type=self.developer_type,
            approval_status_modified_time=self.approval_status_modified_time,
        )
