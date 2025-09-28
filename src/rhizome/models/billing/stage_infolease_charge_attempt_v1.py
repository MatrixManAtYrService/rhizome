"""
SQLModel definition for the stage_infolease_charge_attempt table, version 1.

This module provides the V1 implementation of the StageInfoleaseChargeAttempt model.
Currently, StageInfoleaseChargeAttemptV1 is identical to the base StageInfoleaseChargeAttempt class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_infolease_charge_attempt import StageInfoleaseChargeAttempt


class StageInfoleaseChargeAttemptV1(StageInfoleaseChargeAttempt, NaProdSQLModel, table=True):
    """
    Version 1 of the StageInfoleaseChargeAttempt model.

    Currently a name-only inheritance from the base StageInfoleaseChargeAttempt class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_infolease_charge_attempt"  # type: ignore
