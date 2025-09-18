"""
SQLModel definition for the merchant_acceptance table.

This module provides the SQLModel class for the merchant_acceptance table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AgreementEventType(StrEnum):
    """Enum for agreement_event_type field values."""

    CREATED = "CREATED"
    INVALIDATED = "INVALIDATED"


class AcceptanceAction(StrEnum):
    """Enum for action field values."""

    ACCEPTED = "ACCEPTED"
    STALE = "STALE"
    REVOKED = "REVOKED"
    DECLINED = "DECLINED"
    REREQUESTED = "REREQUESTED"
    OFFBOARDED = "OFFBOARDED"
    UNKNOWN = "UNKNOWN"


class MerchantAcceptance(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_acceptance` table.

    This model represents merchant acceptance records in the billing system,
    tracking agreement acceptances and their current status.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing unsigned bigint")
    uuid: str = Field(max_length=26, description="UUID identifier for the merchant acceptance")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    account_id: str = Field(max_length=13, description="Account identifier")
    acceptance_id: str = Field(max_length=36, description="Acceptance identifier")
    agreement_id: str = Field(max_length=36, description="Agreement identifier")
    agreement_type: str = Field(max_length=25, description="Type of agreement")
    agreement_event_type: AgreementEventType = Field(description="Event type for the agreement")
    action: AcceptanceAction = Field(description="Action taken on the acceptance")
    acceptance_created_datetime: datetime.datetime | None = Field(default=None, description="When the acceptance was created")
    acceptance_modified_datetime: datetime.datetime | None = Field(default=None, description="When the acceptance was modified")
    acceptance_deleted_datetime: datetime.datetime | None = Field(default=None, description="When the acceptance was deleted")
    acceptance_expiration_datetime: datetime.datetime | None = Field(default=None, description="When the acceptance expires")
    serial_number: str | None = Field(default=None, max_length=32, description="Device serial number")
    iccid: str | None = Field(default=None, max_length=22, description="ICCID of the device")
    is_oobe: bool | None = Field(default=None, description="Whether this is an out-of-box experience")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> MerchantAcceptance:
        """Return a sanitized copy of this MerchantAcceptance instance."""
        return MerchantAcceptance(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            account_id=sanitize_uuid_field(self.account_id, 13),  # type: ignore
            acceptance_id=sanitize_uuid_field(self.acceptance_id, 36),  # type: ignore
            agreement_id=sanitize_uuid_field(self.agreement_id, 36),  # type: ignore
            agreement_type=self.agreement_type,
            agreement_event_type=self.agreement_event_type,
            action=self.action,
            acceptance_created_datetime=self.acceptance_created_datetime,
            acceptance_modified_datetime=self.acceptance_modified_datetime,
            acceptance_deleted_datetime=self.acceptance_deleted_datetime,
            acceptance_expiration_datetime=self.acceptance_expiration_datetime,
            serial_number=self.serial_number,
            iccid=self.iccid,
            is_oobe=self.is_oobe,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )