"""
SQLModel definition for the server_config table, version 1.

This module provides the V1 implementation of the ServerConfig model.
"""

from __future__ import annotations

from .server_config import ServerConfig


class ServerConfigV1(ServerConfig, table=True):
    """
    Version 1 of the ServerConfig model.

    Currently a name-only inheritance from the base ServerConfig class.
    """

    __tablename__ = "server_config"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
