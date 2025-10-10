"""
SQLModel definition for the merchant_terms_acceptance_events table, version 1.

This module provides the V1 implementation of the MerchantTermsAcceptanceEvents model.
Currently, MerchantTermsAcceptanceEventsV1 is identical to the base
MerchantTermsAcceptanceEvents class (name-only inheritance), but as the table schema evolves
across environments, future versions (V2, V3, etc.) will contain actual schema differences
(new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_terms_acceptance_events import MerchantTermsAcceptanceEvents


class MerchantTermsAcceptanceEventsV1(MerchantTermsAcceptanceEvents, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantTermsAcceptanceEvents model.

    Currently a name-only inheritance from the base MerchantTermsAcceptanceEvents class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_terms_acceptance_events"  # type: ignore
