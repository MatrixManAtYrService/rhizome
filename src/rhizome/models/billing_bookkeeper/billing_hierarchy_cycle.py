"""
SQLModel definition for the billing_hierarchy_cycle table.

This module provides the SQLModel class for the billing_hierarchy_cycle table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingHierarchyCycle(RhizomeModel, table=False):
    """
    SQLModel for the `billing_hierarchy_cycle` table.

    This model represents billing hierarchy cycle records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    processing_group_uuid: str = Field(max_length=26, description="Processing Group Uuid")
    billing_hierarchy_uuid: str = Field(max_length=26, description="Billing Hierarchy Uuid")
    cycle_date: datetime.date = Field(description="Cycle Date")
    close_date: datetime.date | None = Field(default=None, description="Close Date")
    effective_close_date: datetime.date | None = Field(default=None, description="Effective Close Date")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    entity_uuid: str = Field(max_length=13, description="Entity Uuid")
    schedule_parent_be_uuid: str = Field(max_length=26, description="Schedule Parent Be Uuid")
    fee_rate_parent_be_uuid: str = Field(max_length=26, description="Fee Rate Parent Be Uuid")
    frequency: str = Field(description="Frequency")
    billing_day: int = Field(description="Billing Day")
    next_billing_date: datetime.date = Field(description="Next Billing Date")
    last_billing_date: datetime.date | None = Field(default=None, description="Last Billing Date")
    arrears_billing_date: datetime.date | None = Field(default=None, description="Arrears Billing Date")
    units_in_next_period: int = Field(description="Units In Next Period")
    units_in_last_period: int = Field(default=None, description="Units In Last Period")
    units_in_arrears_period: int = Field(default=None, description="Units In Arrears Period")
    default_currency: str = Field(max_length=3, description="Default Currency")
    post_method: str = Field(max_length=20, description="Post Method")
    plan_billing_method: str = Field(max_length=20, description="Plan Billing Method")
    invoice_method: str = Field(max_length=20, description="Invoice Method")
    invoice_number_format: str = Field(max_length=20, description="Invoice Number Format")
    settlement_method: str = Field(max_length=20, description="Settlement Method")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> BillingHierarchyCycle:
        """Return a sanitized copy of this BillingHierarchyCycle instance."""
        return BillingHierarchyCycle(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            processing_group_uuid=sanitize_uuid_field(self.processing_group_uuid, 26),  # type: ignore
            billing_hierarchy_uuid=sanitize_uuid_field(self.billing_hierarchy_uuid, 26),  # type: ignore
            cycle_date=self.cycle_date,
            close_date=self.close_date,
            effective_close_date=self.effective_close_date,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            entity_uuid=sanitize_uuid_field(self.entity_uuid, 13),  # type: ignore
            schedule_parent_be_uuid=sanitize_uuid_field(self.schedule_parent_be_uuid, 26),  # type: ignore
            fee_rate_parent_be_uuid=sanitize_uuid_field(self.fee_rate_parent_be_uuid, 26),  # type: ignore
            frequency=self.frequency,
            billing_day=self.billing_day,
            next_billing_date=self.next_billing_date,
            last_billing_date=self.last_billing_date,
            arrears_billing_date=self.arrears_billing_date,
            units_in_next_period=self.units_in_next_period,
            units_in_last_period=self.units_in_last_period,
            units_in_arrears_period=self.units_in_arrears_period,
            default_currency=self.default_currency,
            post_method=self.post_method,
            plan_billing_method=self.plan_billing_method,
            invoice_method=self.invoice_method,
            invoice_number_format=self.invoice_number_format,
            settlement_method=self.settlement_method,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
