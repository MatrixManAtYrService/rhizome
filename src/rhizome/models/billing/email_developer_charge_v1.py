"""
SQLModel definition for the email_developer_charge table, version 1.

This module provides the V1 implementation of the EmailDeveloperCharge model.
Currently, EmailDeveloperChargeV1 is identical to the base EmailDeveloperCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .email_developer_charge import EmailDeveloperCharge


class EmailDeveloperChargeV1(EmailDeveloperCharge, NaProdSQLModel, table=True):
    """
    Version 1 of the EmailDeveloperCharge model.

    Currently a name-only inheritance from the base EmailDeveloperCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "email_developer_charge"  # type: ignore
