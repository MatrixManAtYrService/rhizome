"""
SQLModel definition for the charge_state_attempt table, version 1.

This module provides the V1 implementation of the ChargeStateAttempt model.
Currently, ChargeStateAttemptV1 is identical to the base ChargeStateAttempt class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .charge_state_attempt import ChargeStateAttempt


class ChargeStateAttemptV1(ChargeStateAttempt, NaProdSQLModel, table=True):
    """
    Version 1 of the ChargeStateAttempt model.

    Currently a name-only inheritance from the base ChargeStateAttempt class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "charge_state_attempt"  # type: ignore
