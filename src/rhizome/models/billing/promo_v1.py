"""
SQLModel definition for the promo table, version 1.

This module provides the V1 implementation of the Promo model.
Currently, PromoV1 is identical to the base Promo class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .promo import Promo


class PromoV1(Promo, NaProdSQLModel, table=True):
    """
    Version 1 of the Promo model.

    Currently a name-only inheritance from the base Promo class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "promo"  # type: ignore
