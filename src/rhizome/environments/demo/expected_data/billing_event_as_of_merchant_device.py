"""
Expected data for as_of_merchant_device table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_device_v1 import AsOfMerchantDeviceV1


class AsOfMerchantDeviceDemo(Emplacement[AsOfMerchantDeviceV1]):
    """Expected data for AsOfMerchantDevice in demo environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantDeviceV1:
        """Get expected as of merchant device data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )