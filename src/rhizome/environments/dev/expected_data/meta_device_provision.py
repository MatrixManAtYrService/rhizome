"""
Expected data for device_provision table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.device_provision_v1 import DeviceProvisionV1


class DeviceProvisionDev(Emplacement[DeviceProvisionV1]):
    """Expected data for DeviceProvisionV1 in dev environment."""

    @classmethod
    def get_expected(cls) -> DeviceProvisionV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_device_provision.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return DeviceProvisionV1.model_validate(data)
