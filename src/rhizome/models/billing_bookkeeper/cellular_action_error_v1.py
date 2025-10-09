"""
SQLModel definition for the cellular_action_error table, version 1.

This module provides the V1 implementation of the CellularActionError model.
"""

from __future__ import annotations

from .cellular_action_error import CellularActionError


class CellularActionErrorV1(CellularActionError, table=True):
    """
    Version 1 of the CellularActionError model.

    Currently a name-only inheritance from the base CellularActionError class.
    """

    __tablename__ = "cellular_action_error"  # type: ignore
