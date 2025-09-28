"""
SQLModel definition for the suppression_metrics table.

This module provides the SQLModel class for the suppression_metrics table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class SuppressionMetrics(RhizomeModel, table=False):
    """
    SQLModel for the `suppression_metrics` table.

    This model represents suppression_metrics records in the billing system.
    """

    supp_month: datetime.date = Field(description="supp_month")
    supp_type: str | None = Field(default=None, description="supp_type")
    supp_context: str | None = Field(default=None, description="supp_context")
    plan_charges: int = Field(description="plan_charges")
    app_charges: int = Field(description="app_charges")
    wm_charges: int = Field(description="wm_charges")
    total_charges: int = Field(description="total_charges")
    num_suppressions: int = Field(description="num_suppressions")
    num_merchants: int = Field(description="num_merchants")

    def sanitize(self) -> SuppressionMetrics:
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
