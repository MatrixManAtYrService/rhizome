"""
SQLModel definition for the invoice_info table, version 1.
"""

from __future__ import annotations

from .invoice_info import InvoiceInfo


class InvoiceInfoV1(InvoiceInfo, table=True):
    """Version 1 of the InvoiceInfo model."""

    __tablename__ = "invoice_info"  # type: ignore