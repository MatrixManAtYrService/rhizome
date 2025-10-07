"""
SQLModel definition for the bank_routing table, version 1.

This module provides the V1 implementation of the BankRouting model.
Currently, BankRoutingV1 is identical to the base BankRouting class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .bank_routing import BankRouting


class BankRoutingV1(BankRouting, NaProdSQLModel, table=True):
    """
    Version 1 of the BankRouting model.

    Currently a name-only inheritance from the base BankRouting class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "bank_routing"  # type: ignore
