"""
SQLModel definition for the fee_exception table.

This module provides the SQLModel class for the fee_exception table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ReferenceTypeType(str, Enum):
    """Enum for reference_type values."""

    MERCHANT = "MERCHANT"


class FeeException(RhizomeModel, table=False):
    """
    SQLModel for the `fee_exception` table.

    This model represents fee_exception records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    reference_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reference_type: ReferenceTypeType = Field(description="reference_type")
    fee_type: str | None = Field(default=None, description="fee_type")
    context: str | None = Field(default=None, description="context")
    detail: str = Field(max_length=511, description="detail")
    start_time: datetime.datetime = Field(description="start_time")
    finalization_time: datetime.datetime | None = Field(default=None, description="finalization_time")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> FeeException:
        """Return a sanitized copy of this FeeException instance."""
        return FeeException(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            reference_id=self.reference_id,
            reference_type=self.reference_type,
            fee_type=self.fee_type,
            context=self.context,
            detail=self.detail,
            start_time=self.start_time,
            finalization_time=self.finalization_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
