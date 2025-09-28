"""
Emplacement for merchant_app_subscription_history table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_app_subscription_history import MerchantAppSubscriptionHistory


class MerchantAppSubscriptionHistoryNaProd(Emplacement[MerchantAppSubscriptionHistory]):
    """
    Emplacement for MerchantAppSubscriptionHistory in na_prod environment.
    """

    # This class is empty because we are using the default expectation_query.
    # We also don't have expected data for this table yet.
    pass