"""
Expected data for cellular_arrears_acceptances table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.cellular_arrears_acceptances_v1 import CellularArrearsAcceptancesV1


class CellularArrearsAcceptancesDev(Emplacement[CellularArrearsAcceptancesV1]):
    """Expected data for CellularArrearsAcceptances in dev environment."""

    @classmethod
    def get_expected(cls) -> CellularArrearsAcceptancesV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_cellular_arrears_acceptances.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run \'rhizome sync data\' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return CellularArrearsAcceptancesV1.model_validate(data)