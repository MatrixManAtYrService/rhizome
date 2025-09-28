"""
SQLModel definition for the email_audit table, version 1.

This module provides the V1 implementation of the EmailAudit model.
Currently, EmailAuditV1 is identical to the base EmailAudit class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .email_audit import EmailAudit


class EmailAuditV1(EmailAudit, NaProdSQLModel, table=True):
    """
    Version 1 of the EmailAudit model.

    Currently a name-only inheritance from the base EmailAudit class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "email_audit"  # type: ignore
