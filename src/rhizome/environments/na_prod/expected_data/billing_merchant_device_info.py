"""
Expected data for merchant_device_info table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_device_info_v1 import MerchantDeviceInfoV1


class MerchantDeviceInfoNaProd(Emplacement[MerchantDeviceInfoV1]):
    """Expected data for MerchantDeviceInfo in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantDeviceInfoV1:
        """Get expected merchant_device_info data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_device_info.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantDeviceInfoV1.model_validate(data)
