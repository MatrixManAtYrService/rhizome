"""
Expected data for test_merchant_criteria table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.test_merchant_criteria_v1 import TestMerchantCriteriaV1


class TestMerchantCriteriaDemo(Emplacement[TestMerchantCriteriaV1]):
    """Expected data for TestMerchantCriteria in demo environment."""

    @classmethod
    def get_expected(cls) -> TestMerchantCriteriaV1:
        """Get expected test_merchant_criteria data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
