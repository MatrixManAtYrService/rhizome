"""
Emplacement for merchant_merchant_plan_history table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_merchant_plan_history import MerchantMerchantPlanHistory


class MerchantMerchantPlanHistoryNaProd(Emplacement[MerchantMerchantPlanHistory]):
    """
    Emplacement for MerchantMerchantPlanHistory in na_prod environment.
    """

    # This class is empty because we are using the default expectation_query.
    # We also don't have expected data for this table yet.
    pass