"""
SQLModel definition for the reseller_usage_job_config table.

This module provides the SQLModel class for the reseller_usage_job_config table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel


class ResellerUsageJobConfig(RhizomeModel, table=False):
    """
    SQLModel for the `reseller_usage_job_config` table.

    This model represents reseller_usage_job_config records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reseller_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    report_type: str | None = Field(default=None, description="report_type")

    def sanitize(self) -> ResellerUsageJobConfig:
        """Return a sanitized copy of this ResellerUsageJobConfig instance."""
        return ResellerUsageJobConfig(
            id=self.id,
            reseller_id=self.reseller_id,
            report_type=self.report_type,
        )
