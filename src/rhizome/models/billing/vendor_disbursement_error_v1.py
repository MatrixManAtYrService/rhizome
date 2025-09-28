"""
SQLModel definition for the vendor_disbursement_error table, version 1.

This module provides the V1 implementation of the VendorDisbursementError model.
Currently, VendorDisbursementErrorV1 is identical to the base VendorDisbursementError class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .vendor_disbursement_error import VendorDisbursementError


class VendorDisbursementErrorV1(VendorDisbursementError, NaProdSQLModel, table=True):
    """
    Version 1 of the VendorDisbursementError model.

    Currently a name-only inheritance from the base VendorDisbursementError class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "vendor_disbursement_error"  # type: ignore
