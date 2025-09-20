"""
Expected data for iccid_carrier table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.iccid_carrier_v1 import IccidCarrierV1


class IccidCarrierNaProd(Emplacement[IccidCarrierV1]):
    """Expected data for IccidCarrier in na_prod environment."""

    @classmethod
    def get_expected(cls) -> IccidCarrierV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_iccid_carrier.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return IccidCarrierV1.model_validate(data)
