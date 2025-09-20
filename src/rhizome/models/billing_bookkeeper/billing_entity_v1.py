"""
SQLModel definition for the billing_entity table, version 1.

This module provides the V1 implementation of the BillingEntity model.
Currently, BillingEntityV1 is identical to the base BillingEntity class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .billing_entity import BillingEntity


class BillingEntityV1(BillingEntity, table=True):
    """
    Version 1 of the BillingEntity model.

    Currently a name-only inheritance from the base BillingEntity class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "billing_entity"  # type: ignore
