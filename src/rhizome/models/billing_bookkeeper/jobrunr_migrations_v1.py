"""
SQLModel definition for the jobrunr_migrations table, version 1.

This module provides the V1 implementation of the JobrunrMigrations model.
"""

from __future__ import annotations

from .jobrunr_migrations import JobrunrMigrations


class JobrunrMigrationsV1(JobrunrMigrations, table=True):
    """
    Version 1 of the JobrunrMigrations model.

    Currently a name-only inheritance from the base JobrunrMigrations class.
    """

    __tablename__ = "jobrunr_migrations"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
