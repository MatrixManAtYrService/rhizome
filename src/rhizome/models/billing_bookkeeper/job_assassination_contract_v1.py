"""
SQLModel definition for the job_assassination_contract table, version 1.

This module provides the V1 implementation of the JobAssassinationContract model.
"""

from __future__ import annotations

from .job_assassination_contract import JobAssassinationContract


class JobAssassinationContractV1(JobAssassinationContract, table=True):
    """
    Version 1 of the JobAssassinationContract model.

    Currently a name-only inheritance from the base JobAssassinationContract class.
    """

    __tablename__ = "job_assassination_contract"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
