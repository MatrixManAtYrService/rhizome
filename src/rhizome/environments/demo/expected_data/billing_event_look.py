"""
Expected data for look table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.look_v1 import LookV1


class LookDemo(Emplacement[LookV1]):
    """Expected data for Look in demo environment."""

    @classmethod
    def get_expected(cls) -> LookV1:
        """Get expected look data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )