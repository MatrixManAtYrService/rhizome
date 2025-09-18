"""
Expected data for uninstalled_app table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.uninstalled_app_v1 import UninstalledAppV1


class UninstalledAppDev(Emplacement[UninstalledAppV1]):
    """Expected data for UninstalledApp in dev environment."""

    @classmethod
    def get_expected(cls) -> UninstalledAppV1:
        """Get expected uninstalled_app data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
