"""
Expected data for look_data table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.look_data_v1 import LookDataV1


class LookDataNaProd(Emplacement[LookDataV1]):
    """Expected data for LookData in na_prod environment."""

    @classmethod
    def get_expected(cls) -> LookDataV1:
        """Get expected look_data data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
