"""
Expected data for iccid_carrier table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.iccid_carrier_v1 import IccidCarrierV1


class IccidCarrierNaProd(Emplacement[IccidCarrierV1]):
    """Expected data for IccidCarrier in na_prod environment."""

    @classmethod
    def get_expected(cls) -> IccidCarrierV1:
        """Get expected iccid carrier data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )