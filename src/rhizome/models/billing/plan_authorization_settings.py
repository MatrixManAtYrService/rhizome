"""
SQLModel definition for the plan_authorization_settings table.

This module provides the SQLModel class for the plan_authorization_settings table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations


from sqlmodel import Field

from ...models.base import RhizomeModel


class PlanAuthorizationSettings(RhizomeModel, table=False):
    """
    SQLModel for the `plan_authorization_settings` table.

    This model represents plan_authorization_settings records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    partner_control_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reseller_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    country_code: str = Field(max_length=2, description="country_code")
    plan_group_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    device_name: str | None = Field(default=None, max_length=255, description="device_name")
    rules: str = Field(max_length=16383, description="rules")

    def sanitize(self) -> PlanAuthorizationSettings:
        """Return a sanitized copy of this PlanAuthorizationSettings instance."""
        return PlanAuthorizationSettings(
            id=self.id,
            merchant_id=self.merchant_id,
            partner_control_id=self.partner_control_id,
            reseller_id=self.reseller_id,
            country_code=self.country_code,
            plan_group_id=self.plan_group_id,
            device_name=self.device_name,
            rules=self.rules,
        )
