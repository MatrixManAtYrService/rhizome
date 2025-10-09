"""
SQLModel definition for the skip_fee_category_lexi_tag table, version 1.

This module provides the V1 implementation of the SkipFeeCategoryLexiTag model.
"""

from __future__ import annotations

from .skip_fee_category_lexi_tag import SkipFeeCategoryLexiTag


class SkipFeeCategoryLexiTagV1(SkipFeeCategoryLexiTag, table=True):
    """
    Version 1 of the SkipFeeCategoryLexiTag model.

    Currently a name-only inheritance from the base SkipFeeCategoryLexiTag class.
    """

    __tablename__ = "skip_fee_category_lexi_tag"  # type: ignore
