"""
SQLModel definition for the invoice_alliance_code table, version 1.

This module provides the V1 implementation of the InvoiceAllianceCode model.
"""

from __future__ import annotations

from .invoice_alliance_code import InvoiceAllianceCode


class InvoiceAllianceCodeV1(InvoiceAllianceCode, table=True):
    """
    Version 1 of the InvoiceAllianceCode model.

    Currently a name-only inheritance from the base InvoiceAllianceCode class.
    """

    __tablename__ = "invoice_alliance_code"  # type: ignore
