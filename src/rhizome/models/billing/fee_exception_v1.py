"""
SQLModel definition for the fee_exception table, version 1.

This module provides the V1 implementation of the FeeException model.
Currently, FeeExceptionV1 is identical to the base FeeException class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .fee_exception import FeeException


class FeeExceptionV1(FeeException, NaProdSQLModel, table=True):
    """
    Version 1 of the FeeException model.

    Currently a name-only inheritance from the base FeeException class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "fee_exception"  # type: ignore
