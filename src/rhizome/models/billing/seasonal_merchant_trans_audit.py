"""
SQLModel definition for the seasonal_merchant_trans_audit table.

This module provides the SQLModel class for the seasonal_merchant_trans_audit table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class SeasonalMerchantTransAudit(RhizomeModel, table=False):
    """
    SQLModel for the `seasonal_merchant_trans_audit` table.

    This model represents seasonal_merchant_trans_audit records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    bill_cycle: datetime.date = Field(description="bill_cycle")
    seasonal_event: str | None = Field(default=None, description="seasonal_event")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> SeasonalMerchantTransAudit:
        """Return a sanitized copy of this SeasonalMerchantTransAudit instance."""
        return SeasonalMerchantTransAudit(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            merchant_id=self.merchant_id,
            bill_cycle=self.bill_cycle,
            seasonal_event=self.seasonal_event,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
