"""
SQLModel definition for the banner_data table, version 1.

This module provides the V1 implementation of the BannerData model.
Currently, BannerDataV1 is identical to the base BannerData class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .banner_data import BannerData


class BannerDataV1(BannerData, NaProdSQLModel, table=True):
    """
    Version 1 of the BannerData model.

    Currently a name-only inheritance from the base BannerData class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "banner_data"  # type: ignore
