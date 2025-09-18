"""
Expected data for as_of_merchant_device table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_device_v1 import AsOfMerchantDeviceV1


class AsOfMerchantDeviceDev(Emplacement[AsOfMerchantDeviceV1]):
    """Expected data for AsOfMerchantDevice in dev environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantDeviceV1:
        """Get expected as of merchant device data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )