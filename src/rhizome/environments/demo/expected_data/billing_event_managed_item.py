"""
Expected data for managed_item table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.managed_item_v1 import ManagedItemV1


class ManagedItemDemo(Emplacement[ManagedItemV1]):
    """Expected data for ManagedItem in demo environment."""

    @classmethod
    def get_expected(cls) -> ManagedItemV1:
        """Get expected managed_item data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
