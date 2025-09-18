"""
SQLModel definition for the cellular_billing_arrears_info table, version 1.

This module provides the V1 implementation of the CellularBillingArrearsInfo model.
Currently, CellularBillingArrearsInfoV1 is identical to the base CellularBillingArrearsInfo class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .cellular_billing_arrears_info import CellularBillingArrearsInfo


class CellularBillingArrearsInfoV1(CellularBillingArrearsInfo, table=True):
    """
    Version 1 of the CellularBillingArrearsInfo model.

    Currently a name-only inheritance from the base CellularBillingArrearsInfo class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "cellular_billing_arrears_info"  # type: ignore