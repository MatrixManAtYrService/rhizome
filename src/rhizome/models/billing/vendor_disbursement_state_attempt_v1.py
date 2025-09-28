"""
SQLModel definition for the vendor_disbursement_state_attempt table, version 1.

This module provides the V1 implementation of the VendorDisbursementStateAttempt model.
Currently, VendorDisbursementStateAttemptV1 is identical to the base VendorDisbursementStateAttempt class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .vendor_disbursement_state_attempt import VendorDisbursementStateAttempt


class VendorDisbursementStateAttemptV1(VendorDisbursementStateAttempt, NaProdSQLModel, table=True):
    """
    Version 1 of the VendorDisbursementStateAttempt model.

    Currently a name-only inheritance from the base VendorDisbursementStateAttempt class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "vendor_disbursement_state_attempt"  # type: ignore
