"""
SQLModel definition for the stage_infolease_disbursement_attempt table, version 1.

This module provides the V1 implementation of the StageInfoleaseDisbursementAttempt model.
Currently, StageInfoleaseDisbursementAttemptV1 is identical to the base
StageInfoleaseDisbursementAttempt class (name-only inheritance), but as the table schema
evolves across environments, future versions (V2, V3, etc.) will contain actual schema
differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_infolease_disbursement_attempt import StageInfoleaseDisbursementAttempt


class StageInfoleaseDisbursementAttemptV1(StageInfoleaseDisbursementAttempt, NaProdSQLModel, table=True):
    """
    Version 1 of the StageInfoleaseDisbursementAttempt model.

    Currently a name-only inheritance from the base StageInfoleaseDisbursementAttempt class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_infolease_disbursement_attempt"  # type: ignore
