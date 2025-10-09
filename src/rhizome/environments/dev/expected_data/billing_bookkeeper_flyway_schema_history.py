"""Expected data for flyway_schema_history table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.flyway_schema_history_v1 import FlywaySchemaHistoryV1


class FlywaySchemaHistoryDev(Emplacement[FlywaySchemaHistoryV1]):
    """Expected data for FlywaySchemaHistory in dev environment."""

    @classmethod
    def get_expected(cls) -> FlywaySchemaHistoryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_flyway_schema_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FlywaySchemaHistoryV1.model_validate(data)
