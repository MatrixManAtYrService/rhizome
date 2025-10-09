"""
SQLModel definition for the misc_action_error table, version 1.

This module provides the V1 implementation of the MiscActionError model.
"""

from __future__ import annotations

from .misc_action_error import MiscActionError


class MiscActionErrorV1(MiscActionError, table=True):
    """
    Version 1 of the MiscActionError model.

    Currently a name-only inheritance from the base MiscActionError class.
    """

    __tablename__ = "misc_action_error"  # type: ignore
