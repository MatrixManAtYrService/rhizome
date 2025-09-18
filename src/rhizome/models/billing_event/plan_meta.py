"""
SQLModel definition for the plan_meta table.

This module provides the SQLModel class for the plan_meta table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import Enum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PlanType(str, Enum):
    """Enum for plan types."""
    CLASSIC = "CLASSIC"
    PAYMENTS = "PAYMENTS"
    PAYMENTS_PLUS = "PAYMENTS_PLUS"
    REGISTER_LITE = "REGISTER_LITE"
    REGISTER = "REGISTER"
    QSR = "QSR"
    DINING = "DINING"
    NO_HARDWARE = "NO_HARDWARE"
    SERVICES = "SERVICES"
    RETAIL = "RETAIL"


class PlanMeta(RhizomeModel, table=False):
    """
    SQLModel for the `plan_meta` table.

    This model represents metadata for plans in the billing system,
    containing configuration and property information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=36, description="Unique identifier for the plan metadata")
    country: str | None = Field(default=None, max_length=2, description="Country code")
    plan_type: PlanType | None = Field(default=None, description="Type of the plan")
    plan_uuid: str | None = Field(default=None, max_length=13, description="UUID of the plan")
    name: str = Field(max_length=255, description="Name of the metadata property")
    value: str | None = Field(default=None, max_length=2048, description="Value of the metadata property")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")
    deleted_timestamp: datetime.datetime | None = Field(default=None, description="Timestamp when the record was deleted")

    def sanitize(self) -> PlanMeta:
        """Return a sanitized copy of this PlanMeta instance."""
        return PlanMeta(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            country=self.country,
            plan_type=self.plan_type,
            plan_uuid=sanitize_uuid_field(self.plan_uuid, 13),
            name=self.name,
            value=self.value,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            deleted_timestamp=self.deleted_timestamp,
        )