"""
SQLModel definition for the merchant_suppression_by_app table.

This module provides the SQLModel class for the merchant_suppression_by_app table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MerchantSuppressionByApp(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_suppression_by_app` table.

    This model represents merchant_suppression_by_app records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reference_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    plan_billable: bool | None = Field(default=None, description="plan_billable")
    app_billable: bool | None = Field(default=None, description="app_billable")
    plan_exportable: bool | None = Field(default=None, description="plan_exportable")
    app_exportable: bool | None = Field(default=None, description="app_exportable")
    context: str | None = Field(default=None, description="context")
    detail: str | None = Field(default=None, max_length=511, description="detail")
    start_time: datetime.datetime = Field(description="start_time")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    finalization_time: datetime.datetime | None = Field(default=None, description="finalization_time")

    def sanitize(self) -> MerchantSuppressionByApp:
        """Return a sanitized copy of this MerchantSuppressionByApp instance."""
        return MerchantSuppressionByApp(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            reference_id=self.reference_id,
            plan_billable=self.plan_billable,
            app_billable=self.app_billable,
            plan_exportable=self.plan_exportable,
            app_exportable=self.app_exportable,
            context=self.context,
            detail=self.detail,
            start_time=self.start_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
            finalization_time=self.finalization_time,
        )
