"""SQLModel definition for the merchant_evolution table, version 1.

This module provides the V1 implementation of the MerchantEvolution model.
Currently, MerchantEvolutionV1 is identical to the base MerchantEvolution class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .merchant_evolution import MerchantEvolution


class MerchantEvolutionV1(MerchantEvolution, table=True):
    """Version 1 of the MerchantEvolution model.

    Currently a name-only inheritance from the base MerchantEvolution class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_evolution"  # type: ignore