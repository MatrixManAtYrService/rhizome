"""
Expected data for mlc_captured_event table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.mlc_captured_event_v1 import MlcCapturedEventV1


class MlcCapturedEventDev(Emplacement[MlcCapturedEventV1]):
    """Expected data for MlcCapturedEvent in dev environment."""

    @classmethod
    def get_expected(cls) -> MlcCapturedEventV1:
        """Get expected mlc_captured_event data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
