"""
SQLModel definition for the offboarding table, version 1.

This module provides the V1 implementation of the Offboarding model.
Currently, OffboardingV1 is identical to the base Offboarding class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .offboarding import Offboarding


class OffboardingV1(Offboarding, NaProdSQLModel, table=True):
    """
    Version 1 of the Offboarding model.

    Currently a name-only inheritance from the base Offboarding class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "offboarding"  # type: ignore
