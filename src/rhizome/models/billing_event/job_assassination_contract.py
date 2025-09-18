"""
SQLModel definition for the job_assassination_contract table.

This module provides the SQLModel class for the job_assassination_contract table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobAssassinationContract(RhizomeModel, table=False):
    """
    SQLModel for the `job_assassination_contract` table.

    This model represents job assassination contracts in the billing system,
    containing information about jobs that need to be terminated.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    job_identifier: str = Field(max_length=50, description="Identifier of the job to be assassinated")
    killed: int = Field(default=0, description="Status flag indicating if job was killed (0=no, 1=yes)")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> JobAssassinationContract:
        """Return a sanitized copy of this JobAssassinationContract instance."""
        return JobAssassinationContract(
            id=self.id,
            job_identifier=self.job_identifier,
            killed=self.killed,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )