"""
Emplacement for terminal_config_merchant_props table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.meta.terminal_config_merchant_props import TerminalConfigMerchantProps


class TerminalConfigMerchantPropsNaProd(Emplacement[TerminalConfigMerchantProps]):
    """
    Emplacement for TerminalConfigMerchantProps in na_prod environment.
    """

    # This class is empty because we are using the default expectation_query.
    # We also don't have expected data for this table yet.
    pass