"""
SQLModel definition for the cellular_action_type table, version 1.

This module provides the V1 implementation of the CellularActionType model.
"""

from __future__ import annotations

from .cellular_action_type import CellularActionType


class CellularActionTypeV1(CellularActionType, table=True):
    """
    Version 1 of the CellularActionType model.

    Currently a name-only inheritance from the base CellularActionType class.
    """

    __tablename__ = "cellular_action_type"  # type: ignore
