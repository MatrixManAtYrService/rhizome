"""
SQLModel definition for the invoice_info_settlement_mutation table, version 1.

This module provides the V1 implementation of the InvoiceInfoSettlementMutation model.
"""

from __future__ import annotations

from .invoice_info_settlement_mutation import InvoiceInfoSettlementMutation


class InvoiceInfoSettlementMutationV1(InvoiceInfoSettlementMutation, table=True):
    """
    Version 1 of the InvoiceInfoSettlementMutation model.

    Currently a name-only inheritance from the base InvoiceInfoSettlementMutation class.
    """

    __tablename__ = "invoice_info_settlement_mutation"  # type: ignore
