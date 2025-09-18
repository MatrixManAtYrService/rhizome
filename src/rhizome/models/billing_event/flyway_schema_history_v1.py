"""
SQLModel definition for the flyway_schema_history table, version 1.

This module provides the V1 implementation of the FlywaySchemaHistory model.
Currently, FlywaySchemaHistoryV1 is identical to the base FlywaySchemaHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .flyway_schema_history import FlywaySchemaHistory


class FlywaySchemaHistoryV1(FlywaySchemaHistory, table=True):
    """
    Version 1 of the FlywaySchemaHistory model.

    Currently a name-only inheritance from the base FlywaySchemaHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "flyway_schema_history"  # type: ignore