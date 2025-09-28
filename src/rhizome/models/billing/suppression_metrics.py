"""
SQLModel definition for the suppression_metrics table.

This module provides the SQLModel class for the suppression_metrics table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum
from typing import TypeVar

from sqlmodel import Field, SQLModel

T = TypeVar("T", bound="SuppressionMetrics")


class SuppTypeEnum(str, Enum):
    """Enum for supp_type values."""
    MERCHANT = "MERCHANT"
    APP = "APP"
    RESELLER = "RESELLER"
    COUNTRY = "COUNTRY"
    MERCHANT_BY_APP = "MERCHANT_BY_APP"


class SuppContextEnum(str, Enum):
    """Enum for supp_context values."""
    SYSTEM = "SYSTEM"
    SUNSET = "SUNSET"
    PROMO = "PROMO"
    FINANCE_EXCEPTION = "FINANCE_EXCEPTION"
    OFFER = "OFFER"
    OFF_BOARDED = "OFF_BOARDED"
    TRIAL = "TRIAL"
    PILOT = "PILOT"
    OVERRIDE = "OVERRIDE"
    NO_PLAN = "NO_PLAN"
    NO_CLOVER_APPS = "NO_CLOVER_APPS"
    FIELD_TEST = "FIELD_TEST"
    DEBIT_NO_AUTH = "DEBIT_NO_AUTH"
    DEMO = "DEMO"
    ACH_HOLD = "ACH_HOLD"
    SEASONAL = "SEASONAL"
    ALL = "ALL"


class SuppressionMetrics(SQLModel, table=False):
    """
    SQLModel for the `suppression_metrics` table.

    This model represents suppression_metrics records in the billing system.
    Special case: table with composite primary key (no standard id field).
    """

    supp_month: datetime.date = Field(primary_key=True, description="Suppression month")
    supp_type: SuppTypeEnum = Field(primary_key=True, description="Suppression type")
    supp_context: SuppContextEnum = Field(primary_key=True, description="Suppression context")
    plan_charges: int = Field(description="Plan charges")
    app_charges: int = Field(description="App charges")
    wm_charges: int = Field(description="Web management charges")
    total_charges: int = Field(description="Total charges")
    num_suppressions: int = Field(description="Number of suppressions")
    num_merchants: int = Field(description="Number of merchants")

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this SuppressionMetrics instance."""
        return SuppressionMetrics(
            supp_month=self.supp_month,
            supp_type=self.supp_type,
            supp_context=self.supp_context,
            plan_charges=self.plan_charges,
            app_charges=self.app_charges,
            wm_charges=self.wm_charges,
            total_charges=self.total_charges,
            num_suppressions=self.num_suppressions,
            num_merchants=self.num_merchants,
        )
