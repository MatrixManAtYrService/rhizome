"""
SQLModel definition for the stage_vendor_disbursement_state_attempt table, version 1.

This module provides the V1 implementation of the StageVendorDisbursementStateAttempt
model. Currently, StageVendorDisbursementStateAttemptV1 is identical to the base
StageVendorDisbursementStateAttempt class (name-only inheritance), but as the table
schema evolves across environments, future versions (V2, V3, etc.) will contain
actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_vendor_disbursement_state_attempt import StageVendorDisbursementStateAttempt


class StageVendorDisbursementStateAttemptV1(StageVendorDisbursementStateAttempt, NaProdSQLModel, table=True):
    """
    Version 1 of the StageVendorDisbursementStateAttempt model.

    Currently a name-only inheritance from the base StageVendorDisbursementStateAttempt class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_vendor_disbursement_state_attempt"  # type: ignore
