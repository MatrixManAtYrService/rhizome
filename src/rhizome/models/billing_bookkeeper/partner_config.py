"""
SQLModel definition for the partner_config table.

This module provides the SQLModel class for the partner_config table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PartnerConfig(RhizomeModel, table=False):
    """
    SQLModel for the `partner_config` table.

    This model represents partner config records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    hierarchy_type: str = Field(max_length=20, description="Hierarchy Type")
    effective_date: datetime.date = Field(description="Effective Date")
    revenue_share_group: str | None = Field(default=None, max_length=20, description="Revenue Share Group")
    post_method: str | None = Field(default=None, max_length=20, description="Post Method")
    plan_billing_method: str | None = Field(default=None, max_length=20, description="Plan Billing Method")
    invoice_method: str | None = Field(default=None, max_length=20, description="Invoice Method")
    invoice_number_format: str | None = Field(default=None, max_length=20, description="Invoice Number Format")
    settlement_method: str | None = Field(default=None, max_length=20, description="Settlement Method")
    seasonal_rule_set_uuid: str | None = Field(default=None, max_length=26, description="Seasonal Rule Set Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> PartnerConfig:
        """Return a sanitized copy of this PartnerConfig instance."""
        return PartnerConfig(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            hierarchy_type=self.hierarchy_type,
            effective_date=self.effective_date,
            revenue_share_group=self.revenue_share_group,
            post_method=self.post_method,
            plan_billing_method=self.plan_billing_method,
            invoice_method=self.invoice_method,
            invoice_number_format=self.invoice_number_format,
            settlement_method=self.settlement_method,
            seasonal_rule_set_uuid=sanitize_uuid_field(self.seasonal_rule_set_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
