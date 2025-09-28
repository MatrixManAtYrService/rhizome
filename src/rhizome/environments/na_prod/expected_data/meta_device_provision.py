"""
Expected data for device_provision table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.device_provision import DeviceProvision


class DeviceProvisionNaProd(Emplacement[DeviceProvision]):
    """Expected data for DeviceProvision in na_prod environment."""

    @classmethod
    def get_expected(cls) -> DeviceProvision:
        """Get expected device_provision data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_device_provision.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return DeviceProvision.model_validate(data)
