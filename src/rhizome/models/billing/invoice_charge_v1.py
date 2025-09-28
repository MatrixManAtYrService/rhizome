"""
SQLModel definition for the invoice_charge table, version 1.

This module provides the V1 implementation of the InvoiceCharge model.
Currently, InvoiceChargeV1 is identical to the base InvoiceCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .invoice_charge import InvoiceCharge


class InvoiceChargeV1(InvoiceCharge, NaProdSQLModel, table=True):
    """
    Version 1 of the InvoiceCharge model.

    Currently a name-only inheritance from the base InvoiceCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "invoice_charge"  # type: ignore
