"""
Expected data for test_merchant_criteria table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.test_merchant_criteria_v1 import TestMerchantCriteriaV1


class TestMerchantCriteriaNaProd(Emplacement[TestMerchantCriteriaV1]):
    """Expected data for TestMerchantCriteria in na_prod environment."""

    @classmethod
    def get_expected(cls) -> TestMerchantCriteriaV1:
        """Get expected test_merchant_criteria data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
