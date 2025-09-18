"""
Expected data for cellular_billing_arrears_info table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.cellular_billing_arrears_info_v1 import CellularBillingArrearsInfoV1


class CellularBillingArrearsInfoDemo(Emplacement[CellularBillingArrearsInfoV1]):
    """Expected data for CellularBillingArrearsInfo in demo environment."""

    @classmethod
    def get_expected(cls) -> CellularBillingArrearsInfoV1:
        """Get expected cellular billing arrears info data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_cellular_billing_arrears_info.json"
        with open(file_path) as f:
            data = json.load(f)
        return CellularBillingArrearsInfoV1.model_validate(data)