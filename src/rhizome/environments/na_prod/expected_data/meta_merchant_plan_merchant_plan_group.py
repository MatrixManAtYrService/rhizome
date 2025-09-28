"""
Emplacement for merchant_plan_merchant_plan_group table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_plan_merchant_plan_group import MerchantPlanMerchantPlanGroup


class MerchantPlanMerchantPlanGroupNaProd(Emplacement[MerchantPlanMerchantPlanGroup]):
    """
    Emplacement for MerchantPlanMerchantPlanGroup in na_prod environment.
    """

    # This class is empty because we are using the default expectation_query.
    # We also don't have expected data for this table yet.
    pass