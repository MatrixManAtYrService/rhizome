"""
SQLModel definition for the test_merchant_criteria table, version 1.

This module provides the V1 implementation of the TestMerchantCriteria model.
Currently, TestMerchantCriteriaV1 is identical to the base TestMerchantCriteria class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .test_merchant_criteria import TestMerchantCriteria


class TestMerchantCriteriaV1(TestMerchantCriteria, table=True):
    """
    Version 1 of the TestMerchantCriteria model.

    Currently a name-only inheritance from the base TestMerchantCriteria class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "test_merchant_criteria"  # type: ignore
