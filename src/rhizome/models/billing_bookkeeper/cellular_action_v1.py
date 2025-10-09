"""
SQLModel definition for the cellular_action table, version 1.

This module provides the V1 implementation of the CellularAction model.
"""

from __future__ import annotations

from .cellular_action import CellularAction


class CellularActionV1(CellularAction, table=True):
    """
    Version 1 of the CellularAction model.

    Currently a name-only inheritance from the base CellularAction class.
    """

    __tablename__ = "cellular_action"  # type: ignore
