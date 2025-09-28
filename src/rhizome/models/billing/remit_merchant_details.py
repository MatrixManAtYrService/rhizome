"""
SQLModel definition for the remit_merchant_details table.

This module provides the SQLModel class for the remit_merchant_details table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class RemitMerchantDetails(RhizomeModel, table=False):
    """
    SQLModel for the `remit_merchant_details` table.

    This model represents remit_merchant_details records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    remit_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    hierarchy_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    remit_type: str | None = Field(default=None, max_length=30, description="remit_type")
    hierarchy_name: str | None = Field(default=None, description="hierarchy_name")
    status_owner: str | None = Field(default=None, max_length=30, description="status_owner")
    entity_name: str | None = Field(default=None, max_length=50, description="entity_name")
    relm_code: str | None = Field(default=None, max_length=30, description="relm_code")
    deleted_time: datetime.date | None = Field(default=None, description="deleted_time")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> RemitMerchantDetails:
        """Return a sanitized copy of this RemitMerchantDetails instance."""
        return RemitMerchantDetails(
            id=self.id,
            remit_uuid=sanitize_uuid_field(self.remit_uuid, 30),
            hierarchy_id=self.hierarchy_id,
            remit_type=self.remit_type,
            hierarchy_name=self.hierarchy_name,
            status_owner=self.status_owner,
            entity_name=self.entity_name,
            relm_code=self.relm_code,
            deleted_time=self.deleted_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
