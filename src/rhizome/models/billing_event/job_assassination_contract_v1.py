"""
SQLModel definition for the job_assassination_contract table, version 1.

This module provides the V1 implementation of the JobAssassinationContract model.
Currently, JobAssassinationContractV1 is identical to the base JobAssassinationContract class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .job_assassination_contract import JobAssassinationContract


class JobAssassinationContractV1(JobAssassinationContract, table=True):
    """
    Version 1 of the JobAssassinationContract model.

    Currently a name-only inheritance from the base JobAssassinationContract class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "job_assassination_contract"  # type: ignore