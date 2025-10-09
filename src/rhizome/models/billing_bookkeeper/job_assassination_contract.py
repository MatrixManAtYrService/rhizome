"""
SQLModel definition for the job_assassination_contract table.

This module provides the SQLModel class for the job_assassination_contract table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobAssassinationContract(RhizomeModel, table=False):
    """
    SQLModel for the `job_assassination_contract` table.

    This model represents job assassination contract records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    job_identifier: str = Field(max_length=50, description="Job Identifier")
    killed: int = Field(description="Killed")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> JobAssassinationContract:
        """Return a sanitized copy of this JobAssassinationContract instance."""
        return JobAssassinationContract(
            id=self.id,
            job_identifier=self.job_identifier,
            killed=self.killed,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
