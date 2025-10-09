"""
SQLModel definition for the misc_action table, version 1.

This module provides the V1 implementation of the MiscAction model.
"""

from __future__ import annotations

from .misc_action import MiscAction


class MiscActionV1(MiscAction, table=True):
    """
    Version 1 of the MiscAction model.

    Currently a name-only inheritance from the base MiscAction class.
    """

    __tablename__ = "misc_action"  # type: ignore
