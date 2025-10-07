"""
SQLModel definition for the banner_curb table, version 1.

This module provides the V1 implementation of the BannerCurb model.
Currently, BannerCurbV1 is identical to the base BannerCurb class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .banner_curb import BannerCurb


class BannerCurbV1(BannerCurb, NaProdSQLModel, table=True):
    """
    Version 1 of the BannerCurb model.

    Currently a name-only inheritance from the base BannerCurb class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "banner_curb"  # type: ignore
