"""
Expected data for flight_check_execution table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.flight_check_execution_v1 import FlightCheckExecutionV1


class FlightCheckExecutionNaProd(Emplacement[FlightCheckExecutionV1]):
    """Expected data for FlightCheckExecution in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FlightCheckExecutionV1:
        """Get expected flight_check_execution data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_flight_check_execution.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return FlightCheckExecutionV1.model_validate(data)
