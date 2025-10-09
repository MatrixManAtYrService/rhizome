"""
SQLModel definition for the app_sub_action_type table, version 1.

This module provides the V1 implementation of the AppSubActionType model.
"""

from __future__ import annotations

from .app_sub_action_type import AppSubActionType


class AppSubActionTypeV1(AppSubActionType, table=True):
    """
    Version 1 of the AppSubActionType model.

    Currently a name-only inheritance from the base AppSubActionType class.
    """

    __tablename__ = "app_sub_action_type"  # type: ignore
