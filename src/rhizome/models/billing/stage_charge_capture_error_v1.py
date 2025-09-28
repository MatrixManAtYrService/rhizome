"""
SQLModel definition for the stage_charge_capture_error table, version 1.

This module provides the V1 implementation of the StageChargeCaptureError model.
Currently, StageChargeCaptureErrorV1 is identical to the base StageChargeCaptureError class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_charge_capture_error import StageChargeCaptureError


class StageChargeCaptureErrorV1(StageChargeCaptureError, NaProdSQLModel, table=True):
    """
    Version 1 of the StageChargeCaptureError model.

    Currently a name-only inheritance from the base StageChargeCaptureError class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_charge_capture_error"  # type: ignore
