"""
Expected data for mlc_captured_event table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.mlc_captured_event_v1 import MlcCapturedEventV1


class MlcCapturedEventDemo(Emplacement[MlcCapturedEventV1]):
    """Expected data for MlcCapturedEvent in demo environment."""

    @classmethod
    def get_expected(cls) -> MlcCapturedEventV1:
        """Get expected mlc_captured_event data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
