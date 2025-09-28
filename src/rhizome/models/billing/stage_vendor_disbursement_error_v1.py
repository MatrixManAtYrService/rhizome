"""
SQLModel definition for the stage_vendor_disbursement_error table, version 1.

This module provides the V1 implementation of the StageVendorDisbursementError model.
Currently, StageVendorDisbursementErrorV1 is identical to the base StageVendorDisbursementError class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_vendor_disbursement_error import StageVendorDisbursementError


class StageVendorDisbursementErrorV1(StageVendorDisbursementError, NaProdSQLModel, table=True):
    """
    Version 1 of the StageVendorDisbursementError model.

    Currently a name-only inheritance from the base StageVendorDisbursementError class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_vendor_disbursement_error"  # type: ignore
