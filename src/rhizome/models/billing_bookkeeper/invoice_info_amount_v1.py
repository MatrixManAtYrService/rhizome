"""
SQLModel definition for the invoice_info_amount table, version 1.

This module provides the V1 implementation of the InvoiceInfoAmount model.
"""

from __future__ import annotations

from .invoice_info_amount import InvoiceInfoAmount


class InvoiceInfoAmountV1(InvoiceInfoAmount, table=True):
    """
    Version 1 of the InvoiceInfoAmount model.

    Currently a name-only inheritance from the base InvoiceInfoAmount class.
    """

    __tablename__ = "invoice_info_amount"  # type: ignore
