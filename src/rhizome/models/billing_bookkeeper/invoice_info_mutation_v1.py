"""
SQLModel definition for the invoice_info_mutation table, version 1.

This module provides the V1 implementation of the InvoiceInfoMutation model.
"""

from __future__ import annotations

from .invoice_info_mutation import InvoiceInfoMutation


class InvoiceInfoMutationV1(InvoiceInfoMutation, table=True):
    """
    Version 1 of the InvoiceInfoMutation model.

    Currently a name-only inheritance from the base InvoiceInfoMutation class.
    """

    __tablename__ = "invoice_info_mutation"  # type: ignore
