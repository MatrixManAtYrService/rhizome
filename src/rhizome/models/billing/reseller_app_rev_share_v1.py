"""
SQLModel definition for the reseller_app_rev_share table, version 1.

This module provides the V1 implementation of the ResellerAppRevShare model.
Currently, ResellerAppRevShareV1 is identical to the base ResellerAppRevShare class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .reseller_app_rev_share import ResellerAppRevShare


class ResellerAppRevShareV1(ResellerAppRevShare, NaProdSQLModel, table=True):
    """
    Version 1 of the ResellerAppRevShare model.

    Currently a name-only inheritance from the base ResellerAppRevShare class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_app_rev_share"  # type: ignore
