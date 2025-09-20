"""
SQLModel definition for the test_merchant_criteria table.

This module provides the SQLModel class for the test_merchant_criteria table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CriteriaType(str, Enum):
    """Enum for criteria types."""

    SOURCE = "SOURCE"
    EMAIL = "EMAIL"


class TestMerchantCriteria(RhizomeModel, table=False):
    """
    SQLModel for the `test_merchant_criteria` table.

    This model represents criteria used to identify test merchants in the billing system,
    containing type and value information for filtering.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=36, description="Unique identifier for the test merchant criteria")
    type: CriteriaType = Field(description="Type of criteria (SOURCE or EMAIL)")
    value: str = Field(max_length=255, description="Value for the criteria")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    deleted_timestamp: datetime.datetime | None = Field(
        default=None, description="Timestamp when the record was deleted"
    )

    def sanitize(self) -> TestMerchantCriteria:
        """Return a sanitized copy of this TestMerchantCriteria instance."""
        return TestMerchantCriteria(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            type=self.type,
            value=self.value,
            created_timestamp=self.created_timestamp,
            deleted_timestamp=self.deleted_timestamp,
        )
