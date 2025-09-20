"""
SQLModel definition for the iccid_carrier table.

This module provides the SQLModel class for the iccid_carrier table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class IccidCarrier(RhizomeModel, table=False):
    """
    SQLModel for the `iccid_carrier` table.

    This model represents ICCID carrier mappings in the billing system,
    containing information about SIM card identifiers and their carriers.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, description="Unique identifier for the ICCID carrier record")
    iccid: str = Field(max_length=24, unique=True, description="Integrated Circuit Card Identifier")
    iin: str = Field(max_length=7, description="Issuer Identification Number")
    carrier: str = Field(max_length=25, description="Carrier name")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> IccidCarrier:
        """Return a sanitized copy of this IccidCarrier instance."""
        return IccidCarrier(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            iccid=self.iccid,
            iin=self.iin,
            carrier=self.carrier,
            created_timestamp=self.created_timestamp,
        )
