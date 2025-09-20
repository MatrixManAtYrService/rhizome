"""
Expected data for as_of_merchant_device table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_device_v1 import AsOfMerchantDeviceV1


class AsOfMerchantDeviceDemo(Emplacement[AsOfMerchantDeviceV1]):
    """Expected data for AsOfMerchantDevice in demo environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantDeviceV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_as_of_merchant_device.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return AsOfMerchantDeviceV1.model_validate(data)