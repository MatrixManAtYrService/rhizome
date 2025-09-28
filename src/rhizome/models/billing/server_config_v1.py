"""
SQLModel definition for the server_config table, version 1.

This module provides the V1 implementation of the ServerConfig model.
Currently, ServerConfigV1 is identical to the base ServerConfig class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .server_config import ServerConfig


class ServerConfigV1(ServerConfig, NaProdSQLModel, table=True):
    """
    Version 1 of the ServerConfig model.

    Currently a name-only inheritance from the base ServerConfig class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "server_config"  # type: ignore