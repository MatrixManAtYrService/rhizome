"""
SQLModel definition for the disbursement_invoice_number table, version 1.

This module provides the V1 implementation of the DisbursementInvoiceNumber model.
Currently, DisbursementInvoiceNumberV1 is identical to the base DisbursementInvoiceNumber class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .disbursement_invoice_number import DisbursementInvoiceNumber


class DisbursementInvoiceNumberV1(DisbursementInvoiceNumber, NaProdSQLModel, table=True):
    """
    Version 1 of the DisbursementInvoiceNumber model.

    Currently a name-only inheritance from the base DisbursementInvoiceNumber class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "disbursement_invoice_number"  # type: ignore
