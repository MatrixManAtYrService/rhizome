"""
SQLModel definition for the app_sub_action_error table, version 1.

This module provides the V1 implementation of the AppSubActionError model.
"""

from __future__ import annotations

from .app_sub_action_error import AppSubActionError


class AppSubActionErrorV1(AppSubActionError, table=True):
    """
    Version 1 of the AppSubActionError model.

    Currently a name-only inheritance from the base AppSubActionError class.
    """

    __tablename__ = "app_sub_action_error"  # type: ignore
