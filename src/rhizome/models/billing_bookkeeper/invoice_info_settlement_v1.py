"""
SQLModel definition for the invoice_info_settlement table, version 1.

This module provides the V1 implementation of the InvoiceInfoSettlement model.
"""

from __future__ import annotations

from .invoice_info_settlement import InvoiceInfoSettlement


class InvoiceInfoSettlementV1(InvoiceInfoSettlement, table=True):
    """
    Version 1 of the InvoiceInfoSettlement model.

    Currently a name-only inheritance from the base InvoiceInfoSettlement class.
    """

    __tablename__ = "invoice_info_settlement"  # type: ignore
