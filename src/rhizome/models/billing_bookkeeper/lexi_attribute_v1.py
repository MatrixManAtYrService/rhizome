"""
SQLModel definition for the lexi_attribute table, version 1.

This module provides the V1 implementation of the LexiAttribute model.
"""

from __future__ import annotations

from .lexi_attribute import LexiAttribute


class LexiAttributeV1(LexiAttribute, table=True):
    """
    Version 1 of the LexiAttribute model.

    Currently a name-only inheritance from the base LexiAttribute class.
    """

    __tablename__ = "lexi_attribute"  # type: ignore
