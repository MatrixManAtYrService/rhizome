"""
SQLModel definition for the billing_entity table.

This module provides the SQLModel class for the billing_entity table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class EntityType(StrEnum):
    """Enum for billing entity types."""

    MERCHANT = "MERCHANT"
    RESELLER = "RESELLER"
    DEVELOPER = "DEVELOPER"
    PSEUDO = "PSEUDO"
    ARCHETYPE = "ARCHETYPE"


class BillingEntity(RhizomeModel, table=False):
    """
    SQLModel for the `billing_entity` table.

    This model represents billing entities in the system,
    tracking different types of entities (merchants, resellers, developers, etc.).
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the billing entity record")
    entity_uuid: str = Field(max_length=13, description="UUID of the entity")
    entity_type: EntityType = Field(description="Type of entity (MERCHANT, RESELLER, DEVELOPER, PSEUDO, ARCHETYPE)")
    name: str | None = Field(default=None, max_length=127, description="Name of the entity")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> BillingEntity:
        """Return a sanitized copy of this BillingEntity instance."""
        return BillingEntity(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            entity_uuid=sanitize_uuid_field(self.entity_uuid, 13),  # type: ignore
            entity_type=self.entity_type,
            name=self.name,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )