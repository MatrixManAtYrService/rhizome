"""
SQLModel definition for the look table, version 1.

This module provides the V1 implementation of the Look model.
"""

from __future__ import annotations

from .look import Look


class LookV1(Look, table=True):
    """
    Version 1 of the Look model.

    Currently a name-only inheritance from the base Look class.
    """

    __tablename__ = "look"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
