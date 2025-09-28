"""
SQLModel definition for the promo_control table, version 1.

This module provides the V1 implementation of the PromoControl model.
Currently, PromoControlV1 is identical to the base PromoControl class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .promo_control import PromoControl


class PromoControlV1(PromoControl, NaProdSQLModel, table=True):
    """
    Version 1 of the PromoControl model.

    Currently a name-only inheritance from the base PromoControl class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "promo_control"  # type: ignore
