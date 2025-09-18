"""
SQLModel definition for the migrated_merchant table, version 1.

This module provides the V1 implementation of the MigratedMerchant model.
Currently, MigratedMerchantV1 is identical to the base MigratedMerchant class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .migrated_merchant import MigratedMerchant


class MigratedMerchantV1(MigratedMerchant, table=True):
    """
    Version 1 of the MigratedMerchant model.

    Currently a name-only inheritance from the base MigratedMerchant class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "migrated_merchant"  # type: ignore