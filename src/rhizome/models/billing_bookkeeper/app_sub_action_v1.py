"""
SQLModel definition for the app_sub_action table, version 1.

This module provides the V1 implementation of the AppSubAction model.
"""

from __future__ import annotations

from .app_sub_action import AppSubAction


class AppSubActionV1(AppSubAction, table=True):
    """
    Version 1 of the AppSubAction model.

    Currently a name-only inheritance from the base AppSubAction class.
    """

    __tablename__ = "app_sub_action"  # type: ignore
