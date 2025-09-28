"""
SQLModel definition for the billing_business_initiative table, version 1.

This module provides the V1 implementation of the BillingBusinessInitiative model.
Currently, BillingBusinessInitiativeV1 is identical to the base BillingBusinessInitiative class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .billing_business_initiative import BillingBusinessInitiative


class BillingBusinessInitiativeV1(BillingBusinessInitiative, NaProdSQLModel, table=True):
    """
    Version 1 of the BillingBusinessInitiative model.

    Currently a name-only inheritance from the base BillingBusinessInitiative class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "billing_business_initiative"  # type: ignore
