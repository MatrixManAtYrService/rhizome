"""
SQLModel definition for the reseller_invoice_alliance table, version 1.

This module provides the V1 implementation of the ResellerInvoiceAlliance model.
Currently, ResellerInvoiceAllianceV1 is identical to the base ResellerInvoiceAlliance class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .reseller_invoice_alliance import ResellerInvoiceAlliance


class ResellerInvoiceAllianceV1(ResellerInvoiceAlliance, NaProdSQLModel, table=True):
    """
    Version 1 of the ResellerInvoiceAlliance model.

    Currently a name-only inheritance from the base ResellerInvoiceAlliance class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_invoice_alliance"  # type: ignore
