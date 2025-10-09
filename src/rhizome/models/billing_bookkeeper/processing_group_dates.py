"""
SQLModel definition for the processing_group_dates table.

This module provides the SQLModel class for the processing_group_dates table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ProcessingGroupDates(RhizomeModel, table=False):
    """
    SQLModel for the `processing_group_dates` table.

    This model represents processing group dates records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    hierarchy_type: str = Field(max_length=20, description="Hierarchy Type")
    cycle_date: datetime.date = Field(description="Cycle Date")
    last_cycle_date: datetime.date | None = Field(default=None, description="Last Cycle Date")
    posting_date: datetime.date = Field(description="Posting Date")
    last_posting_date: datetime.date | None = Field(default=None, description="Last Posting Date")
    billing_date: datetime.date = Field(description="Billing Date")
    last_billing_date: datetime.date | None = Field(default=None, description="Last Billing Date")
    settlement_date: datetime.date = Field(description="Settlement Date")
    last_settlement_date: datetime.date | None = Field(default=None, description="Last Settlement Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> ProcessingGroupDates:
        """Return a sanitized copy of this ProcessingGroupDates instance."""
        return ProcessingGroupDates(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            hierarchy_type=self.hierarchy_type,
            cycle_date=self.cycle_date,
            last_cycle_date=self.last_cycle_date,
            posting_date=self.posting_date,
            last_posting_date=self.last_posting_date,
            billing_date=self.billing_date,
            last_billing_date=self.last_billing_date,
            settlement_date=self.settlement_date,
            last_settlement_date=self.last_settlement_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
