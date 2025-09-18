"""
Expected data for mlc_captured_event table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.mlc_captured_event_v1 import MlcCapturedEventV1


class MlcCapturedEventNaProd(Emplacement[MlcCapturedEventV1]):
    """Expected data for MlcCapturedEvent in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MlcCapturedEventV1:
        """Get expected mlc_captured_event data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
