"""
Emplacement for device_events table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.meta.device_events import DeviceEvents


class DeviceEventsNaProd(Emplacement[DeviceEvents]):
    """
    Emplacement for DeviceEvents in na_prod environment.
    """

    # This class is empty because we are using the default expectation_query.
    # We also don't have expected data for this table yet.
    pass
