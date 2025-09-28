"""
SQLModel definition for the vat_vendor_disbursement table, version 1.

This module provides the V1 implementation of the VatVendorDisbursement model.
Currently, VatVendorDisbursementV1 is identical to the base VatVendorDisbursement class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .vat_vendor_disbursement import VatVendorDisbursement


class VatVendorDisbursementV1(VatVendorDisbursement, NaProdSQLModel, table=True):
    """
    Version 1 of the VatVendorDisbursement model.

    Currently a name-only inheritance from the base VatVendorDisbursement class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "vat_vendor_disbursement"  # type: ignore
