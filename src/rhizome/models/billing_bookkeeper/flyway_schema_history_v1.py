"""
SQLModel definition for the flyway_schema_history table, version 1.

This module provides the V1 implementation of the FlywaySchemaHistory model.
"""

from __future__ import annotations

from .flyway_schema_history import FlywaySchemaHistory


class FlywaySchemaHistoryV1(FlywaySchemaHistory, table=True):
    """
    Version 1 of the FlywaySchemaHistory model.

    Currently a name-only inheritance from the base FlywaySchemaHistory class.
    """

    __tablename__ = "flyway_schema_history"  # type: ignore
