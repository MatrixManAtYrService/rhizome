"""
Expected data for iccid_carrier table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.iccid_carrier_v1 import IccidCarrierV1


class IccidCarrierDemo(Emplacement[IccidCarrierV1]):
    """Expected data for IccidCarrier in demo environment."""

    @classmethod
    def get_expected(cls) -> IccidCarrierV1:
        """Get expected iccid carrier data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )