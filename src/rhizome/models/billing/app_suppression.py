"""
SQLModel definition for the app_suppression table.

This module provides the SQLModel class for the app_suppression table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class SuppressionContext(str, Enum):
    """Enum for suppression context values."""

    TRIAL = "TRIAL"
    DEMO = "DEMO"
    SUNSET = "SUNSET"
    OFFER = "OFFER"
    OVERRIDE = "OVERRIDE"
    SYSTEM = "SYSTEM"
    FIELD_TEST = "FIELD_TEST"
    OFF_BOARDED = "OFF_BOARDED"
    ACH_HOLD = "ACH_HOLD"
    PILOT = "PILOT"
    DEBIT_NO_AUTH = "DEBIT_NO_AUTH"
    PROMO = "PROMO"
    NO_CLOVER_APPS = "NO_CLOVER_APPS"
    SEASONAL = "SEASONAL"
    FINANCE_EXCEPTION = "FINANCE_EXCEPTION"


class AppSuppression(RhizomeModel, table=False):
    """
    SQLModel for the `app_suppression` table.

    This model represents app suppression records in the billing system,
    containing information about suppressed billing for specific apps.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True, description="Unique identifier for the app suppression")
    developer_app_id: int | None = Field(default=None, description="ID of the developer app")
    merchant_id: int | None = Field(default=None, description="ID of the merchant")
    reseller_id: int | None = Field(default=None, description="ID of the reseller")
    country_id: int | None = Field(default=None, description="ID of the country")
    app_id: int = Field(description="ID of the app")
    app_billable: bool = Field(default=True, description="Whether the app is billable")
    app_exportable: bool = Field(default=True, description="Whether the app is exportable")
    context: SuppressionContext = Field(description="Context for the suppression")
    detail: str | None = Field(default=None, max_length=511, description="Details about the suppression")
    start_time: datetime.datetime = Field(description="Start time of the suppression")
    created_time: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_time: datetime.datetime = Field(description="Timestamp when the record was last modified")
    finalization_time: datetime.datetime | None = Field(
        default=None, description="Time when the suppression was finalized"
    )

    def sanitize(self) -> AppSuppression:
        """Return a sanitized copy of this AppSuppression instance."""
        return AppSuppression(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            developer_app_id=self.developer_app_id,
            merchant_id=self.merchant_id,
            reseller_id=self.reseller_id,
            country_id=self.country_id,
            app_id=self.app_id,
            app_billable=self.app_billable,
            app_exportable=self.app_exportable,
            context=self.context,
            detail=self.detail,
            start_time=self.start_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
            finalization_time=self.finalization_time,
        )
