"""
Expected data for flight_check_archive table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.flight_check_archive_v1 import FlightCheckArchiveV1


class FlightCheckArchiveNaProd(Emplacement[FlightCheckArchiveV1]):
    """Expected data for FlightCheckArchive in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FlightCheckArchiveV1:
        """Get expected flight_check_archive data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_flight_check_archive.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return FlightCheckArchiveV1.model_validate(data)
