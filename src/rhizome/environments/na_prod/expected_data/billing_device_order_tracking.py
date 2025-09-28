"""
Expected data for device_order_tracking table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.device_order_tracking_v1 import DeviceOrderTrackingV1


class DeviceOrderTrackingNaProd(Emplacement[DeviceOrderTrackingV1]):
    """Expected data for DeviceOrderTracking in na_prod environment."""

    @classmethod
    def get_expected(cls) -> DeviceOrderTrackingV1:
        """Get expected device_order_tracking data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_device_order_tracking.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return DeviceOrderTrackingV1.model_validate(data)
