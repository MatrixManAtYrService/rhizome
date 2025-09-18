"""
Expected data for managed_item table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.managed_item_v1 import ManagedItemV1


class ManagedItemNaProd(Emplacement[ManagedItemV1]):
    """Expected data for ManagedItem in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ManagedItemV1:
        """Get expected managed_item data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
