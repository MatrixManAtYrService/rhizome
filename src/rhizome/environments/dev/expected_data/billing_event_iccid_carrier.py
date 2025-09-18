"""
Expected data for iccid_carrier table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.iccid_carrier_v1 import IccidCarrierV1


class IccidCarrierDev(Emplacement[IccidCarrierV1]):
    """Expected data for IccidCarrier in dev environment."""

    @classmethod
    def get_expected(cls) -> IccidCarrierV1:
        """Get expected iccid carrier data for dev environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_iccid_carrier.json"
        with open(file_path) as f:
            data = json.load(f)
        return IccidCarrierV1.model_validate(data)