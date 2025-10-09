"""
SQLModel definition for the misc_specifier table, version 1.

This module provides the V1 implementation of the MiscSpecifier model.
"""

from __future__ import annotations

from .misc_specifier import MiscSpecifier


class MiscSpecifierV1(MiscSpecifier, table=True):
    """
    Version 1 of the MiscSpecifier model.

    Currently a name-only inheritance from the base MiscSpecifier class.
    """

    __tablename__ = "misc_specifier"  # type: ignore
