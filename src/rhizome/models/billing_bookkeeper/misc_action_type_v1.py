"""
SQLModel definition for the misc_action_type table, version 1.

This module provides the V1 implementation of the MiscActionType model.
"""

from __future__ import annotations

from .misc_action_type import MiscActionType


class MiscActionTypeV1(MiscActionType, table=True):
    """
    Version 1 of the MiscActionType model.

    Currently a name-only inheritance from the base MiscActionType class.
    """

    __tablename__ = "misc_action_type"  # type: ignore
