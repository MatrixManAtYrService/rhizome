"""
SQLModel definition for the jobrunr_migrations table, version 1.

This module provides the V1 implementation of the JobrunrMigrations model.
Currently, JobrunrMigrationsV1 is identical to the base JobrunrMigrations class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .jobrunr_migrations import JobrunrMigrations


class JobrunrMigrationsV1(JobrunrMigrations, table=True):
    """
    Version 1 of the JobrunrMigrations model.

    Currently a name-only inheritance from the base JobrunrMigrations class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "jobrunr_migrations"  # type: ignore