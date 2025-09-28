"""
SQLModel definition for the charge_invoice_number table, version 1.

This module provides the V1 implementation of the ChargeInvoiceNumber model.
Currently, ChargeInvoiceNumberV1 is identical to the base ChargeInvoiceNumber class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .charge_invoice_number import ChargeInvoiceNumber


class ChargeInvoiceNumberV1(ChargeInvoiceNumber, NaProdSQLModel, table=True):
    """
    Version 1 of the ChargeInvoiceNumber model.

    Currently a name-only inheritance from the base ChargeInvoiceNumber class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "charge_invoice_number"  # type: ignore
