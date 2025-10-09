"""
SQLModel definition for the look_data table, version 1.

This module provides the V1 implementation of the LookData model.
"""

from __future__ import annotations

from .look_data import LookData


class LookDataV1(LookData, table=True):
    """
    Version 1 of the LookData model.

    Currently a name-only inheritance from the base LookData class.
    """

    __tablename__ = "look_data"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
