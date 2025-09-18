"""
Expected data for uninstalled_app table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.uninstalled_app_v1 import UninstalledAppV1


class UninstalledAppNaProd(Emplacement[UninstalledAppV1]):
    """Expected data for UninstalledApp in na_prod environment."""

    @classmethod
    def get_expected(cls) -> UninstalledAppV1:
        """Get expected uninstalled_app data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
