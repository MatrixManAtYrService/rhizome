"""
SQLModel definition for the charge_metrics table.

This module provides the SQLModel class for the charge_metrics table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel


class CategoryType(str, Enum):
    """Enum for category values."""

    ALL = "ALL"
    PLAN = "PLAN"
    WM = "WM"
    APP = "APP"


class ChargeMetrics(RhizomeModel, table=False):
    """
    SQLModel for the `charge_metrics` table.

    This model represents charge_metrics records in the billing system.
    """

    stmt_month: datetime.date = Field(primary_key=True, description="Statement month")
    category: CategoryType = Field(primary_key=True, description="Category type")
    net_pending: int = Field(description="net_pending")
    net_incurred: int = Field(description="net_incurred")
    net_in_progress: int = Field(description="net_in_progress")
    net_ach_reject: int = Field(description="net_ach_reject")
    net_billed: int = Field(description="net_billed")
    net_written_off: int = Field(description="net_written_off")
    net_waived: int = Field(description="net_waived")
    net_canceled: int = Field(description="net_canceled")
    num_charges: int = Field(description="num_charges")
    num_merchants: int = Field(description="num_merchants")
    num_in_progress_merchants: int = Field(description="num_in_progress_merchants")
    num_ach_reject_merchants: int = Field(description="num_ach_reject_merchants")
    num_incurred_merchants: int = Field(description="num_incurred_merchants")
    orig_num_incurred_merchants: int = Field(description="orig_num_incurred_merchants")

    def sanitize(self) -> ChargeMetrics:
        """Return a sanitized copy of this ChargeMetrics instance."""
        return ChargeMetrics(
            stmt_month=self.stmt_month,
            category=self.category,
            net_pending=self.net_pending,
            net_incurred=self.net_incurred,
            net_in_progress=self.net_in_progress,
            net_ach_reject=self.net_ach_reject,
            net_billed=self.net_billed,
            net_written_off=self.net_written_off,
            net_waived=self.net_waived,
            net_canceled=self.net_canceled,
            num_charges=self.num_charges,
            num_merchants=self.num_merchants,
            num_in_progress_merchants=self.num_in_progress_merchants,
            num_ach_reject_merchants=self.num_ach_reject_merchants,
            num_incurred_merchants=self.num_incurred_merchants,
            orig_num_incurred_merchants=self.orig_num_incurred_merchants,
        )
