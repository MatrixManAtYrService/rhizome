"""
Expected data for cellular_billing_arrears_info table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.cellular_billing_arrears_info_v1 import CellularBillingArrearsInfoV1


class CellularBillingArrearsInfoNaProd(Emplacement[CellularBillingArrearsInfoV1]):
    """Expected data for CellularBillingArrearsInfo in na_prod environment."""

    @classmethod
    def get_expected(cls) -> CellularBillingArrearsInfoV1:
        """Get expected cellular billing arrears info data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_cellular_billing_arrears_info.json"
        with open(file_path) as f:
            data = json.load(f)
        return CellularBillingArrearsInfoV1.model_validate(data)