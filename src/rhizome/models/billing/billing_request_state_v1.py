"""
SQLModel definition for the billing_request_state table, version 1.

This module provides the V1 implementation of the BillingRequestState model.
Currently, BillingRequestStateV1 is identical to the base BillingRequestState class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .billing_request_state import BillingRequestState


class BillingRequestStateV1(BillingRequestState, NaProdSQLModel, table=True):
    """
    Version 1 of the BillingRequestState model.

    Currently a name-only inheritance from the base BillingRequestState class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "billing_request_state"  # type: ignore
