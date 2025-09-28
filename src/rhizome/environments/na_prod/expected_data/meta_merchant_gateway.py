"""
Emplacement for merchant_gateway table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_gateway import MerchantGateway


class MerchantGatewayNaProd(Emplacement[MerchantGateway]):
    """
    Emplacement for MerchantGateway in na_prod environment.
    """

    # This class is empty because we are using the default expectation_query.
    # We also don't have expected data for this table yet.
    pass