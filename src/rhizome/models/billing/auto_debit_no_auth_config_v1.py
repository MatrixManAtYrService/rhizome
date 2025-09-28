"""
SQLModel definition for the auto_debit_no_auth_config table, version 1.

This module provides the V1 implementation of the AutoDebitNoAuthConfig model.
Currently, AutoDebitNoAuthConfigV1 is identical to the base AutoDebitNoAuthConfig class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .auto_debit_no_auth_config import AutoDebitNoAuthConfig


class AutoDebitNoAuthConfigV1(AutoDebitNoAuthConfig, NaProdSQLModel, table=True):
    """
    Version 1 of the AutoDebitNoAuthConfig model.

    Currently a name-only inheritance from the base AutoDebitNoAuthConfig class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "auto_debit_no_auth_config"  # type: ignore