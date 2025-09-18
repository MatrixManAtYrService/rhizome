"""
SQLModel definition for the cellular_arrears_acceptances table, version 1.

This module provides the V1 implementation of the CellularArrearsAcceptances model.
Currently, CellularArrearsAcceptancesV1 is identical to the base CellularArrearsAcceptances class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .cellular_arrears_acceptances import CellularArrearsAcceptances


class CellularArrearsAcceptancesV1(CellularArrearsAcceptances, table=True):
    """
    Version 1 of the CellularArrearsAcceptances model.

    Currently a name-only inheritance from the base CellularArrearsAcceptances class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "cellular_arrears_acceptances"  # type: ignore