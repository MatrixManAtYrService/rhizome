"""
Expected data for flight_check table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.flight_check_v1 import FlightCheckV1


class FlightCheckNaProd(Emplacement[FlightCheckV1]):
    """Expected data for FlightCheck in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FlightCheckV1:
        """Get expected flight_check data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_flight_check.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return FlightCheckV1.model_validate(data)
