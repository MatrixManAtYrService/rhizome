"""
SQLModel definition for the banner_details table, version 1.

This module provides the V1 implementation of the BannerDetails model.
Currently, BannerDetailsV1 is identical to the base BannerDetails class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .banner_details import BannerDetails


class BannerDetailsV1(BannerDetails, NaProdSQLModel, table=True):
    """
    Version 1 of the BannerDetails model.

    Currently a name-only inheritance from the base BannerDetails class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "banner_details"  # type: ignore
