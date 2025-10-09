"""
SQLModel definition for the cycle_validation table.

This module provides the SQLModel class for the cycle_validation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CycleValidation(RhizomeModel, table=False):
    """
    SQLModel for the `cycle_validation` table.

    This model represents cycle validation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    task_id: str = Field(max_length=126, description="Task Id")
    task_type: str = Field(description="Task Type")
    validation_group: str = Field(max_length=126, description="Validation Group")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    hierarchy_type: str = Field(max_length=20, description="Hierarchy Type")
    cycle_date: datetime.date = Field(description="Cycle Date")
    currency: str = Field(max_length=3, description="Currency")
    status: str = Field(max_length=25, description="Status")
    bypass_count: Decimal = Field(max_digits=12, decimal_places=4, description="Bypass Count")
    bypass_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Bypass Amount")
    accepted_count: Decimal = Field(max_digits=12, decimal_places=4, description="Accepted Count")
    accepted_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Accepted Amount")
    total_count: Decimal = Field(max_digits=12, decimal_places=4, description="Total Count")
    total_amount: Decimal = Field(max_digits=12, decimal_places=3, description="Total Amount")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    validation_request_uuid: str | None = Field(default=None, max_length=26, description="Validation Request Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> CycleValidation:
        """Return a sanitized copy of this CycleValidation instance."""
        return CycleValidation(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            task_id=self.task_id,
            task_type=self.task_type,
            validation_group=self.validation_group,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            hierarchy_type=self.hierarchy_type,
            cycle_date=self.cycle_date,
            currency=self.currency,
            status=self.status,
            bypass_count=self.bypass_count,
            bypass_amount=self.bypass_amount,
            accepted_count=self.accepted_count,
            accepted_amount=self.accepted_amount,
            total_count=self.total_count,
            total_amount=self.total_amount,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            validation_request_uuid=sanitize_uuid_field(self.validation_request_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
