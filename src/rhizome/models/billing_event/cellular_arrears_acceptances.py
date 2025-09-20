"""
SQLModel definition for the cellular_arrears_acceptances table.

This module provides the SQLModel class for the cellular_arrears_acceptances table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CellularArrearsAcceptanceStatus(StrEnum):
    """Enum for cellular arrears acceptance status."""

    INPROGRESS = "INPROGRESS"
    COMPLETE = "COMPLETE"
    ERROR = "ERROR"
    SKIPPED = "SKIPPED"


class CellularArrearsAcceptances(RhizomeModel, table=False):
    """
    SQLModel for the `cellular_arrears_acceptances` table.

    This model represents cellular arrears acceptance records, tracking device
    activation and deactivation information for cellular billing arrears.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_uuid: str | None = Field(default=None, max_length=13, description="UUID of the merchant")
    request_uuid: str = Field(max_length=30, description="UUID of the request")
    acceptance_id: str | None = Field(default=None, max_length=36, description="ID of the acceptance")
    agreement_id: str | None = Field(default=None, max_length=36, description="ID of the agreement")
    device_serial: str | None = Field(default=None, max_length=16, description="Serial number of the device")
    activation_date: datetime.datetime | None = Field(default=None, description="Date when device was activated")
    deactivation_date: datetime.datetime | None = Field(default=None, description="Date when device was deactivated")
    deleted_date: datetime.datetime | None = Field(default=None, description="Date when record was deleted")
    num_days_prorated: int | None = Field(default=None, description="Number of prorated days")
    iccid: str | None = Field(default=None, max_length=26, description="ICCID of the cellular device")
    status: CellularArrearsAcceptanceStatus | None = Field(default=None, description="Status of the acceptance")
    is_oobe: bool = Field(default=False, description="Whether this is out-of-box experience")
    reason: str | None = Field(default=None, max_length=255, description="Reason for the acceptance")

    def sanitize(self) -> CellularArrearsAcceptances:
        """Return a sanitized copy of this CellularArrearsAcceptances instance."""
        return CellularArrearsAcceptances(
            id=self.id,
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),
            request_uuid=sanitize_uuid_field(self.request_uuid, 30),  # type: ignore
            acceptance_id=sanitize_uuid_field(self.acceptance_id, 36),
            agreement_id=sanitize_uuid_field(self.agreement_id, 36),
            device_serial=self.device_serial,
            activation_date=self.activation_date,
            deactivation_date=self.deactivation_date,
            deleted_date=self.deleted_date,
            num_days_prorated=self.num_days_prorated,
            iccid=self.iccid,
            status=self.status,
            is_oobe=self.is_oobe,
            reason=self.reason,
        )
