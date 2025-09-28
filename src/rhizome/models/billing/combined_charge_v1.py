"""
SQLModel definition for the combined_charge table, version 1.

This module provides the V1 implementation of the CombinedCharge model.
Currently, CombinedChargeV1 is identical to the base CombinedCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .combined_charge import CombinedCharge


class CombinedChargeV1(CombinedCharge, NaProdSQLModel, table=True):
    """
    Version 1 of the CombinedCharge model.

    Currently a name-only inheritance from the base CombinedCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "combined_charge"  # type: ignore
